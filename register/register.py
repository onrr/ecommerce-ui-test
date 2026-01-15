from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Register:
    def __init__(self, driver):
        self.driver = driver
    
    # Navigate to the register page
    def go_to_register_page(self):
        self.driver.get("http://localhost:5102/Account/SignUp")

    # Fill in the register form and submit
    def register_form(self, name, surname, email, password, confirm_password):
        register_form = self.driver.find_element(By.CLASS_NAME, "form-group")
        register_form.find_element(By.ID, "Name").send_keys(name)
        register_form.find_element(By.ID, "Surname").send_keys(surname)
        register_form.find_element(By.ID, "Email").send_keys(email)
        register_form.find_element(By.ID, "Password").send_keys(password)
        register_form.find_element(By.ID, "ConfirmPassword").send_keys(confirm_password)
        register_button = register_form.find_element(By.CSS_SELECTOR, "button[type='submit']")
        register_button.click()

        WebDriverWait(self.driver, 5).until(
            EC.url_contains("/Account/SignIn")
        )