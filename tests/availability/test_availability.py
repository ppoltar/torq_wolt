import pytest
import logging
import allure
from playwright.sync_api import expect
from pages.discovery_page import DiscoveryPage

logger = logging.getLogger(__name__)

@allure.description("""
    Test Verifies the availability of key elements on the discovery page:
    - Search input field
    - Address bar button
    - Main discovery content area

    The test checks that these elements are visible and enabled.

    Steps:
    1. Navigate to the discovery page.
    2. Check visibility and enabled state for each element.
    3. Log the results.
    
    Expected Results:
    - The search input field should be visible and enabled.
    - The address bar button should be visible and enabled.
    - The main discovery content area should be visible on the page.
""")
@pytest.mark.availability
def test_availability(page,):
    logger.info(f"Starting availability test.")
    discovery_page = DiscoveryPage(page)
    discovery_page.go_to_discovery_page()

    logger.info(f"Checking search input visible and enable.")
    expect(discovery_page.search_input_locator()).to_be_visible()
    expect(discovery_page.search_input_locator()).to_be_enabled()

    logger.info(f"Checking address bar visible and enable.")
    expect(discovery_page.address_bar_button_locator()).to_be_visible()
    expect(discovery_page.address_bar_button_locator()).to_be_enabled()

    logger.info(f"Checking main page discovery content visible.")
    expect(discovery_page.main_discovery_content()).to_be_visible()
    logger.info(f"Finished availability test.")
