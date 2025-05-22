from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.invokergame.com")

driver.find_element(By.XPATH, "//input[@value='CLASSIC']").click()


driver.find_element(By.XPATH, "//a[.//sub[contains(text(), 'PLAY')]]").click()
# ну типо можно было на энтер нажать через боди, можно было клик


body = driver.find_element(By.TAG_NAME, "body")
#явного поля с импутом тут нет
spells={"Cold Snap": "QQQR","Ghost Walk" :"QQWR", "Ice Wall":"QQER", "EMP":"WWWR", "Tornado":"WWQR","Alacrity":"WWER","Sun Strike":"EEER","Forge Spirit":"EEQR","Chaos Meteor":"EEWR","Deafening Blast":"QWER",'':''}


count=0
driver.find_element(By.XPATH, "//input[@value='START GAME (Press Enter)']").click()
while count!=10:
    count+=1
    spell_element = driver.find_element(By.XPATH, "//*[starts-with(@id, 'Spell_')]")
    print(spell_element.text, spells[spell_element.text])
    body.send_keys(spells[spell_element.text])

# print(driver.find_element(By.CLASS_NAME,"infobox spellList").text)
print(driver.find_element(By.CLASS_NAME,"StatsMainStatResult").text)
# print(driver.find_element(By.TAG_NAME, "span").text)