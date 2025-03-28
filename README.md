# torq_wolt
Torq Automation Developer Assignment


## Overview

This repository contains the automation test suite for **Wolt** discovery site using **Playwright** and **pytest** in Python. The tests are designed to verify the UI flow and functionalities of the **Torq Wolt** application. The tests utilize **pytest-xdist** for parallel execution, **pytest-html** for detailed HTML reports, and **Allure** for advanced reports with integrated screenshots and videos for failed tests.

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


Stress tests -  can run availability tests a lot of time (1000+) and config 
number of workers in ci/cd (Jenkins config with -n=1000)