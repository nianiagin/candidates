from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def start_serch():
    driver.find_element(By.CLASS_NAME, "pure-button-primary-progressive").click()

def send_keys_in_search_bar(word):
    driver.find_element(By.ID, "searchInput").send_keys(word)

def litle_wait():
    time.sleep(5)

def check_h1(word):
    if word == (driver.find_element(By.ID, 'firstHeading').text):
        print("Название статьи соотвествует")
        return
    print("Тест поиска по названию статьи не пройден")

def back_and_clear():
    driver.back()
    driver.find_element(By.ID, "searchInput").clear()

def get_and_found_in_search(what_found):
    res = driver.find_elements(By.CLASS_NAME, "mw-search-result")
    titles = [item.get_attribute("data-prefixedtext") for item in res]
    if titles:
        if what_found in titles:
            print("Cтатья найдена в списке")
            return
        else:
            print("Cтатья не найдена в списке")
            return
    print("Ничего не найдено")

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

#Тест поиска по названию статьи
send_keys_in_search_bar("Python")
start_serch()
litle_wait()
check_h1("Python")
back_and_clear()

#Тест поиска с автозаполнением
send_keys_in_search_bar("Автоматизированное тест")
start_serch()
litle_wait()
get_and_found_in_search("Автоматизированное тестирование")
back_and_clear()

#Тест поиска несуществующей статьи
send_keys_in_search_bar("тттттттттттееееееееееесссссссссстттттт")
start_serch()
get_and_found_in_search("тттттттттттееееееееееесссссссссстттттт")
litle_wait()