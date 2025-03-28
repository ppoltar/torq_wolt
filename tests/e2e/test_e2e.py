import pytest
import logging
from pages.discovery_page import DiscoveryPage
from tests.e2e.e2e_data import e2e_test_data
from playwright.sync_api import expect

logger = logging.getLogger(__name__)

@pytest.mark.e2e
@pytest.mark.parametrize("test_data", e2e_test_data, ids=[data["case"] for data in e2e_test_data])
def test_e2e(page, test_data):
    logger.info(f"Starting test: {test_data['case']}.")
    discovery_page = DiscoveryPage(page)
    discovery_page.go_to_discovery_page()

    logger.info(f"Searching in search bar: {test_data['search_text']}.")
    discovery_page.search_in_wolt(test_data['search_text'])

    logger.info(f"Choose filter option if filter appears")
    if discovery_page.find_sort_filter():
        discovery_page.sorted_filter_by_recommended(test_data['filters'])

    logger.info(f"Choose first venue card.")
    discovery_page.click_first_venue_card()

    logger.info(f"Choose first item in the card and check all first option in order.")
    discovery_page.click_first_available_item_card()
    discovery_page.choose_all_first_option_in_order()

    logger.info(f"Adding order.")
    discovery_page.add_order()

    logger.info(f"View order ad click on price button.")
    discovery_page.click_card_view_button()
    discovery_page.click_card_total_price_button()

    logger.info(f"Checking that the search mail text editable.")
    expect(discovery_page.search_mail_text()).to_be_editable()
    logger.info(f"Finished  {test_data['case']} test.")
