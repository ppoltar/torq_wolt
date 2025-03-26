from playwright.sync_api import Page
from locators.wolt_locators import WoltLocators

class DiscoveryPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_discovery_page(self):
        self.page.goto(WoltLocators.DISCOVERY_URL)
        self.page.locator(WoltLocators.PRODUCTS_LINE).wait_for(state="visible")

    def click_login_button(self):
        self.page.click(WoltLocators.LOGIN_BUTTON)

    def click_signup_button(self):
        self.page.click(WoltLocators.LOGIN_BUTTON)

    def click_on_signup_partner(self, partner: str, popup: bool):
        self.page.click(partner)
        if popup:
            popup_page = self.page.context.wait_for_event('page')
            return popup_page
        else:
            return self.page

