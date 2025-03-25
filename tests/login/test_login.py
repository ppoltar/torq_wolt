from pages.discovery_page import DiscoveryPage

def test_login(page):
    discovery_page = DiscoveryPage(page)
    discovery_page.go_to_discovery_page()
    discovery_page.click_login_button()

    pass