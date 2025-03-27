import pytest
import logging
from playwright.sync_api import expect
from pages.discovery_page import DiscoveryPage

logger = logging.getLogger(__name__)

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
