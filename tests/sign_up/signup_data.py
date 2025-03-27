from locators.wolt_locators import WoltLocators

signup_test_data = [
    {
        "case": "Google",
        "partner": WoltLocators.GOOGLE_SIGNUP_BUTTON,
        "element_to_check": WoltLocators.GOOGLE,
        "popup": False
     },
    {
        "case": "Apple",
        "partner": WoltLocators.APPLE_SIGNUP_BUTTON,
        "element_to_check": WoltLocators.APPLE,
        "popup": True
    },
    {
        "case": "Facebook",
        "partner": WoltLocators.FACEBOOK_SIGNUP_BUTTON  ,
        "element_to_check": WoltLocators.FACEBOOK,
        "popup": True
    }
]