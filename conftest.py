import pytest
import logging
import os
import subprocess
import shutil
import allure
from playwright.sync_api import sync_playwright
logger = logging.getLogger(__name__)

# Define directories
REPORTS_DIR = "reports"  # Define the reports directory
ALLURE_RESULTS_DIR = "reports/allure-results"
ALLURE_REPORT_DIR = "reports/allure-report"
VIDEO_DIR = "reports/videos"
SCREENSHOT_DIR = "reports/screenshots"
TRACE_DIR = "reports/playwright-traces"

@pytest.fixture(scope="session", autouse=True)
def cleanup_reports():
    """
    This fixture will delete the existing reports directory before running any tests and
    recreate it with necessary subdirectories.
    It is automatically invoked at the start of the test session.

    The directories that will be created are:
        - reports/
        - reports/allure-results/
        - reports/allure-report/
        - reports/videos/
        - reports/screenshots/
        - reports/traces/
    """
    if os.path.exists(REPORTS_DIR):
        logging.info(f"Deleting existing {REPORTS_DIR} directory...")
        shutil.rmtree(REPORTS_DIR, ignore_errors=True)
        logging.info(f"{REPORTS_DIR} DELETED directory...")

    os.makedirs(REPORTS_DIR, exist_ok=True)
    os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)
    os.makedirs(ALLURE_REPORT_DIR, exist_ok=True)
    os.makedirs(VIDEO_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    logger.info(
        f"Directories {REPORTS_DIR}, {ALLURE_RESULTS_DIR}, {ALLURE_REPORT_DIR}, {VIDEO_DIR}, and {SCREENSHOT_DIR} are ready.")


@pytest.fixture(scope="function")
def page(request):
    """
     This fixture is responsible for setting up and tearing down a Playwright page for each test.
     It performs the following tasks:
     - Launches a browser and sets up a new context with video recording and trace capturing.
     - Provides a Playwright page for the test to interact with.
     - Captures a video of the test run and saves it to a file.
     - Takes a screenshot if the test fails and attaches the video and screenshot to the Allure report.

     Parameters:
     - request (pytest fixture): The pytest request object, used to access test metadata such as test name and results.

     Yields:
     - page (playwright.page.Page): The Playwright page object that the test can interact with.
     """
    test_name = request.node.name
    video_path = f"{VIDEO_DIR}/{test_name}.webm"
    screenshot_path = f"{SCREENSHOT_DIR}/{test_name}.png"
    trace_path = f"{TRACE_DIR}/{test_name}-trace.zip"

    with sync_playwright() as p:
        logger.info("Launching browser...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir=VIDEO_DIR)
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()

        yield page

        # After the test completes, check if the test failed and attach video/screenshot
        if request.node.rep_call.failed:
            page.screenshot(path=screenshot_path)
            logger.info(f"Screenshot saved at: {screenshot_path}")
            allure.attach.file(screenshot_path,
                               name=f"falling_screenshot_{test_name}",
                               attachment_type=allure.attachment_type.PNG)

            logger.info(f"Test {test_name} failed. Attaching video: {video_path}")
            video_files = [f for f in os.listdir(VIDEO_DIR) if f.endswith(".webm")]
            temp_video_path = os.path.join(VIDEO_DIR, video_files[-1])
            shutil.move(temp_video_path, video_path)
            allure.attach.file(video_path,
                               name=f"falling_video_{test_name}",
                               attachment_type=allure.attachment_type.WEBM)
        else:
            logger.info(f"Test {test_name} passed! God Job!")

        logger.info(f"Test: {test_name} completed. Saving trace...")
        context.tracing.stop(path=trace_path)
        browser.close()


def pytest_sessionfinish():
    """
    This function is a pytest hook that is called after the test session has finished.
    It generates an Allure report if the raw Allure results are available.
    """

    if os.path.exists(ALLURE_RESULTS_DIR):
        logging.info("Generating Allure report...")
        subprocess.run(["allure", "generate", ALLURE_RESULTS_DIR, "--clean", "-o", ALLURE_REPORT_DIR])



def pytest_configure():
    """
    This function is a pytest hook that is called to configure logging settings
    before the test session starts.
    It sets up the basic logging configuration with INFO level.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')