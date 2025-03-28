from locators.wolt_locators import WoltLocators

e2e_test_data = [
    {
        "case": "E2E Test hummus",
        "search_text": "hummus",
        "filters": [
            WoltLocators.SORTED_OPTION_RESTAURANT,
            WoltLocators.SORTED_CATEGORIES_ARABIC,
        ],
     },

    {
        "case": "E2E Test asian",
        "search_text": "asian",
        "filters": [
            WoltLocators.SORTED_OPTION_GROCERY
        ],
    },

    {
        "case": "E2E Test burger",
        "search_text": "burger",
        "filters": [
            WoltLocators.SORTED_CATEGORIES_AMERICAN
        ],
    },
]