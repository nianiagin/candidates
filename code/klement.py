import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    with allure.step("Запуск браузера Firefox и переход на сайт Red-Soft"):
        browser = webdriver.Firefox()
        browser.get("https://www.red-soft.ru/ru/")
        yield browser
        browser.quit()

@allure.title("Переход в раздел 'Блог'")
def test_navigation_blog(browser):
    with allure.step("Ожидание кликабельности и переход по ссылке 'Новости'"):
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/blog" and contains(@class, "dropdown")]'))).click()
    with allure.step("Проверка URL"):
        assert "/ru/blog" in browser.current_url, "Переход на страницу блога не выполнен"


@allure.title("Переход в раздел 'О компании'")
def test_navigation_about_company(browser):
    with allure.step("Ожидание кликабельности и переход по ссылке 'О компании'"):
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/about_about.html" and contains(@class, "dropdown")]'))).click()
    with allure.step("Проверка URL"):
        assert "/ru/about_about.html" in browser.current_url, "Переход на страницу 'О компании' не выполнен"

@allure.title("Переход в раздел 'Заказчики'")
def test_navigation_customers(browser):
    with allure.step("Ожидание кликабельности и переход по ссылке 'Заказчики'"):
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/customers-ru"]'))).click()
    with allure.step("Проверка URL"):
        assert "/ru/customers-ru" in browser.current_url, "Переход на страницу 'Заказчики' не выполнен"


@allure.title("Переход в раздел 'Партнеры'")
def test_navigation_partners(browser):
    with allure.step("Ожидание кликабельности и переход по ссылке 'Партнеры'"):
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/content/partnership" and contains(@class, "dropdown")]'))).click()
    with allure.step("Проверка URL"):
        assert "/ru/content/partnership" in browser.current_url, "Переход на страницу 'Партнеры' не выполнен"


@allure.title("Переход в раздел 'Образование'")
def test_navigation_education(browser):
    with allure.step("Ожидание кликабельности и переход по ссылке 'Обучение'"):
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/education" and contains(@class, "dropdown")]'))).click()
    with allure.step("Проверка URL"):
        assert "/ru/education" in browser.current_url, "Переход на страницу 'Образование' не выполнен"

@allure.title("Переход в раздел 'Продукты'")
def test_navigation_products(browser):
    with allure.step("Ожидание кликабельности и переход по ссылке 'Продукты'"):
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/rs_products" and contains(@class, "dropdown")]'))).click()
    with allure.step("Проверка URL"):
        assert "/ru/rs_products" in browser.current_url, "Переход на страницу 'Продукты' не выполнен"

@allure.title("Переход в раздел 'Услуги'")
def test_navigation_services(browser):
    with allure.step("Ожидание кликабельности и переход по ссылке 'Услуги'"):
        wait = WebDriverWait(browser, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/ru/service" and contains(@class, "dropdown")]'))).click()
    with allure.step("Проверка URL"):
        assert "/ru/service" in browser.current_url, "Переход на страницу 'Услуги' не выполнен"