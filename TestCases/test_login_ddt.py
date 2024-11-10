import time, os
import pytest
from pandas import read_excel
from selenium import webdriver
from pageObjects.CARTERS.HomePageCarters import HomePageCarters
from pageObjects.CARTERS.LoginScreen import LoginScreen
from utilities.readExcel import test_data_file
from utilities.readProperties import ReadConfig
from utilities import takeScreenshots
from utilities.customLogger import LogGenerator
from utilities import readExcel

class TestLoginDDT:

    # Fetching credentials from the configuration
    username = ReadConfig.get_useremail()
    password = ReadConfig.get_password()

    # Path to the test data file
    test_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "TestData", "login_data.xlsx")

    # Initialize logger for the test class
    log = LogGenerator.save_log("Starting the Test Suite using Excel")

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


    def test_login_ddt(self, setup_and_teardown):
        self.log.info("Filling in login form...")
        self.driver = setup_and_teardown
        self.lp = LoginScreen(self.driver)

        self.log.info("Test Data intialize for test_login_data")
        self.rows = readExcel.get_row_count(self.test_data_file, 'Sheet1')
        print("Number of Rows i in a Excel: ", self.rows)

        list_status=[]      #Emptylist variable

        for r in range(2, self.rows+1):
            self.username = readExcel.read_data(self.test_data_file, 'Sheet1', r, 1)
            self.password = readExcel.read_data(self.test_data_file, 'Sheet1', r, 2)
            self.expected = readExcel.read_data(self.test_data_file, 'Sheet1', r, 3)

            self.lp.login(self.username, self.password)
            time.sleep(3)

            act_title = self.driver.title
            if act_title == "[TEST] IA Smart Platform" or act_title == "Impact Smart":
                if self.expected == "pass":
                    self.log.info("-------------- Passed --------------")
                    list_status.append("Pass")
                elif self.expected=="fail":
                    self.log.info("-------------- Failed --------------")

                    list_status.append("Fail")

            elif act_title != "[TEST] IA Smart Platform" or act_title == "Impact Smart":
                if self.expected == "pass":
                    self.log.info("-------------- Failed --------------")
                    list_status.append("Fail")
                elif self.expected=="fail":
                    self.log.info("-------------- Passed --------------")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.log.info("-----------Login DDT test Passed -----------")
            self.driver.close()
            assert True
        else:
            self.log.info("-----------Login DDT test Failed -----------")
            self.driver.close()
            assert  False

        self.log.info("---------------End of Login DDT Test-----------")
        self.log.info("---------------Complete test_login_DDT---------")
            # takeScreenshots.capture_screenshot(self.driver, "login_title_failure")


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
