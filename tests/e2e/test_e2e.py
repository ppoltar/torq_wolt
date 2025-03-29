import pytest
import logging
import allure
from pages.discovery_page import DiscoveryPage
from tests.e2e.e2e_data import e2e_test_data
from playwright.sync_api import expect

logger = logging.getLogger(__name__)

@allure.description("""
    Test E2E verifies the functionality of the search, filtering, and ordering process on the discovery page.
    The test simulates the flow of a user searching, applying filters, selecting items, adding them to the order,viewing the order details and try to order.

    Steps:
    1. Navigate to the discovery page.
    2. Search for a text in the search bar.
    3. Apply filter options if available.
    4. Click on the first venue card.
    5. Choose the first item in the card and go through all the available options in order.
    6. Add the selected item to the order.
    7. View the order and click on the price button.
    8. Check that the search mail text field is editable.

    Expected Results:
    - The search bar should accept the input and return relevant results.
    - The filter options (if any) should be applied successfully.
    - The venue and item selection process should function correctly.
    - The order should be successfully added, and the price button should be clickable.
    - The search mail text field should be editable after the order process.
""")
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
    discovery_page.click_on_add_order()

    logger.info(f"View order ad click on price button.")
    discovery_page.click_card_view_button()
    discovery_page.click_card_total_price_button()

    logger.info(f"Checking that the search mail text editable.")
    expect(discovery_page.search_mail_text()).to_be_editable()
    logger.info(f"Finished  {test_data['case']} test.")
