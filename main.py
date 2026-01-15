from selenium import webdriver
from login.login import Login
from register.register import Register
from search.search import Search

# Set up the WebDriver (using Firefox in this case)
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

# Create an instance of the Register class and perform registration
register_page = Register(driver)
register_page.go_to_register_page()
register_page.register_form("John", "Doe", "john.doe@example.com", "password123", "password123")

# Create an instance of the Login class and perform login
login_page = Login(driver)
#login_page.go_to_login_page()
login_page.login_form("john.doe@example.com", "password123")

# Search for a product
search_box = Search(driver)
search_box.search_form("sony")
