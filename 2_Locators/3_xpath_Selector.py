from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try:
    driver.get('https://demoqa.com/elements')

    #ByXPath
    # driver.find_element(By.XPATH, "//li[contains(.,'NESTED XPATH')]").click()
    # # nested_path = driver.find_element(By.XPATH, "//header[@class='nested-header']//h1[1]")
    #
    # # Locate an element using XPath
    # element1 = driver.find_element(By.XPATH, "//h1")
    # print(element1.text)
    #
    # # Locate an input field by its name attribute
    # input_element = driver.find_element(By.XPATH, "//input[@name='username']")
    # input_element.send_keys("my_username")
    #
    # # Locate an element containing specific text
    # button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    # button.click()
    #
    # # Locate a child element
    # parent_element = driver.find_element(By.XPATH, "//div[@id='parent']")
    # child_element = parent_element.find_element("./child::span")
    # print(child_element.text)
    #
    # # Locate an element based on multiple conditions
    # element = driver.find_element(By.XPATH,"//input[@type='text' and @name='email']")
    # element.send_keys("example@example.com")
    #
    # # Using the following axis to find the next sibling
    # sibling_element =driver.find_element(By.XPATH,"//h2/following-sibling::p[1]")
    # print(sibling_element.text)
    #
    # # nested_path = driver.find_element(By.XPATH, "//p[text()='Child A']/ul/li/p")
    # # print(nested_path.text)


    driver.find_element(By.XPATH, "(//div[contains(@class,'header-right')])[1]").click()
    driver.find_element(By.XPATH, "(//li[@id='item-0'])[1]").click()
    driver.find_element((By.XPATH, "//h1[normalize-space()='Text Box']"))


finally:
    driver.quit()