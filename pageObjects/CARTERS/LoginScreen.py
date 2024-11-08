from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginScreen:
    username_Input = (By.XPATH, "//input[@id='loginInputEmail']")
    password_Input = (By.XPATH, "//input[@id='loginPassword']")
    signin_Button = (By.ID, "btnLogin")

    def __init__(self, driver):
        self.driver = driver

    def set_up(self):
        try:
            # Ensure the driver is set correctly
            if not self.driver:
                raise ValueError("Driver is not initialized properly.")
            print("Driver setup successful.")
        except Exception as e:
            print(f"Error in setUp: {str(e)}")

    def set_username(self, username):
        try:
            # Correctly unpack the tuple and find the element
            self.driver.find_element(*self.username_Input).send_keys(username)
        except Exception as e:
            print(f"Error in set_username: {str(e)}")
            raise

    def set_password(self, password):
        try:
            self.driver.find_element(*self.password_Input).send_keys(password)
        except Exception as e:
            print(f"Error in set_password: {str(e)}")
            raise

    def click_login(self):
        try:
            self.driver.find_element(*self.signin_Button).click()
        except Exception as e:
            print(f"Error in click_login: {str(e)}")
            raise


    def login(self, username, password):
        try:
            self.driver.find_element(*self.username_Input).send_keys(username)
            self.driver.find_element(*self.password_Input).send_keys(password)
            self.driver.find_element(*self.signin_Button).click()
        except Exception as e:
            print(f"Error in login: {str(e)}")
            raise