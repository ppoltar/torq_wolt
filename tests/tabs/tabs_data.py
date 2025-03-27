from locators.wolt_locators import WoltLocators


tabs_test_data = [
    {
        "case": "Discovery Tab",
        "tab": "Discovery",
        "expected_element": WoltLocators.PRODUCTS_LINE
     },
    {
        "case": "Restaurants Tab",
        "tab": "Restaurants",
        "expected_element": WoltLocators.RESTAURANTS_NEAR_ME_TEXT
    },
    {
        "case": "Stores Tab",
        "tab": "Stores",
        "expected_element": WoltLocators.STORES_NEAR_ME_TEXT
    },



]