from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def test_login_success():
    driver = setup_driver()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    assert "inventory" in driver.current_url
    print("✅ Test 1 (Valid login): PASSED")
    driver.quit()

def test_login_failure():
    driver = setup_driver()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)
    error_msg = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert "Epic sadface" in error_msg.text
    print("✅ Test 2 (Invalid login): PASSED")
    driver.quit()


if __name__ == "__main__":
    test_login_success()
    test_login_failure()
