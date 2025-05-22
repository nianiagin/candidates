from selenium import webdriver  # Импорт модуля для управления браузером
from selenium.webdriver.common.by import By  # Импорт класса для указания метода поиска элементов (по ID, XPATH и т.д.)
from selenium.webdriver.common.keys import Keys  # Импорт для работы с клавишами (например, Enter)
from selenium.webdriver.support.ui import WebDriverWait  # Импорт для ожидания появления элементов
from selenium.webdriver.support import expected_conditions as EC  # Импорт стандартных условий ожидания (элемент кликабелен, присутствует и т.д.)

# Настройка драйвера Edge
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

try:
    # 1. Открыть главную страницу YouTube на русском
    driver.get("https://www.youtube.com/?hl=ru")

    # # 2. Дождаться загрузки iframe с согласием на cookies и кликнуть "Согласен"/"Accept"
    # try:
    #     # Переключиться в iframe (обычно в src присутствует 'consent')
    #     WebDriverWait(driver, 10).until(
    #         EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='consent']"))
    #     )
    #     # Нажать на кнопку согласия (по тексту на кнопке)
    #     accept_btn = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH,
    #             "//button[contains(text(), 'Согласен') or contains(text(), 'Accept') or contains(text(), 'Agree')]"))
    #     )
    #     accept_btn.click()
    #     # Вернуться в основной контент
    #     driver.switch_to.default_content()
    # except Exception as e:
    #     print("Диалог согласия с куки не найден или произошла ошибка:", e)

    # 3. Дождаться появления кнопки входа и нажать её
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='topbar']/div[2]/div[2]/ytd-button-renderer"))
    )
    login_button.click()

    # 4. На странице Google-входа ввести email и пароль
    # Ввод email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_input.send_keys("thisusernameisnotallowed.pass@gmail.com")
    driver.find_element(By.ID, "identifierNext").click()
    # Ввод пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "Passwd"))
    )
    password_input.send_keys("thisusernameisnotallowed")
    driver.find_element(By.ID, "passwordNext").click()

    # 5. Дождаться появления строки поиска на YouTube (после входа)
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='center']/yt-searchbox/div[1]/form/input"))
    )

    # 6. Ввести запрос и выполнить поиск
    search_input.send_keys("Миль попс жу-жу-жу", Keys.ENTER)


    # 7. Открыть первый ролик из результатов поиска
    first_video = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//ytd-video-renderer//a[@id='thumbnail'])[1]"))
    )
    first_video.click()

    # 8. Дождаться завершения видео в реальном времени (через JS video.ended)
    video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "video"))
    )
    # Ожидание завершения видео (таймаут установлен на 3600 секунд на случай долгого видео)
    WebDriverWait(driver, 3600).until(lambda d: d.execute_script("return arguments[0].ended;", video))

    # 9. Перейти на страницу Истории
    driver.get("https://www.youtube.com/feed/history")

    # 10. У первого видео найти элемент прогресса (id="progress") и проверить width в style
    progress = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "progress"))
    )
    style_attr = progress.get_attribute("style")
    # Извлечь числовое значение X из "width:X%"
    if style_attr and "width:" in style_attr:
        try:
            width_value = int(style_attr.split("width:")[1].split("%")[0])
        except Exception:
            width_value = None
    else:
        width_value = None

    # Вывести результат проверки
    if width_value == 100:
        print("всё работает корректно")
    else:
        print(f"шкала прогресса (число width:{width_value}%) работает некорректно")

finally:
    # Закрыть браузер
    driver.quit()
