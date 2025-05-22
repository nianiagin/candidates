import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

def test_user_one(driver):
    driver.get("https://www.saucedemo.com/")
    username = "standard_user"
    password = "secret_sauce"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()
    assert driver.find_element(By.ID, "login-button"), "Ошибка, вероятно пользователь не зашёл/не вышел"

def test_user_two(driver):
    driver.get("https://www.saucedemo.com/")
    username = "locked_out_user"
    password = "secret_sauce"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()
    assert driver.find_element(By.ID, "login-button"), "Ошибка, вероятно пользователь не зашёл/не вышел"

def test_user_three(driver):
    driver.get("https://www.saucedemo.com/")
    username = "problem_user"
    password = "secret_sauce"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()
    assert driver.find_element(By.ID, "login-button"), "Ошибка, вероятно пользователь не зашёл/не вышел"

def test_user_four(driver):
    driver.get("https://www.saucedemo.com/")
    username = "performance_glitch_user"
    password = "secret_sauce"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()
    assert driver.find_element(By.ID, "login-button"), "Ошибка, вероятно пользователь не зашёл/не вышел"

def test_user_five(driver):
    driver.get("https://www.saucedemo.com/")
    username = "error_user"
    password = "secret_sauce"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()
    assert driver.find_element(By.ID, "login-button"), "Ошибка, вероятно пользователь не зашёл/не вышел"

def test_user_six(driver):
    driver.get("https://www.saucedemo.com/")
    username = "visual_user"
    password = "secret_sauce"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()
    assert driver.find_element(By.ID, "login-button"), "Ошибка, вероятно пользователь не зашёл/не вышел"

def test_unknown_user(driver):
    driver.get("https://www.saucedemo.com/")
    username = "213"
    password = "secret_sauce"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert driver.find_element(By.CSS_SELECTOR, ".error-message-container.error"), "Ошибка не появилась"

def test_incorrect_password(driver):
    driver.get("https://www.saucedemo.com/")
    username = "standard_user"
    password = "secret_sauce1"
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert driver.find_element(By.CSS_SELECTOR, ".error-message-container.error"), "Ошибка не появилась"

def auto_login(driver):
    username = "standard_user"
    password = "secret_sauce"
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def test_add_to_cart_one(driver):
    auto_login(driver)
    sauce_labs_backpack = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
    str_sauce_labs_backpack = sauce_labs_backpack.text
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    sauce_labs_backpack_in = driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
    str_sauce_labs_backpack_in = sauce_labs_backpack_in.text
    if str_sauce_labs_backpack == str_sauce_labs_backpack_in:
        print(str_sauce_labs_backpack)

def test_sort_By_high_to_low(driver):
    auto_login(driver)
    select_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
    dropdown = Select(select_element)
    dropdown.select_by_visible_text("Price (high to low)")
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = []
    for p in price_elements:
        price_value = float(p.text[1:])
        print(price_value)
        prices.append(price_value)
    assert prices == sorted(prices, reverse=True), "Цены не отсортированы по убыванию"

def test_sort_by_low_to_high(driver):
    auto_login(driver)
    select_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
    dropdown = Select(select_element)
    dropdown.select_by_visible_text("Price (low to high)")
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = []
    for p in price_elements:
        price_value = float(p.text[1:])
        print(price_value)
        prices.append(price_value)
    assert prices == sorted(prices), "Цены не отсортированы по возрастанию"

def test_send_to_basket(driver):
    auto_login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.is_displayed(), "Значок корзины не отображается"
    assert badge.text == "1", f"Ожидалось '1', но получено '{badge.text}'"

def test_bug_remove(driver):
    auto_login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "reset_sidebar_link").click()
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_link"), "Значок не обновился"
    assert driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack"), "Кнопка не вернулась в изначальное состояние"
    
def test_create_empty_order(driver):
    auto_login(driver)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item_label")
    assert len(cart_items) == 0, "Корзина должна быть пуста"
    
    checkout_button = driver.find_element(By.ID, "checkout")
    assert not checkout_button.is_enabled(), "Кнопка Checkout должна быть неактивна для пустой корзины"
