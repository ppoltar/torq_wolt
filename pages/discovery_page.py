import logging
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

    def search_mail_text(self):
        return self.page.locator(WoltLocators.LOGIN_EMAIL_INPUT)

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

    def search_in_wolt(self, input_text: str):
        search_box = self.search_input_locator()
        search_box.clear()
        search_box.fill(input_text)
        search_box.press('Enter')

    def address_bar_button_locator(self):
        return self.page.locator(WoltLocators.ADDRESS_BAR_BUTTON).nth(0)

    def choose_country_in_address_popup(self, country: str):
        self.address_bar_button_locator().click()
        self.page.wait_for_selector(WoltLocators.COUNTRY_SELECT)
        self.page.select_option(WoltLocators.COUNTRY_SELECT, label=country)

    def choose_stree_in_address_popup(self, street: str ):
        self.page.wait_for_selector(WoltLocators.STREET_INPUT)
        self.page.locator(WoltLocators.STREET_INPUT).clear()
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

    def find_sort_filter(self):
        try:
            if self.page.wait_for_selector(WoltLocators.SORT_FILTER_BUTTON, timeout=5000):
                return self.page.locator(WoltLocators.SORT_FILTER_BUTTON)
        except Exception:
            logging.warning(f"Cannot find the filter, maybe next time...")  # Optional: You can log the error for debugging
            return False

    def sorted_filter_by_recommended(self, filters: list):
        self.page.locator(WoltLocators.SORT_FILTER_BUTTON).click()
        for filter in filters:
            logging.info(f'Choosing filter: {filter}')
            self.page.locator(filter).scroll_into_view_if_needed()
            self.page.locator(filter).click()
        self.page.locator(WoltLocators.FILTER_APPLY_BUTTON).click()

    def click_first_venue_card(self):
        self.page.locator(WoltLocators.VENUE_CARD).nth(0).click()

    def click_first_available_item_card(self):
        self.page.wait_for_selector(WoltLocators.ITEM_CARD_BUTTON, timeout=5000)
        item_buttons = self.page.locator(WoltLocators.ITEM_CARD_BUTTON).all()
        for item in item_buttons:
            item.scroll_into_view_if_needed()
            parent_card = item.locator("..")
            if parent_card.locator('text="Not available"').is_visible():
                logging.warning(f'The item not available...continue to next')
                continue
            else:
                item.click()
                break

    def choose_all_first_option_in_order(self):
        option_groups_list = self.page.locator(WoltLocators.PRODUCT_OPTIONS_GROUP).all()
        for option_group in option_groups_list:
            first_locator = option_group.locator(WoltLocators.CHECK_OPTION).nth(0)
            first_locator.wait_for(state="visible", timeout=5000)
            option_type = first_locator.get_attribute('type')
            if option_type == 'checkbox':
                first_locator.locator("..").click()

    def add_order(self):
        self.page.locator(WoltLocators.PRODUCT_ORDER_SUBMIT).click()

    def click_card_view_button(self):
        self.page.locator(WoltLocators.CARD_VIEW_BUTTON).nth(0).click()

    def click_card_total_price_button(self):
        self.page.locator(WoltLocators.CARD_TOTAL_PRICE_BUTTON).click()
