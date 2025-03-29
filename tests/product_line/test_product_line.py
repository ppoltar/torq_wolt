import pytest
import logging
import allure
from pages.discovery_page import DiscoveryPage
from playwright.sync_api import expect
from tests.product_line.product_line_data import product_line_test_data

logger = logging.getLogger(__name__)

@allure.description("""
    Test Verifies the functionality of choosing a product line category on the discovery page.
    The test runs for each category in the test data and checks if the expected title and venue content are visible.

    Steps:
    1. Navigate to the discovery page.
    2. Choose a product line category from the available options.
    3. Verify that the expected title for the category is visible.
    4. Ensure that the venue content for the selected product line category is visible.

    Expected Results:
    - The expected title for the category should be visible on the page.
    - The venue content for the selected category should be visible.
""")
@pytest.mark.product_line
@pytest.mark.parametrize("test_data", product_line_test_data, ids=[data["case"] for data in product_line_test_data])
def test_product_line(page, test_data):
    logger.info(f"Starting test: {test_data['case']}")
    discovery_page = DiscoveryPage(page)
    discovery_page.go_to_discovery_page()

    logger.info(f"Choosing category: {test_data['category']} from product line.")
    discovery_page.choose_product_line_category(test_data['category'])

    logger.info(f"Checking expected title name visible.")
    expect(discovery_page.discovery_page_title()).to_have_text(test_data['title'])

    logger.info(f"Checking page discovery venue content visible.")
    expect(discovery_page.venue_content()).to_be_visible()
    logger.info(f"Finished test: {test_data['case']}.")