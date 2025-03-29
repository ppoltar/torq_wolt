import logging
from playwright.sync_api import Page
from locators.wolt_locators import WoltLocators

logger = logging.getLogger(__name__)


class DiscoveryPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_discovery_page(self):
        """
        Navigates to the Wolt Discovery page and waits for the product line to be visible.
        Raises:
            Exception: If navigation fails or the product line is not visible.
        """
        try:
            self.page.goto(WoltLocators.DISCOVERY_URL)
            self.page.locator(WoltLocators.PRODUCTS_LINE).wait_for(state="visible", timeout=60000)
        except Exception as e:
            error_message = f"Failed to go to the page: {WoltLocators.DISCOVERY_URL}. Error: {str(e)}"
            logger.error(error_message)
            raise Exception(f"Page navigation failed: {error_message}")

    def click_login_button(self):
        """
        Clicks the login button on the Discovery page.
        """
        self.page.click(WoltLocators.LOGIN_BUTTON)

    def search_mail_text(self):
        """
        Returns the locator for the email input field in the login form.
        Returns:
            Locator: The locator for the email input field.
        """
        return self.page.locator(WoltLocators.LOGIN_EMAIL_INPUT)

    def insert_login_mail(self, mail: str):
        """
        Inserts the given email into the email input field on the login form.
        Args:
            mail: The email address to insert.
        """
        self.page.wait_for_selector(WoltLocators.LOGIN_EMAIL_INPUT)
        self.page.fill(WoltLocators.LOGIN_EMAIL_INPUT, mail)

    def click_on_login_next_button(self):
        """
        Clicks the 'Next' button on the login form.
        """
        self.page.locator(WoltLocators.LOGIN_NEXT_BUTTON).click()

    def resent_mail_login_button(self):
        """
        Returns the locator for the 'Resend Mail' button on the login form.
        Returns:
            Locator: The locator for the 'Resend Mail' button.
        """
        return self.page.locator(WoltLocators.LOGIN_MAIL_RESEND_BUTTON)

    def click_signup_button(self):
        """
        Clicks the sign-up button on the Discovery page.
        """
        self.page.click(WoltLocators.SIGNUP_BUTTON)

    def click_on_signup_partner(self, partner: str, popup: bool):
        """
           Clicks on a signup partner and optionally handles the popup.
           Args:
               partner: The name of the partner to click.
               popup: If True, waits for the popup page and returns it. Otherwise, returns the current page.
           Returns:
               Page: The new page if popup is True, or the current page otherwise.
           """
        self.page.click(partner)
        if popup:
            popup_page = self.page.context.wait_for_event('page')
            return popup_page
        else:
            return self.page

    def search_input_locator(self):
        """
        Returns the locator for the search input field on the Discovery page.
        Returns:
            Locator: The locator for the search input field.
        """
        return self.page.locator(WoltLocators.SEARCH_INPUT)

    def search_in_wolt(self, input_text: str):
        """
        Clears the search input field, enters the provided text, and submits the search.
        Args:
            input_text: The text to search for.
        """
        search_box = self.search_input_locator()
        search_box.clear()
        search_box.fill(input_text)
        search_box.press('Enter')

    def address_bar_button_locator(self):
        """
        Returns the locator for the address bar button.
        Returns:
            Locator: The locator for the address bar button.
        """
        return self.page.locator(WoltLocators.ADDRESS_BAR_BUTTON).nth(0)

    def choose_country_in_address_popup(self, country: str):
        """
        Selects a country from the address selection popup.
        Args:
            country: The name of the country to select.
        """
        self.address_bar_button_locator().click()
        self.page.wait_for_selector(WoltLocators.COUNTRY_SELECT)
        self.page.select_option(WoltLocators.COUNTRY_SELECT, label=country)

    def choose_stree_in_address_popup(self, street: str ):
        """
        Fills in the street address and selects a suggestion from the dropdown.
        Args:
            street: The street address to enter.
            """
        self.page.wait_for_selector(WoltLocators.STREET_INPUT)
        self.page.locator(WoltLocators.STREET_INPUT).clear()
        self.page.fill(WoltLocators.STREET_INPUT, street)
        self.page.locator(WoltLocators.STREET_SUGGESTIONS_LIST).locator("li").nth(0).click()

    def address_continue_button(self):
        """
        Returns the locator for the 'Continue' button in the address section.
        Returns:
            Locator: The locator for the 'Continue' button.
        """
        return self.page.locator(WoltLocators.ADDRESS_CONTINUE_BUTTON)

    def main_discovery_content(self):
        """
        Returns the locator for the main discovery content on the page.
        Returns:
            Locator: The locator for the main discovery content.
        """
        return self.page.locator(WoltLocators.MAIN_DISCOVERY_CONTENT)

    def choose_tab_by_name(self, name: str):
        """
        Clicks on a tab based on its name.
        Args:
            name: The name of the tab to select.
        """
        self.page.get_by_role("tab", name=name).click()

    def choose_product_line_category(self, category: str):
        """
        Open all product line category and selects a product.
         Args:
            category: The category name to select.
        """
        self.page.locator(WoltLocators.PRODUCTS_LINE_BUTTON).click()
        self.page.locator(WoltLocators.PRODUCT_LINE_CATEGORY.format(category=category)).click()

    def discovery_page_title(self):
        """
        Returns the locator for the discovery page title.
        Returns:
            Locator: The locator for the page title.
        """
        return self.page.locator(WoltLocators.DISCOVERY_PAGE_TITLE)

    def venue_content(self):
        """
        Returns the locator for the venue content list on the page.
        Returns:
            Locator: The locator for the venue content list.
        """
        return self.page.locator(WoltLocators.VENUE_CONTENT_LIST)

    def find_sort_filter(self):
        """
        Returns bool results for the filter button, if available.
        Returns:
            bool: True if the filter button found or False if not found.
        """
        try:
            if self.page.wait_for_selector(WoltLocators.SORT_FILTER_BUTTON, timeout=5000):
                return True
        except Exception:
            logging.warning(f"Cannot find the filter, maybe next time...")
            return False

    def sorted_filter_by_recommended(self, filters: list):
        """
        Clicks the sort/filter button and applies the specified filters.
        Args:
            filters (list): List of filters to apply.
        """
        self.page.locator(WoltLocators.SORT_FILTER_BUTTON).click()
        for filter in filters:
            logging.info(f'Choosing filter: {filter}')
            self.page.locator(filter).scroll_into_view_if_needed()
            self.page.locator(filter).click()
        self.page.locator(WoltLocators.FILTER_APPLY_BUTTON).click()

    def click_first_venue_card(self):
        """
        Clicks on the first venue card on the page.
        """
        self.page.locator(WoltLocators.VENUE_CARD).nth(0).click()

    def click_first_available_item_card(self):
        """
        Clicks on the first available item card, skipping unavailable ones.
        """
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
        """
        Selects the first available option for each product in the order.
        """
        option_groups_list = self.page.locator(WoltLocators.PRODUCT_OPTIONS_GROUP).all()
        for option_group in option_groups_list:
            first_locator = option_group.locator(WoltLocators.CHECK_OPTION).nth(0)
            first_locator.wait_for(state="visible", timeout=5000)
            option_type = first_locator.get_attribute('type')
            if option_type == 'checkbox':
                first_locator.locator("..").click()

    def click_on_add_order(self):
        """
        Clicks the 'Submit Order' button to finalize and place the order.
        """
        self.page.locator(WoltLocators.PRODUCT_ORDER_SUBMIT).click()

    def click_card_view_button(self):
        """
        Clicks the 'Card View' button to view the order in the card layout.
        """
        self.page.locator(WoltLocators.CARD_VIEW_BUTTON).click()

    def click_card_total_price_button(self):
        """
        Clicks the button that shows the total price of the items in the card.
        """
        self.page.locator(WoltLocators.CARD_TOTAL_PRICE_BUTTON).click()
