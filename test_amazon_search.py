import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Create class to simplify and shortify code
# Use 'self.' to drivers can work in different def`s(need to use 'self' in def`s)
class TestAmazon:
    # driver - allow to separate 'driver' functions to def`s
    search_words = ('auto', 'guitar', 'toyota')
    driver = ''
    # Put here necessary setup for every test
    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.amazon.com/")

    # Allows input need parameters, without copy whole function
    @pytest.mark.parametrize('search_query', search_words)
    def test_amazon_search_auto(self, search_query):
        search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys(search_query, Keys.ENTER)

        # f'\"' - allows check '"auto"' query, not a 'auto'
        expected_text = f'\"{search_query}\"'
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
        assert expected_text == actual_text, f'Error. Expected text: {expected_text}, but actual text: {actual_text}'

    def teardown_method(self):
        self.driver.quit()

