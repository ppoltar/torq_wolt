import pytest
import logging
import os
import subprocess
from playwright.sync_api import sync_playwright
logger = logging.getLogger(__name__)

TRACE_DIR = "reports/playwright-traces"


@pytest.fixture(scope="function")
def page(request):
    test_name = request.node.name
    trace_path = f"{TRACE_DIR}/{test_name}-trace.zip"

    with sync_playwright() as p:
        logger.info("Launching browser...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()

        yield page

        logger.info(f"Test: {test_name} completed. Saving trace...")
        context.tracing.stop(path=trace_path)
        browser.close()



def pytest_sessionfinish():
    """
    This function is a pytest hook that is called after the test session has finished.
    It generates an Allure report if the raw Allure results are available.
    """
    allure_results_dir = "reports/allure-results"
    allure_report_dir = "reports/allure-report"

    if os.path.exists(allure_results_dir):
        logging.info("Generating Allure report...")
        subprocess.run(["allure", "generate", allure_results_dir, "--clean", "-o", allure_report_dir])
