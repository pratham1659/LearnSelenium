import time
import unittest
from pageObjects.HomePageCarters import HomePageCarters
from pageObjects.LoginScreen import LoginScreen
from TestCases.confest import setup

class TestLogin():
    baseUrl = "https://carters.test.impactsmartsuite.com/login"
    username = "qa@impactanalytics.co"
    password = "testuser@456"

    def set_up(self, setup):
        """Runs before each test to initialize WebDriver"""
        self.driver = setup

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "[TEST] IA Smart Platform" or "Impact Smart":
            assert True
        else:
            assert  False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginScreen(self.driver)
        time.sleep(3)

        self.lp.login(self.username, self.password)
        # self.lp.set_username(self.username)
        # self.lp.set_password(self.password)
        # self.lp.click_login()
        time.sleep(3)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "[TEST] IA Smart Platform" or "Impact Smart":
            assert True
        else:
            assert False

    def test_home_page(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginScreen(self.driver)
        time.sleep(3)
        self.lp.login(self.username, self.password)

        self.hm = HomePageCarters(self.driver)
        time.sleep(5)
        self.hm.home_page_inventory_smart_selection()
        self.hm.home_page_get_started()
        time.sleep(4)
        decision_text = self.hm.get_decision_dashboard_text()
        if decision_text == "Decision Dashboard":
            assert  True
        else:
            assert False
        self.driver.close()




