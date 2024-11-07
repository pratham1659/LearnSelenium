import time

from selenium.webdriver.common.by import By

class HomePageCarters:
    # Define locators as tuples
    homePage_Inventory_hyperlink = (By.XPATH, "//span[text()='Inventory Smart']/preceding-sibling::button")
    homePage_getStarted_button = (By.XPATH, "(//button[@type='button'][normalize-space()='Get Started'])[2]")
    dd_title = (By.XPATH, "//*[text()='Decision Dashboard']")
    expand_icon_cs = (By.XPATH, "//div[@id='showmore-button']")

    def __init__(self, driver):
        self.driver=driver

    def home_page_inventory_smart_selection(self):
        try:
            time.sleep(3)
            self.driver.find_element(*self.homePage_Inventory_hyperlink).click()
            print("Inventory Tab Selected.")
        except Exception as e:
            print(f"Error during home screen: {str(e)}")

    def home_page_get_started(self):
        try:
            time.sleep(3)
            self.driver.find_element(*self.homePage_getStarted_button).click()
            print("Get Started Button clicked")
        except Exception as e:
            print(f"Error during home screen: {str(e)}")

    def get_decision_dashboard_text(self):
        """Get the text from the Decision Dashboard"""
        try:
            decision_text = self.driver.find_element(*self.dd_title).text
            return decision_text
        except Exception as e:
            print(f"Error retrieving decision dashboard text: {str(e)}")
            return None


