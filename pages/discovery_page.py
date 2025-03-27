from playwright.sync_api import Page
from locators.wolt_locators import WoltLocators

class DiscoveryPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_discovery_page(self):
        self.page.goto(WoltLocators.DISCOVERY_URL)
        self.page.locator(WoltLocators.PRODUCTS_LINE).wait_for(state="visible", timeout=60000)

    def click_login_button(self):
        self.page.click(WoltLocators.LOGIN_BUTTON)

    def insert_login_mail(self, mail: str):
        self.page.wait_for_selector(WoltLocators.LOGIN_EMAIL_INPUT)
        self.page.fill(WoltLocators.LOGIN_EMAIL_INPUT, mail)

    def click_on_login_next_button(self):
        self.page.locator(WoltLocators.LOGIN_NEXT_BUTTON).click()

    def resent_mail_login_button(self):
        return self.page.locator(WoltLocators.LOGIN_MAIL_RESEND_BUTTON)

    def click_signup_button(self):
        self.page.click(WoltLocators.LOGIN_BUTTON)

    def click_on_signup_partner(self, partner: str, popup: bool):
        self.page.click(partner)
        if popup:
            popup_page = self.page.context.wait_for_event('page')
            return popup_page
        else:
            return self.page

    def search_input_locator(self):
        return self.page.locator(WoltLocators.SEARCH_INPUT)

    def address_bar_button_locator(self):
        return self.page.locator(WoltLocators.ADDRESS_BAR_BUTTON).nth(0)

    def choose_country_in_address_popup(self, country: str):
        self.address_bar_button_locator().click()
        self.page.wait_for_selector(WoltLocators.COUNTRY_SELECT)
        self.page.select_option(WoltLocators.COUNTRY_SELECT, label=country)

    def choose_stree_in_address_popup(self, street: str ):
        self.page.wait_for_selector(WoltLocators.STREET_INPUT)
        self.page.fill(WoltLocators.STREET_INPUT, "")
        self.page.fill(WoltLocators.STREET_INPUT, street)
        self.page.locator(WoltLocators.STREET_SUGGESTIONS_LIST).locator("li").nth(0).click()

    def address_continue_button(self):
        return self.page.locator(WoltLocators.ADDRESS_CONTINUE_BUTTON)

    def main_discovery_content(self):
        return self.page.locator(WoltLocators.MAIN_DISCOVERY_CONTENT)

    def choose_tab_by_name(self, name: str):
        self.page.get_by_role("tab", name=name).click()

    def choose_product_line_category(self, category: str):
        self.page.locator(WoltLocators.PRODUCTS_LINE_BUTTON).click()
        self.page.locator(WoltLocators.PRODUCT_LINE_CATEGORY.format(category=category)).click()

    def discovery_page_title(self):
        return self.page.locator(WoltLocators.DISCOVERY_PAGE_TITLE)

    def find_venue_content(self):
        return self.page.locator(WoltLocators.VENUE_CONTENT_LIST)