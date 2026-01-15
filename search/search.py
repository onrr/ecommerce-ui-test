from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Search:
    def __init__(self, driver):
        self.driver = driver

    # Fill in the search form and submit
    def search_form(self, search_query):
        search_form = self.driver.find_element(By.CSS_SELECTOR, "form[role='search']")
        search_form.find_element(By.NAME, "q").send_keys(search_query)
        search_button = search_form.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()

        WebDriverWait(self.driver, 5).until(
            EC.url_contains("/Products/ProductsByBrand?q")
        )
    
    def has_results(self):
        return len(self.driver.find_elements(By.ID, "search-result")) > 0