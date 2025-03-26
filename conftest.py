import pytest
import logging
import os
import subprocess
from playwright.sync_api import sync_playwright
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def page(request):
    test_name = request.node.name
    trace_path = f"reports/playwright-traces/{test_name}-trace.zip"

    with sync_playwright() as p:
        logger.info("Launching browser...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()
        yield page
        logger.info("Test completed. Saving trace...")
        context.tracing.stop(path=trace_path)
        browser.close()

# This function will be executed at the end of the test session
# generate index.html report for allure
def pytest_sessionfinish(session, exitstatus):
    allure_results_dir = "reports/allure-results"
    allure_report_dir = "reports/allure-report"

    if os.path.exists(allure_results_dir):
        print("Generating Allure report...")
        subprocess.run(["allure", "generate", allure_results_dir, "--clean", "-o", allure_report_dir])
