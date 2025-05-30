import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Firefox()
    browser.get("https://www.paulinecake.ae/ru")
    yield browser
    browser.quit()

def test_catalog(browser):
    wait = WebDriverWait(browser, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/order"]'))).click()
    time.sleep(3)
    assert browser.current_url.endswith("/ru/order"), "Не перешли в каталог для заказа"
    
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/fillings"]'))).click()
    time.sleep(2)
    assert browser.current_url.endswith("/ru/fillings"), "Не перешли в раздел начинок"

    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/custom-cakes"]'))).click()
    time.sleep(2)
    assert browser.current_url.endswith("/ru/custom-cakes"), "Не перешли в кастомные торты"

    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/login"]'))).click()
    time.sleep(2)
    assert browser.current_url.endswith("/ru/login"), "Не перешли на страницу входа"

    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru"]'))).click()
    time.sleep(2)
    assert browser.current_url.rstrip("/") == "https://www.paulinecake.ae/ru", "Не вернулись на главную"


