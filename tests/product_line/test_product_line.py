import pytest
import logging
from pages.discovery_page import DiscoveryPage
from playwright.sync_api import expect
from tests.product_line.product_line_data import product_line_test_data


logger = logging.getLogger(__name__)

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
    expect(discovery_page.find_venue_content()).to_be_visible()
    logger.info(f"Finished test: {test_data['case']}.")