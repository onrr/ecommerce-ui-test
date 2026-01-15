from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.driver = driver
    
    # Navigate to the login page
    def go_to_login_page(self):
        self.driver.get("http://localhost:5102/Account/SignIn")

    # Fill in the login form and submit
    def login_form(self, email, password):
        login_form = self.driver.find_element(By.CLASS_NAME, "form-group")
        login_form.find_element(By.ID, "Email").send_keys(email)
        login_form.find_element(By.ID, "Password").send_keys(password)
        login_button = login_form.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()