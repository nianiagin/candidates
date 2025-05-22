import time
import os
import cv2
import numpy as np
import pyautogui
import pytesseract
import pygetwindow as gw
import pyperclip
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def find_text_and_click(text, region):
    screenshot = pyautogui.screenshot(region=region)

    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)

    config = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789+-*/='
    data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT, config=config)

    for i in range(len(data['text'])):
        if data['text'][i].strip() == text:
            x = data['left'][i] + region[0]
            y = data['top'][i] + region[1]
            w = data['width'][i]
            h = data['height'][i]
            pyautogui.click(x + w // 2, y + h // 2)
            return True, (x, y, w, h)
    print(f'Не удалось найти "{i}"')
    return False

r = 0
c = ['1','2','3','4','5','6','7','8','9','0']
dd = ["сложение", "Cложение", "+", "вычитание", "Вычитание", "-", "умножение", "Умножение", "*", "деление", "Деление", ":", "/"]
a = input("Ведите первое целое число: ")
i = 0
while type(a) != int:
    while i <= len(a)-1:
        if a[i] not in c:
            print("Введено некорректное значение, повторите попытку")
            a = input("Ведите первое целое число: ")
            i = 0
        else:
            i += 1
    a = int(a)
b = input("Ведите второе целое число: ")
i = 0
while type(b) != int:
    while i <= len(b)-1:
        if b[i] not in c:
            print("Введено некорректное значение, повторите попытку")
            b = input("Ведите второе целое число: ")
            i = 0
        else:
            i += 1
    b = int(b)
d = input("Выберите арифметическое действие (сложение/вычитание/умножение/деление):")
while d not in dd:
    print("Неизвестное действие, повторите попытку.")
    d = input("Выберите арифметическое действие (сложение/вычитание/умножение/деление):")
if d == "сложение" or d == "Cложение" or d == "+":
    d = "+"
    r = a+b
elif d == "вычитание" or d == "Вычитание" or d == "-":
    d = "-"
    r = a-b
elif d == "умножение" or d == "Умножение" or d == "*":
    d = "*"
    r = a*b
elif d == "деление" or d == "Деление" or d == ":" or d == "/":
    d = "/"
    r = a/b
r=float(r)
a=str(a)
b=str(b)

os.startfile(r"C:\Калькулятор\dist\calc2.exe")
time.sleep(2)

calc_window = gw.getWindowsWithTitle("Калькулятор")[0]
calc_window.activate()
time.sleep(1)

left, top, width, height = calc_window.left, calc_window.top, calc_window.width, calc_window.height
calc_region = (left, top, width, height)

for i in a:
    found, pos = find_text_and_click(i, calc_region)
    time.sleep(1)

found, pos = find_text_and_click(d, calc_region)
time.sleep(1)

for i in b:
    found, pos = find_text_and_click(i, calc_region)
    time.sleep(1)

found, pos = find_text_and_click("=", calc_region)
time.sleep(1)

pyautogui.click(left + width//2, top + 60)
time.sleep(1)

pyautogui.hotkey('ctrl', 'a')
time.sleep(1)

pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

calc_result = float(pyperclip.paste())

pyautogui.hotkey('alt', 'f4')

print("Ответ программы: " + str(r))
print("Ответ калькулятора: " + str(calc_result))
if float(r) == float(calc_result):
    print("Ответы совпадают. Калькулятор работает корректно")
else:
    print("Ответы не совпадают. Калькулятор работает некорректно")