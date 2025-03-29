import pytest
import logging
import allure
from pages.discovery_page import DiscoveryPage
from playwright.sync_api import expect
from tests.tabs.tabs_data import tabs_test_data

logger = logging.getLogger(__name__)


@allure.description("""
    Test Verifies the functionality of selecting tabs on the discovery page.
    The test runs for each tab specified in the test data and checks if the expected elements are visible after selecting the tab.

    Steps:
    1. Navigate to the discovery page.
    2. Click on the specified tab.
    3. Verify the visibility of the expected element for the tab.
    4. Ensure the main discovery content is visible on the page.

    Expected Results:
    - The expected element (defined in the test data) should be visible after clicking the corresponding tab.
    - The main discovery content should be visible after the tab interaction.
""")
@pytest.mark.tabs
@pytest.mark.parametrize("test_data", tabs_test_data, ids=[data["case"] for data in tabs_test_data])
def test_tabs(page, test_data):
    logger.info(f"Starting test: {test_data['case']}")
    discovery_page = DiscoveryPage(page)
    discovery_page.go_to_discovery_page()

    logger.info(f"Clicking on tab: {test_data['tab']}.")
    discovery_page.choose_tab_by_name(test_data["tab"])

    logger.info(f"Checking expected elements to be visible.")
    expect(discovery_page.page.locator(test_data['expected_element'])).to_be_visible()

    logger.info(f"Checking main page discovery content visible.")
    expect(discovery_page.main_discovery_content()).to_be_visible()
    logger.info(f"Finished test: {test_data['case']}.")


