from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


# Настройка драйвера
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

try:
    # 1. Открываем сайт
    driver.get("https://www.agar.io/")
    time.sleep(2)

    # 2. Вводим ник
    wait.until(EC.element_to_be_clickable((By.ID, "nick"))).send_keys("Leonid")

    # 3. Выбираем Experimental режим
    exp = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mode_experimental"]/span')))
    driver.execute_script("arguments[0].click();", exp)
    wait.until(lambda d: "#experimental" in d.current_url)

    # 4. Нажимаем Play
    play = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="play"]')))
    play.click()

    # 5. Проверяем запуск
    wait.until(EC.presence_of_element_located((By.ID, "canvas")))
    print("Игра успешно запущена!")
    time.sleep(10)

except Exception as e:
    print(f"Ошибка: {e}")
    driver.save_screenshot("error.png")

finally:
    driver.quit()
#код с наименьшим кол-вом строк