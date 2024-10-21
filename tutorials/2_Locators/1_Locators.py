from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless
# driver.maximize_window()

driver = webdriver.Chrome(options=chrome_options)


try:
    driver.get('https://selenium-test-react.vercel.app/')

    # # By ID
    # element_id = driver.find_element(By.ID, 'element_id')
    # print(f'By ID: {element_id.text}')
    #
    # # By Name
    # element_name = driver.find_element(By.NAME, 'element_name')
    # print(f'By Name: {element_name.text}')
    #
    # # By Class Name
    # elements_class = driver.find_elements(By.CLASS_NAME, 'class_name')
    # print('By Class Name:')
    # for elem in elements_class:
    #     print(elem.text)
    #
    # # By Tag Name
    # elements_tag = driver.find_elements(By.TAG_NAME, 'p')
    # print('By Tag Name:')
    # for elem in elements_tag:
    #     print(elem.text)
    #
    # # By Link Text
    # element_link = driver.find_element(By.LINK_TEXT, 'Click Here')
    # print(f'By Link Text: {element_link.get_attribute("href")}')
    #
    # # By Partial Link Text
    # element_partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Click')
    # print(f'By Partial Link Text: {element_partial_link.get_attribute("href")}')
    #

    driver.find_element(By.LINK_TEXT, "HOMEPAGE").click()
    count_elements = driver.find_elements(By.TAG_NAME, "li")

    # Print the count of <li> elements
    print(f'Total <li> elements found: {len(count_elements)}') #format print is used here

    # Print the text of each <li> element
    for index, element in enumerate(count_elements):
        print(f'{index + 1}: {element.text}')

finally:
    driver.quit()