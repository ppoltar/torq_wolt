import pytest
import logging
import allure
from pages.discovery_page import DiscoveryPage
from tests.sign_up.signup_data import signup_test_data
from playwright.sync_api import expect

logger = logging.getLogger(__name__)

@allure.description("""
    Test Verifies the sign-up process by navigating to the Wolt discovery page and interacting with the sign-up button.
    The test runs for each set of sign-up data provided in the test data.

    Steps:
    1. Navigate to the discovery page.
    2. Click the sign-up button.
    3. Choose a partner to sign up with based on test data.
    4. Check that the partner's sign-up page or popup opens correctly.

    Expected Results:
    - The partner's page or popup should open as expected.
    - The specified element on the partner's page/popup should be visible.
""")
@pytest.mark.signup
@pytest.mark.parametrize("test_data", signup_test_data, ids=[data["case"] for data in signup_test_data])
def test_signup(page, test_data):
    logger.info(f"Starting test: {test_data['case']} sign-up and navigate to wolt discovery page.")
    discovery_page = DiscoveryPage(page)
    discovery_page.go_to_discovery_page()

    logger.info(f"Clicking sign-up button and choosing partner to sign-up: {test_data['case']}.")
    discovery_page.click_signup_button()
    new_page = discovery_page.click_on_signup_partner(test_data["partner"], popup=test_data["popup"])

    logger.info(f"Checking partner page/popup opened as expected.")
    expect(new_page.locator(test_data["element_to_check"])).to_be_visible()
    logger.info(f"Finished test: {test_data['case']}.")