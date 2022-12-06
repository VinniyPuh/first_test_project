# import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestAmazonTDB:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.amazon.com/")

    # count elements
    # len() - leigh(count)
    def test_count_sections(self):
        clk1 = self.driver.find_element(By.XPATH, "//div[@id='nav-xshop']/a[contains(@href, 'nav_cs_gb')]")
        # IDK. It`s just not working without command below
        self.driver.execute_script("arguments[0].click();", clk1)
        # 'elementS' - not 'elemenT'
        actual_links = self.driver.find_elements(By.XPATH, "//div[@id='nav-subnav']//a")

        assert len(actual_links) == 6, f"Expected to see 6 links, but actual links: '{len(actual_links)}'"

    def teardown_method(self):
        self.driver.quit()


