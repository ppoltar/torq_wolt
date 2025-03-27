import pytest
import logging
from pages.discovery_page import DiscoveryPage
from playwright.sync_api import expect
from tests.tabs.tabs_data import tabs_test_data

logger = logging.getLogger(__name__)

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


