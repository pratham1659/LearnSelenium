import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    driver.get('https://selenium-test-react.vercel.app/loginportal')

    driver.maximize_window()

    title = driver.title

    driver.find_element(By.NAME, "username").send_keys("admin123")
    driver.find_element(By.NAME, "password").send_keys("1234")
    driver.find_element(By.NAME, "rememberMe").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    expected_login = driver.find_element(By.XPATH,
                                         "//p[normalize-space(text())='You are now logged in.']").get_attribute

    login_text = "You are now logged in."
    if login_text == expected_login:
        print("Login Successfully")
    else:
        print("Something went wrong")
    # Hard wait: pause execution for 5 seconds
    time.sleep(5)

finally:
    driver.quit()
