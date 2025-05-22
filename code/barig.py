from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.uiua.org/")
#driver.implicitly_wait(7)

driver.find_element(By.LINK_TEXT, "Pad").click()
driver.implicitly_wait(3)

textarea = driver.find_element(By.CLASS_NAME, "code-entry")
textarea.send_keys("⊞(ℂ).⇡120")
#textarea.send_keys("1")
driver.implicitly_wait(3)
button = driver.find_elements(By.XPATH, "//button[text()='Run']")
for elem in button:
    elem.click()
try:
        result = driver.find_element(By.CLASS_NAME, "output-image")
        print("output image exists")
except NoSuchElementException:
        print("output image doesnt exist")

#driver.quit()