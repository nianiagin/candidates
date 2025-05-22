from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com")
    print("Сайт открыт")
    ab_test_link = driver.find_element(By.LINK_TEXT, "A/B Testing")
    ab_test_link.click()
    print("Клик по ссылке 'A/B Testing' выполнен.")
    time.sleep(2)

    heading = driver.find_element(By.TAG_NAME, "h3")
    if "A/B Test" in heading.text:
        print("A/B Test control passed")
    else:
        print("A/B Test control failed")
    driver.back()
    time.sleep(3)

    heading = driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
    print("Перешли на Add/Remove Elements.")
    time.sleep(2)

    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
    print("Кнопка 'Add Element' нажата.")
    time.sleep(2)

    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    if delete_buttons:
        print("Кнопка 'Delete' появилась")
    else:
        print("Кнопка 'Delete' не появилась")

    delete_buttons[0].click()
    print("Кнопка 'Delete' нажата.")
    time.sleep(1)

    delete_buttons_after = driver.find_elements(By.CLASS_NAME, "added-manually")
    if not delete_buttons_after:
        print("Кнопка 'Delete' удалена")
    else:
        print("Кнопка 'Delete' осталась")

    driver.back()
    time.sleep(3)

    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    time.sleep(2)

    success_message = driver.find_element(By.CSS_SELECTOR, "div.example p").text
    if "Congratulations" in success_message:
        print("Basic Auth passed")
    else:
        print("Basic Auth failed")

    driver.back()
    time.sleep(3)

    driver.get("https://the-internet.herokuapp.com/challenging_dom")
    header = driver.find_element(By.TAG_NAME, "h3").text
    if "Challenging DOM" in header:
        print("Challenging DOM загружена")

    for i in range(3):  # У нас там всегда 3 кнопки
        buttons = driver.find_elements(By.CSS_SELECTOR, "div.example .button")
        if i < len(buttons):
            button = buttons[i]
            print("Кликаю по кнопке:", button.get_attribute("class"))
            button.click()
            time.sleep(1)

    cell = driver.find_element(By.XPATH, '//table//tbody/tr[1]/td[1]')
    print("Значение ячейки:", cell.text)
    time.sleep(3)

finally:
    driver.quit()
    print("Браузер закрыт")