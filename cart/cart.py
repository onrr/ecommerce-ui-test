from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart:
    def __init__(self, driver):
        self.driver = driver
    
    # Add to Cart
    def add_to_cart(self):
        plusIcon = self.driver.find_element(By.CLASS_NAME, "fa-cart-plus")
        plusIcon.click()

        WebDriverWait(self.driver, 5).until(
            EC.url_contains("/Cart")
        )

    def item_amount(self, amount=1):

        if amount == 1:
            self.go_to_checkout()
        else:
            for _ in range(amount - 1):
                increase_button = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "fa-plus"))
                ) 
                increase_button.click()
            
            self.go_to_checkout()   
        

    def go_to_checkout(self):
        buy_now_button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/Order/Checkout']"))
        )
        buy_now_button.click()
        
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("/Order/Checkout")
        )