import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")  # Отключает уведомления
chrome_options.add_argument("--disable-infobars")       # Отключает всплывающие инфо-бары
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Скрывает режим автоматизации

driver = webdriver.Chrome(options=chrome_options)
# 1. Заходим на сайт YouTube
driver.get("https://www.youtube.com/")


try:
    # 2. Нажимаем на кнопку логина
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='buttons']//ytd-button-renderer//a")),
        message="Не удалось найти/использовать кнопку Входа"
    )
    login_button.click()
    # 2.1. Вводим ПОЧТУ
    email_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys("t71060345@gmail.com" + Keys.RETURN)
    # 2.2. Вводим ПАРОЛЬ
    pass_field = WebDriverWait(driver, 70).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))
    )
    pass_field.send_keys("=19GJ71KJ00=" + Keys.RETURN)

    # 3. Проверяем наличие просмотренных ранее видео
    # Если такие есть - удаляем, что бы избежать возможных багов
    try:
        time.sleep(5)
        driver.get("https://www.youtube.com/feed/history")

        # Пробуем очистить историю, если есть что чистить
        try:
            clear_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='contents']/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div")),
                message="Кнопка очистки истории не найдена"
            )

            if clear_button.is_displayed() and clear_button.is_enabled():
                clear_button.click()

                clear_confirm_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='confirm-button']")),
                    message="Кнопка подтверждения не найдена"
                )
                clear_confirm_button.click()
                time.sleep(1)
                print("🕒 История просмотров успешно очищена")
            else:
                print("Кнопка очистки истории недоступна")
        except:
            print("🕒 История просмотров уже пуста или кнопка недоступна")

        # Откатываемся на главную
        driver.back()
        time.sleep(2)

    except Exception as e:
        print(f"Не удалось обработать историю просмотров: {str(e)}")
    ##

    # 4. Ищем ВИДЕО
    search_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='center']/yt-searchbox/div[1]/form/input"))
    )
    search_field.send_keys("Звуки дождя 10 часов" + Keys.RETURN)

    # 5. Добавляем первые три видео в "Посмотреть позже"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//ytd-video-renderer"))
    )

    # Находим первые три видео
    videos = driver.find_elements(By.XPATH, "//ytd-video-renderer")[:3]

    for video in videos:

        # Нажимаем на меню
        menu_button = video.find_element(By.XPATH, ".//button[contains(@aria-label, 'действий')]")
        menu_button.click()

        # Выбираем "Смотреть позже"
        save_option = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(text(), 'Смотреть позже')]"))
        )
        save_option.click()
        time.sleep(1)
    # 6. Включаем первое видео на 10 секунд
    first_video = videos[0].find_element(By.XPATH, ".//a[@id='video-title']")
    first_video.click()

    # Ждём загрузки плеера
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//video"))
    )

    # Ждём 10 секунд воспроизведения
    time.sleep(10)

    # 7-8 Переходим в раздел "Посмотреть позже" и проверяем количество видео
    driver.get("https://www.youtube.com/playlist?list=WL")
    initial_videos = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, "//ytd-playlist-video-renderer")),
        message="Не удалось загрузить список видео"
    )
    if len(initial_videos) != 3:
        print(f"❌На момент открытия в плейлисте ожидалось 3 видео, найдено {len(initial_videos)}")
    else:
        print(f"📑 На момент открытия в плейлисте {len(initial_videos)} видео")

    # 9. Удаляем просмотренные видео из плейлиста
    # Находим меню плейлиста
    playlist_menu = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='button-shape']/button/yt-touch-feedback-shape/div")),
        message="Кнопка меню плейлиста не найдена"
    )
    playlist_menu.click()

    # Нажимаем на удаление
    remove_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(., 'Удалить просмотренные') or contains(., 'Remove watched')]"))
    )
    remove_option.click()

    # Подтверждаем удаление
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='confirm-button']/yt-button-shape/button/yt-touch-feedback-shape/div"))
        )
    confirm_button.click()

    # 10. Проверка количества оставшихся видео
    time.sleep(3)
    remaining_videos = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, "//ytd-playlist-video-renderer")),
        message="Не удалось загрузить список видео"
    )
    if len(remaining_videos) == 2:
        print(f"✅Тест успешно пройден!")

    else:
        print(f"❌Тест не пройден! После очистки ожидалось 2 видео, найдено {len(remaining_videos)}")

    # 12. (Дополнительно) - чистим за собой плейлист
    # Если ранее (до запуска теста) в плейлисте были другие видео, то скорее всего он выдаст ошибку. Этот блок не только страхует нас от такой ситуации, но и дебажит её, удаляя вообще все видео из плейлиста
    for video in remaining_videos:
        # Кликаем меню (три точки)
        menu_button = video.find_element(By.XPATH, ".//button[contains(@aria-label, 'действий')]")
        menu_button.click()

        # Удаляем видео
        delete_option = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[contains(., 'Удалить из')]"))
        )
        delete_option.click()
        time.sleep(1)
    print("Завершение теста...")
    print("Плейлист очищен, тест завершён")

except Exception as e:
    driver.save_screenshot('debug.png')
    print("Скриншот ошибки сохранен")

finally:
    driver.quit()
