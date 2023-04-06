from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Test_1:
    def empty(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        userNameInput = driver.find_element(By.ID, "user-name").send_keys("")
        passwordInput = driver.find_element(By.ID, "password").send_keys("")
        loginBtn = driver.find_element(By.ID, "login-button").click()

        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Result: {testResult}")

    def empty_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        userNameInput = driver.find_element(By.ID, "user-name").send_keys("polatalemdar01")
        passwordInput = driver.find_element(By.ID, "password").send_keys("")
        loginBtn = driver.find_element(By.ID, "login-button").click()

        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Result: {testResult}")

    def locked_user(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        userNameInput = driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        passwordInput = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID, "login-button").click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Result: {testResult}")

    def x_close_button(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        userNameInput = driver.find_element(By.ID, "user-name").send_keys("")
        passwordInput = driver.find_element(By.ID, "password").send_keys("")
        loginBtn = driver.find_element(By.ID, "login-button").click()
        sleep(2)
        closeErrorBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button").click()
        sleep(2)

    def routing(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        userNameInput = driver.find_element(By.ID, "user-name").send_keys("standard_user")
        passwordInput = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID, "login-button").click()

        urlAvailability = driver.current_url == "https://www.saucedemo.com/inventory.html"
        print(f"Test Result: {urlAvailability}")

    def products_list(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        userNameInput = driver.find_element(By.ID, "user-name").send_keys("standard_user")
        passwordInput = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID, "login-button").click()
        inventoryList = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"{len(inventoryList)}")
        if len(inventoryList) == 6:
            print(f"The number of products shown to the user is {len(inventoryList)}, \nTest Result: True")
        else:
            print("Test Result: False")

testClass = Test_1()
testClass.empty()
testClass.empty_password()
testClass.locked_user()
#testClass.x_close_button()
testClass.routing()
testClass.products_list()