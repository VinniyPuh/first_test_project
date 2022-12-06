
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# common - module for using elements searching/using(searching by id,press the buttons(e.g 'TAB', etc.)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.imp... - give time to find elements, for defence by errors(when need time to find elements)
driver.implicitly_wait(5)
# driver.get('testing_site_adress') - open page requirement site
# Necessary use 'https://'
driver.get("https://www.amazon.com/")
# Search 'searchbar' by 'id', write the text and imitate press 'enter' button
search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys('auto', Keys.ENTER)

# If there is mistake(site show not right text),python show error with text
# txt that should be
expected_text = '"auto"'
# txt that actually is
actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

# error text
assert expected_text == actual_text, f'Error. Expected text: {expected_text}, but actual text: {actual_text}'

# if no there is errors, browser just close
driver.quit()