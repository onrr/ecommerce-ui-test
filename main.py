from selenium import webdriver
from selenium.webdriver.common.by import By
from login.login import Login
from register.register import Register
from search.search import Search
from cart.cart import Cart
from checkout.checkout import Checkout

# Set up the WebDriver (using Firefox in this case)
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

# Go to homepage
driver.get("http://localhost:5102")
driver.find_element(By.CSS_SELECTOR, "a[href='/Account/SignUp']").click()

# Create an instance of the Register class and perform registration
register_page = Register(driver)
#register_page.go_to_register_page()
register_page.register_form("John", "Doe", "john.doe@example.com", "password123", "password123")
assert "/Account/SignIn" in driver.current_url, "Registration failed!"

# Create an instance of the Login class and perform login
login_page = Login(driver)
#login_page.go_to_login_page()
login_page.login_form("john.doe@example.com", "password123")
assert "/" in driver.current_url, "Login failed!"

# Search for a product
search_box = Search(driver)
search_box.search_form("Q45")
assert search_box.has_results(), "Search failed!"

# Cart actions
cart = Cart(driver)
cart.add_to_cart()
cart.item_amount(3)
assert "/Order/Checkout" in driver.current_url, "Checkout failed!"

# Checkout and complete order
checkout = Checkout(driver)
checkout.checkout_form("John", "Doe", "New York", "10001", "123 Main St", "1234567890")

# Check if order is completed
assert "/Order/Completed" in driver.current_url, "Order was not completed!"

print("Test completed successfully!")