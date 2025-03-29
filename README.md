# Torq Automation Developer Assignment 

Wolt discovery Web Page.

## Overview

This repository contains the automation test suite for **Wolt** discovery site using **Playwright** and **pytest** in Python. The tests are designed to verify the UI flow and functionalities of the **Wolt** web application. The tests utilize **pytest-xdist** for parallel execution, **pytest-html** for detailed HTML reports, and **Allure** for advanced reports with integrated screenshots and videos for failed tests.

## Features
- **UI Automation**: Verifies all major user flows in the application, including searching, sorting, and adding items to the order.
- **Parallel Test Execution**: Uses `pytest-xdist` for running tests in parallel to speed up the testing process.
- **Allure Reports**: Generates detailed Allure reports with embedded screenshots and videos on test failures.
- **Logging and Tracing**: Collects detailed logs and execution traces for better debugging and traceability.

## Requirements

- **Python 3.9+**
- **Playwright** 
- **pytest** 
- **pytest-playwright** 
- **pytest-xdist** 
- **pytest-html** 
- **allure-pytest** 


## Setup

### 1. Install Dependencies
To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```

### 2. Install Playwright browsers
```bash
python -m playwright install
```

### 3. Run Tests
```bash
pytest -v
```

## Test Structure

The project is organized into different directories and files that follow a logical structure for ease of navigation and maintenance. Below is the description of each directory and file.

```bash
.
├── locators/
│   ├── wolt_locators.py 
├── pages/
│   ├── discovery_page.py     
├── tests/
│   ├── address_bar/
│   ├── availability/
│   ├── e2e/
│   ├── log_in/  
│   ├── product_line/
│   ├── sign_up/ 
│   ├── tabs/             
├── conftest.py               
├── pytest.ini                
└── requirements.txt          
```

### Directory Layout

- **`locators/`**:  
  Stores the locators for UI elements used across multiple pages or components. It allows centralized management of locators so that they can be reused throughout the test suite. Locators are defined in classes and can be imported wherever needed.

- **`pages/`**:  
  Implements the **Page Object Model (POM)** pattern. Each file in this directory corresponds to a page or a component of the application. It contains methods that interact with the elements on the page (e.g., `discovery_page.py`). This structure helps to abstract away the details of how the elements are located and interacted with, which makes the tests more maintainable and scalable.

- **`tests/`**:  
  Contains the test cases organized by functionality or page. Each test file corresponds to a feature or a page in the application. For example, you may have a `test_e2e.py` for testing the E2E flow, or `test_availability.py` for testing that product a live.

- **`conftest.py`**:  
  Includes **pytest fixtures** and global configurations. This file is used to define any setup or teardown steps needed across multiple test files. Fixtures might include setting up browser instances, logging configurations, or test data. It's also a place for global settings related to pytest (e.g., hooks, logging configuration).

- **`pytest.ini`**:  
  The pytest configuration file that includes test-related settings like logging levels, test discovery rules, and configuration of pytest plugins like `pytest-playwright`, `pytest-xdist`, etc. The settings here help control the behavior of pytest when running the tests.

# Test Suite Overview

The suite covers a range of tests to ensure the robustness and usability of the discovery page.

### 1. **Availability Test**
   - **Purpose**: Ensures that key elements are visible and functional on the discovery page.
   - **Steps**: 
     - Verifies visibility and functionality of the discovery content main page.
   - **Expected Results**: All key elements must be visible and interactable.
   - **Use Case**: Basic availability check of core UI elements and the liveness of the page.

### 2. **Login Test**
   - **Purpose**: Simulates the login process by entering an email and navigating through the login flow.
   - **Steps**:
     - Clicks the login button, enters an email, and proceeds with the "Next" step.
     - Verifies that the "Resend Mail" login button is visible and enabled.
   - **Expected Results**: The "Resend Mail" button should be visible and enabled after clicking "Next".
   - **Use Case**: Verifies login functionality.

### 3. **Product Line Test**
   - **Purpose**: Ensures that selecting a product line category displays the correct title and venue content.
   - **Steps**:
     - Selects a product line category.
     - Verifies that the correct title for the selected category appears and the venue content is visible.
   - **Expected Results**: The title and venue content should match the selected category.
   - **Use Case**: Verifies product line category selection and content visibility.

### 4. **E2E Test**
   - **Purpose**: Verifies the full user journey from searching for an item to placing an order.
   - **Steps**:
     - Search for an item, apply filters, select a venue and item, and proceed to order.
     - Verifies that the price button is clickable and the search mail text field is editable.
   - **Expected Results**: The entire flow should function correctly, with the price button and mail text field being editable.
   - **Use Case**: E2E flow test from search to order confirmation.

### 5. **Sign-Up Test**
   - **Purpose**: Validates the sign-up process and ensures the correct page or popup appears when a sign-up partner is selected.
   - **Steps**:
     - Clicks the sign-up button, chooses a partner, and verifies that the partner's page or popup opens as expected.
   - **Expected Results**: The appropriate partner page or popup should be displayed.
   - **Use Case**: Verifies sign-up functionality and partner selection.

### 6. **Address Bar Test**
   - **Purpose**: Verifies that the address bar is visible and functional, allowing users to select countries and streets.
   - **Steps**:
     - Selects a country and a street from the address bar and ensures the "Continue" button is correctly enabled/disabled.
   - **Expected Results**: The address bar should be fully functional, enabling the user to select country and street options.
   - **Use Case**: Verifies the functionality of the address bar component.

### 7. **Tabs Test**
   - **Purpose**: Ensures that switching between tabs on the discovery page works as expected and displays the correct content.
   - **Steps**:
     - Clicks on a tab and verifies that the expected content associated with that tab is visible.
   - **Expected Results**: The correct content should be displayed when switching between tabs.
   - **Use Case**: Verifies tab functionality and content switching.

### 8. **Stress Test (High Load Availability Test)**
   - **Purpose**: Stress tests the availability of core elements on the discovery page by running the availability test repeatedly to simulate heavy load.
   - **Steps**:
     - Runs the availability test for a large number of iterations (e.g., 1000+ times) to simulate high traffic and ensure the stability of the discovery page under stress.
   - **Expected Results**: The discovery page should remain stable, and all core elements should remain functional under high load.
   - **Use Case**: Verifies the system's stability and resilience under heavy usage.

## Reports and Logs

Report and Logs created automatically in run directory in folder with prefix <reports/>

### 1. Allure report
Allure files created automatically in reports/allure-results, 
Allure report generated automatically in reports/allure-report include index.html file.

You can generate the report by yourself with command:
```bash
allure generate reports/allure-results --clean -o reports/allure-report
```

In the test execution process, if a test fails, Allure will attach the following to the report:

- **Video Recording**
Each test is recorded, and the videos are saved in the reports/videos/ directory. The video is automatically attached to the Allure report if the test fails.

- **Screenshot**
If a test fails, a screenshot is automatically taken and stored in reports/screenshots/. It is then attached to the Allure report for further analysis.


### 2. Trace Files
Playwright captures trace files of each test execution. Trace files contain detailed information on every action performed during a test, including network requests, DOM states, and screenshots.

These trace files are saved in the reports/playwright-traces/ directory. If you encounter a failure, you can inspect the trace file for more detailed insights.

Viewing trace file is generated, you can view it using the Playwright Trace Viewer. 

You can run the following command to open the trace viewer:
```bash
playwright show-trace reports/playwright-traces/{test_name}-trace.zip
```


### 3. HTML Report
The HTML report is generated automatically using configuration in pytest.ini file.

You can open the generated HTML report directly in any browser by navigating to - **reports/report.html.**