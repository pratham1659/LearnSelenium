import time
import pytest
from selenium import webdriver
from pageObjects.CARTERS.HomePageCarters import HomePageCarters
from pageObjects.CARTERS.LoginScreen import LoginScreen
from utilities.readProperties import ReadConfig
from utilities import takeScreenshots
from utilities.customLogger import LogGenerator


class TestLogin:
    # Fetching credentials from the configuration
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()

    # Initialize logger for the test class
    log = LogGenerator.save_log("Starting the Test Suite")

    def test_homepage_title(self, setup_and_teardown):
        self.log.info("Verifying HomePage Title...")
        self.driver = setup_and_teardown
        act_title = self.driver.title
        if act_title == "[TEST] IA Smart Platform" or act_title == "Impact Smart":
            self.log.info("HomePage title verified successfully.")
            assert True
        else:
            self.log.error("HomePage title verification failed!")
            takeScreenshots.capture_screenshot(self.driver, "homepage_title_failure")
            assert False


    def test_login(self, setup_and_teardown):
        self.log.info("Filling in login form...")
        self.driver = setup_and_teardown
        self.lp = LoginScreen(self.driver)
        self.lp.login(self.username, self.password)
        time.sleep(3)
        act_title = self.driver.title
        if act_title == "[TEST] IA Smart Platform" or act_title == "Impact Smart":
            self.log.info("Title verified successfully.")
            assert True
        else:
            self.log.error("Title verification failed!")
            takeScreenshots.capture_screenshot(self.driver, "login_title_failure")
            assert False


    def test_home_page(self, setup_and_teardown):
        self.log.info("Navigating to home page...")
        self.driver = setup_and_teardown
        self.lp = LoginScreen(self.driver)
        self.lp.login(self.username, self.password)
        self.hm = HomePageCarters(self.driver)
        time.sleep(3)
        decision_text = self.hm.get_decision_dashboard_text()
        if decision_text == "Decision Dashboard":
            self.log.info("Successfully verified the home page content.")
            assert True
        else:
            self.log.error("Home page verification failed!")
            takeScreenshots.capture_screenshot(self.driver, "home_page_failure")
            assert False
