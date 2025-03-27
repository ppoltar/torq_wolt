import pytest
import logging
from playwright.sync_api import expect
from pages.discovery_page import DiscoveryPage
from tests.address_bar.address_bar_data import address_bar_test_data

logger = logging.getLogger(__name__)

@pytest.mark.address_bar
@pytest.mark.parametrize("test_data", address_bar_test_data, ids=[data["case"] for data in address_bar_test_data])
def test_address_bar(page, test_data):
    logger.info(f"Starting test address bar for: {test_data['case']}.")
    discovery_page = DiscoveryPage(page)
    discovery_page.go_to_discovery_page()

    logger.info(f"Choosing country:{test_data['country']} in address bar.")
    discovery_page.choose_country_in_address_popup(test_data["country"])
    expect(discovery_page.address_continue_button()).to_be_disabled()

    logger.info(f"Choosing Street:{test_data['street']} in address bar.")
    discovery_page.choose_stree_in_address_popup(test_data["street"])
    discovery_page.address_continue_button().click()

    logger.info(f"Checking main page discovery content visible.")
    expect(discovery_page.main_discovery_content()).to_be_visible(timeout=60000)
    logger.info(f"Finished test: {test_data['case']}.")