import time
from selenium import webdriver
from pageObjects.CARTERS.HomePageCarters import HomePageCarters
from pageObjects.CARTERS.LoginScreen import LoginScreen
from utilities import readProperties


class TestLogin:
    baseUrl = readProperties.read_configuration("basic_info", "baseUrl")
    username = readProperties.read_configuration("basic_info", "useremail")
    password = readProperties.read_configuration("basic_info", "password")

    def test_homepage_title(self, setup_and_teardown):
        self.driver = setup_and_teardown
        act_title = self.driver.title
        self.driver.close()
        assert act_title == "[TEST] IA Smart Platform" or act_title == "Impact Smart"

    def test_login(self, setup_and_teardown):
        self.driver = setup_and_teardown
        self.lp = LoginScreen(self.driver)
        time.sleep(3)
        self.lp.login(self.username, self.password)
        time.sleep(3)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "[TEST] IA Smart Platform" or "Impact Smart":
            assert True
        else:
            assert False

    def test_home_page(self, setup_and_teardown):
        failed_assertions = []
        self.driver = setup_and_teardown
        self.lp = LoginScreen(self.driver)
        time.sleep(3)
        self.lp.login(self.username, self.password)

        self.hm = HomePageCarters(self.driver)
        time.sleep(5)
        self.hm.home_page_inventory_smart_selection()
        self.hm.home_page_get_started()
        time.sleep(4)
        decision_text = self.hm.get_decision_dashboard_text()
        print(decision_text)

        try:
            decision_text = self.hm.get_decision_dashboard_text()
            assert decision_text == "Decision Dashboard"
        except AssertionError as e:
            failed_assertions.append(str(e))
        self.driver.close()




