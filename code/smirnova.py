from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://demoqa.com/automation-practice-form")
    driver.execute_script("""
        var elements = document.querySelectorAll('footer, #fixedban');
        for (var i = 0; i < elements.length; i++) {
            elements[i].remove();
        }
    """)
    time.sleep(1)

    wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("Иван")
    driver.find_element(By.ID, "lastName").send_keys("Петров")
    driver.find_element(By.ID, "userEmail").send_keys("ivan.petrov@example.com")
    male_radio = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Male')]")))
    driver.execute_script("arguments[0].click();", male_radio)
    driver.find_element(By.ID, "userNumber").send_keys("1234567890")
    dob = driver.find_element(By.ID, "dateOfBirthInput")
    dob.click()
    dob.send_keys(Keys.CONTROL + "a")
    dob.send_keys("15 May 1990")
    dob.send_keys(Keys.ENTER)
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths")
    subjects.send_keys(Keys.ENTER)
    subjects.send_keys("Physics")
    subjects.send_keys(Keys.ENTER)
    sports_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Sports')]")))
    driver.execute_script("arguments[0].click();", sports_checkbox)
    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", submit_btn)
    success = wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
    assert "Thanks for submitting the form" in success.text
    print("Тест пройден успешно!")
except Exception as e:
    print(f" Ошибка: {str(e)}")
    driver.save_screenshot("error.png")
finally:
    time.sleep(3)
    driver.quit()