import time
from tkinter import Radiobutton

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # driver.get('https://demo.nopcommerce.com/register')


    # Applications Commands ------------------------------------------
    # driver.maximize_window()
    # print(driver.title)
    # print(driver.current_url)
    # print(driver.page_source)


    # Conditional Commands --------------------------------------------------
    # radio_button = driver.find_element(By.ID, "gender")
    # print(f'Radio Button displayed or not : {radio_button.is_displayed()}')
    #
    # selected = driver.find_element(By.XPATH, "//input[@id='Newsletter']")
    # print(f'Check Button Selected or not 1 : {selected.is_selected()}')
    # driver.find_element(By.XPATH, "//input[@id='Newsletter']").click()
    # print(f'Check Button Selected or not 2 : {selected.is_selected()}')
    #
    # enabled = driver.find_element(By.XPATH, "//input[@id='FirstName']")
    # print(f'Check Button Enabled or not : {enabled.is_enabled()}')

    # Browser Commands ----------------------------------------------------------
    # driver.close()
    # driver.quit()
    # time.sleep(5)

    # Navigation commands ----------------------------------------------------------
    # driver.get("https://www.amazon.in/")
    # driver.back()
    # print("Check Driver Title",driver.current_url)
    # driver.forward()
    # print("Check Driver Title",driver.current_url)
    # driver.refresh()

    #Text Extract Commands -----------------------------------------------------------
    #Locator Matching with single element
    # driver.get("https://selenium-test-react.vercel.app/tables")

    # table_name_single =  driver.find_element(By.XPATH, "//td[text()='John Doe']").text
    # print("Table_name: ", table_name_single)
    #
    # table_name_single2 = driver.find_element(By.XPATH, "//ul[@class='scrollableList']//a")
    # print(table_name_single2.text)

    #Locator Matching with multiple element
    # multiple_tb_name = driver.find_elements(By.XPATH, "//ul[@class='scrollableList']/li/a")
    # print("No. of Links: ", len(multiple_tb_name))
    # print(multiple_tb_name[1].text)

    # for ele in multiple_tb_name:
    #     print(ele.text)

    # get Attribute methods -------------------------------------------------------------------
    driver.get("https://selenium-test-react.vercel.app/loginportal")

    username = driver.find_element(By.NAME, "username")
    username.send_keys("Pratham")
    print("FirstName TEXT: ", username.text)
    print("FirstNAME GetAttribute: ",username.get_attribute('value')) # inner Text

    password = driver.find_element(By.NAME, "password")
    password.send_keys("pratham123")
    print("Password GetAttribute: ", password.get_attribute('value'))


finally:
    driver.quit()
