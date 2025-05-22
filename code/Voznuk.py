import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class OrangeHRMTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()

    def test_add_employee(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "password")
        username.send_keys("Admin")
        password.send_keys("admin123")
        driver.find_element(By.TAG_NAME, "button").click()

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM"))).click()

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee"))).click()

        first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        last_name = driver.find_element(By.NAME, "lastName")

        first_name.send_keys("Иван")
        last_name.send_keys("Иванов")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        success_name = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h6[text()='Personal Details']")))
        self.assertTrue(success_name.is_displayed())
        print("✅ Сотрудник успешно добавлен.")

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

