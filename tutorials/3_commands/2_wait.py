from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    driver.get('https://demo.nopcommerce.com/register')

    driver.find_element(By.XPATH,"")
finally:
    driver.quit()
