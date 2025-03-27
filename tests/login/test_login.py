import pytest
import logging
from playwright.sync_api import expect
from pages.discovery_page import DiscoveryPage
from tests.login.login_data import login_test_data

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("test_data", login_test_data, ids=[data["case"] for data in login_test_data])
def test_login(page, test_data):
    logger.info(f"Starting test: {test_data['case']}.")
    discovery_page = DiscoveryPage(page)
    discovery_page.go_to_discovery_page()

    logger.info(f"Insert mail and click next button")
    discovery_page.click_login_button()
    discovery_page.insert_login_mail(test_data["mail"])
    discovery_page.click_on_login_next_button()

    logger.info(f"Checking popup expected element visible and enabled.")
    expect(discovery_page.resent_mail_login_button()).to_be_visible()
    expect(discovery_page.resent_mail_login_button()).to_be_enabled()
    logger.info(f"Finished test: {test_data['case']}.")
