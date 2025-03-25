from playwright.sync_api import Page
from locators.wolt_locators import WoltLocators

class DiscoveryPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_discovery_page(self):
        self.page.goto(WoltLocators.DISCOVERY_URL)