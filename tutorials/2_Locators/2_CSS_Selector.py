from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
# driver.maximize_window()


try:
    driver.get('https://www.facebook.com/')

    # By CSS Selector
    driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys("pratham1659")

    #Using ID : tagName#valueOfID
    # element_btn = driver.find_element(By.CSS_SELECTOR, "button#u_0_5_kJ")

    #Using Class : tagName.valueOfClass
    # element_btn = driver.find_element(By.CSS_SELECTOR, "button._42ft._4jy0")

    #Using attribute : tagName[attribute=value]
    # element_btn = driver.find_element(By.CSS_SELECTOR, "button[name='login']")
    # element_btn = driver.find_element(By.CSS_SELECTOR, " button[type = 'submit']")

    #Using class Attribute : tagName.valueOfClass[attribute=value]
    element_btn = driver.find_element(By.CSS_SELECTOR, "button._42ft._4jy0[data-testid=royal_login_button]")
    print(f'By CSS Selector: {element_btn.text}')


finally:
    driver.quit()
