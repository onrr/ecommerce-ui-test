from selenium import webdriver
from login.login import Login

# Set up the WebDriver (using Firefox in this case)
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

# Create an instance of the Login class and perform login
login_page = Login(driver)
login_page.land_first_page()
login_page.login_form("admin@admin.com", "12345678")