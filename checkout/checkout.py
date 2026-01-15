from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout:
    def __init__(self, driver):
        self.driver = driver

    # Fill in the checkout form and complete order
    def checkout_form(self, name, surname, city, zipcode, address, phonenumber):
        checkout_form = self.driver.find_element(By.ID, "checkout-form")
        checkout_form.find_element(By.ID, "Name").send_keys(name)
        checkout_form.find_element(By.ID, "Surname").send_keys(surname)
        checkout_form.find_element(By.ID, "City").send_keys(city)
        checkout_form.find_element(By.ID, "ZipCode").send_keys(zipcode)
        checkout_form.find_element(By.ID, "Address").send_keys(address)
        checkout_form.find_element(By.ID, "PhoneNumber").send_keys(phonenumber)
        register_button = checkout_form.find_element(By.CSS_SELECTOR, "button[type='submit']")
        register_button.click()

        WebDriverWait(self.driver, 5).until(
            EC.url_contains("/Order/Completed")
        )