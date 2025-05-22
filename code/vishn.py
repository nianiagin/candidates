from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Настройки для RedAdm ---
redadm_url = "http://192.168.56.101"
login_username = "Administrator"
login_password = "********"

user_login = "testuser"
user_password = "Testuser123!"

group_name = "testuser_group"
# --- Настройки для RedAdm ---

# --- Локаторы элементов ---
USERNAME_FIELD = (By.NAME, "username")
PASSWORD_FIELD = (By.NAME, "password")
LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-tooster=\"LoginForm-LoadingButton\"]")
DASHBOARD_ELEMENT_CHECK = (By.CSS_SELECTOR, "[data-testid=\"LogoutIcon\"]")

USER_NAV_LINK = (By.XPATH, "//a[contains(@href, '/directory/objectTypeExplorer/user')]")
CREATE_BUTTON = (By.CSS_SELECTOR, "[data-tooster-action=\"openMenu\"]")
NAME_FIELD = (By.NAME, "name")
USER_LOGIN_FIELD = (By.NAME, "sAMAccountName")
USER_PASSWORD_FIELD = (By.NAME, "password")
USER_CONFIRM_PASSWORD_FIELD = (By.NAME, "confirmPassword")
CONFIRM_BUTTON = (By.CLASS_NAME, "css-be4r64")

GROUP_NAV_LINK = (By.XPATH, "//a[contains(@href, '/directory/objectTypeExplorer/group')]")
GROUP_EDIT_BUTTON = (By.XPATH, f"//button[.='Редактировать']")
GROUP_MEMBERS_BUTTON = (By.CSS_SELECTOR, "[data-tooster-action=\"groupMembers\"]")
ADD_BUTTON = (By.CSS_SELECTOR, "[data-tooster-action=\"add\"]")
ADD_MEMBER_BUTTON = (By.CSS_SELECTOR, "[data-tooster=\"AddMembersDrawer-LoadingButton\"]")
SEARCH_USER_FIELD = (By.CSS_SELECTOR, "[placeholder=\"Поиск...\"]")
USER_CHECKBOX = (By.CSS_SELECTOR, f'[data-id^="CN={user_login}"]')

LOG_NAV_LINK = (By.XPATH, "//a[contains(@href, '/log/eventLog')]")
FIRST_ROW = (By.XPATH, "//div[@class='MuiDataGrid-row'][1]")
STATUS_CELL = (By.XPATH, ".//div[@data-field='status']")
ACTION_CELL = (By.XPATH, ".//div[@data-field='action_type']")
# --- Локаторы элементов ---

# --- Хелперы ---
def wait_for_visibility(driver, locator, timeout=10):
    """Ожидает видимости элемента"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_for_clickable(driver, locator, timeout=10):
    """Ожидает, пока элемент станет кликабельным"""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def click(driver, locator, timeout=10):
    """Ожидает кликабельности элемента и кликает на него"""
    wait_for_clickable(driver, locator, timeout).click()

def type_text(driver, locator, text, timeout=10):
    """Ожидает наличия элемента и вводит текст"""
    wait_for_visibility(driver, locator, timeout).send_keys(text)

def find_element_in(parent_element, locator):
    """Находит элемент внутри другого элемента"""
    return parent_element.find_element(*locator)

# --- Хелперы ---


print("Начинаем автотест RedAdm...")

driver = None
try:
    # 1. Инициализация драйвера браузера
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("Драйвер браузера успешно инициализирован.")

    # 2. Переход на страницу входа и логин
    print("Выполняем вход...")
    driver.get(f'{redadm_url}/login')
    type_text(driver, USERNAME_FIELD, login_username)
    type_text(driver, PASSWORD_FIELD, login_password)
    click(driver, LOGIN_BUTTON)

    # 3. Проверка успешного входа
    wait_for_visibility(driver, DASHBOARD_ELEMENT_CHECK)
    print("Вход выполнен успешно.")

    # 4. Создаём нового пользователя
    print(f"Переходим к созданию пользователя и создаем '{user_login}'...")
    driver.get(f'{redadm_url}/directory/objectTypeExplorer/user')
    click(driver, CREATE_BUTTON)
    type_text(driver, NAME_FIELD, user_login)
    type_text(driver, USER_LOGIN_FIELD, user_login)
    type_text(driver, USER_PASSWORD_FIELD, user_password)
    type_text(driver, USER_CONFIRM_PASSWORD_FIELD, user_password)
    click(driver, CONFIRM_BUTTON)
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(CONFIRM_BUTTON))
    print(f"Пользователь '{user_login}' создан.")

    # 5. Создаём новую группу
    print(f"Переходим к созданию группы и создаем '{group_name}'...")
    driver.get(f'{redadm_url}/directory/objectTypeExplorer/group')
    click(driver, CREATE_BUTTON)
    type_text(driver, NAME_FIELD, group_name)
    click(driver, CONFIRM_BUTTON)
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(CONFIRM_BUTTON))
    print(f"Группа '{group_name}' создана.")

    # 6. Добавление пользователя в группу
    print(f"Добавляем пользователя '{user_login}' в группу '{group_name}'...")
    click(driver, GROUP_EDIT_BUTTON)
    click(driver, GROUP_MEMBERS_BUTTON)
    click(driver, ADD_BUTTON)
    type_text(driver, SEARCH_USER_FIELD, user_login)
    click(driver, USER_CHECKBOX)
    click(driver, ADD_MEMBER_BUTTON)
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(ADD_MEMBER_BUTTON))
    print(f"Пользователь '{user_login}' добавлен в группу '{group_name}'.")

    # 7. Проверка выполнения теста в логах
    print("Проверяем запись в журнале событий...")
    driver.get(f'{redadm_url}/log/eventLog')
    first_row_element = wait_for_visibility(driver, FIRST_ROW)

    status_cell = find_element_in(first_row_element, STATUS_CELL)
    status_text = status_cell.text

    action_cell = find_element_in(first_row_element, ACTION_CELL)
    action_text = action_cell.text

    assert "Успешно" in status_text, f"Ожидаемый статус 'Успешно', получен '{status_text}'"
    assert "Добавление членов групп" in action_text, f"Ожидаемое действие 'Добавление членов групп', получено '{action_text}'"

    print("Проверка в журнале успешна: найдена запись о 'Добавлении членов групп' со статусом 'Успешно'.")
    print("\nТест успешно пройден!")

except Exception as e:
    print(f"\nТест провален. Произошла ошибка: {e}")

finally:
    # 8. Завершение: закрытие браузера
    if driver:
        print("Завершаем работу, закрываем браузер...")
        driver.quit()
        print("Браузер закрыт.")

print("Автотест завершен.")