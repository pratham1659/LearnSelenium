from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get('https://selenium-test-react.vercel.app/')

    # xpath axes - preceding
    driver.find_element(By.XPATH, "//a[text()='CALCULATOR']/preceding::li/a[text()='FAMILY TREE']").click()

    verify_page = driver.find_element(By.XPATH, "//h1[text()='Family Tree for Xpath Testing']").text
    print(verify_page)

    # verify_childTag = driver.find_element(By.XPATH, "//*[attribute='value']/child::tagname").text
    # print(verify_childTag)

    # verify_parentTag = driver.find_element(By.XPATH, "//*[attribute='value']/parent::tagname").text
    # print(verify_parentTag)

    verify_following = driver.find_element(By.XPATH, "//div[text()='Child 1']/following::div[5]").text
    print(verify_following)

    verify_following_sibling = driver.find_element(By.XPATH, "//div[text()='Child 1']/following-sibling::div[3]").text
    print(verify_following_sibling)

    verif_preceding = driver.find_element(By.XPATH, "//div[text()='Child 1']/preceding::div[1]").text
    print(verif_preceding)

    verify_preceding_sibling = driver.find_element(By.XPATH, "//div[text()='Child 4']/preceding-sibling::div[3]").text
    print(verify_preceding_sibling)

    # verify_ancestor = driver.find_element(By.XPATH, "//div[text()='Grandchild 4']/ancestor::div").text
    # print(verify_ancestor)

    # verify_descendant =  driver.find_element(By.XPATH, "//div[text()='Grandchild 4']/descendant::div").text
    # print(verify_descendant)

    driver.find_element(By.XPATH, "//a[text()='TABLES']").click()

finally:
    driver.quit()



