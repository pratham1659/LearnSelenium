import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utilities import readProperties

# Define Chrome options to handle SSL and other configurations
chrome_options = Options()

# Disable SSL certificate verification
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--incognito")  # Optionally run in incognito mode

# Define the fixture for setting up and tearing down the WebDriver
@pytest.fixture()
def setup_and_teardown(request):
    # Read the browser type from configuration
    browser = readProperties.read_configuration("basic_info", "browser")

    # Initialize the driver based on the browser choice
    if browser == "chrome":
        # Set Chrome options when initializing the Chrome WebDriver
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox()  # Add Firefox options if necessary
    else:
        raise ValueError("Unsupported browser type")

    # Maximize window and set implicit wait
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Open the URL from the configuration
    web_url = readProperties.read_configuration("basic_info", "baseUrl")
    driver.get(web_url)

    # Yield the driver to the test
    yield driver

    # Teardown: Quit the driver after the test completes
    driver.quit()

