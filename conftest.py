import pytest
from selenium import webdriver
from utilities import ReadConfiguration


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfiguration.read_configuration("basic_info", "browser")
    driver = None

    try:
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "edge":
            driver = webdriver.Edge()
        else:
            raise ValueError("Provide a valid browser name from this list: chrome/firefox/edge")

        driver.maximize_window()
        web_url = ReadConfiguration.read_configuration("basic_info", "url")
        driver.get(web_url)
        request.cls.driver = driver
        yield
    finally:
        if driver is not None:
            driver.quit()