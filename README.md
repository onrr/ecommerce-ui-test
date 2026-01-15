# ECommerce UI Test Automation with Selenium

---

## Project Description
This project is a **UI End-toEnd test automation** project.

It tests an **[ECommerce Web Application](https://github.com/onrr/ecommerce-mvc)** from the user points of view.
The tests are written with **Python + Selenium WebDriver**.

This project only contains **UI test automation code**.

---

## What is tested?

This project tests a **real user scenario**:

1. User goes to the homepage
2. User clicks the Sign Up Button
3. User fiils in the Sign Up form and registers
4. User direct to the Login page and writes their email and password to log in 
5. User searches a product  
6. User adds the product to the cart  
7. User can increases product amount  
8. User direct to checkout page
9. User fiils in the form on the checkout page and completes the order

These steps are tested using **real browser actions**.

---

## Test Type

- UI Test  
- End-to-End (E2E) Test  
- Functional Test  

The test checks if the main features of the ecommerce application work correctly.

---

## Technologies Used

- Python  
- Selenium WebDriver  
- Firefox (gecko) WebDriver  

---

## How to Run the Test

1. First, clone the ***ecommerce application*** and run it locally:
- Check the [repository]((https://github.com/onrr/ecommerce-mvc)) for project details.
```bash
git clone https://github.com/onrr/ecommerce-mvc
cd ecommerce-mvc
dotnet restore
dotnet build
dotnet run
```
- Make sure the application is running on http://localhost:5102

2. Make sure Python, Selenium, Firefox and [geckodriver](https://github.com/mozilla/geckodriver/releases) are installed on your system

3. Clone this project:

```bash
git clone https://github.com/onrr/ecommerce-ui-test
cd ecommerce-ui-test
```

4. Run

```bash
python main.py
```