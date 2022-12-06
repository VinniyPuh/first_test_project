# import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAmazonCart:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.amazon.com/")


    def test_empty_cart(self):
        # check '.click()'
        cart = self.driver.find_element(By.ID, 'nav-cart')
        cart.click()

        actual_txt = self.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']//h2").text
        expected_text = f'Your Amazon Cart is empty'

        assert expected_text == actual_txt, f"Error. Expected text: '{expected_text}', but actual text: '{actual_txt}'"


    def teardown_method(self):
        self.driver.quit()
