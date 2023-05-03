import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_elements_of_card():
    pytest.driver.implicitly_wait(5)  # Неявное ожидание
    pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')


def test_table_all_pets():
    assert WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located
                                                  ((By.XPATH, "//a[@href='/my_pets']")))  # Явное ожидание
    assert WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located
                                                  ((By.XPATH, "//a[@href='/all_pets']")))  # Явное ожидание
    assert WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located
                                                  ((By.XPATH, "//button[contains(text(), 'Выйти')]")))  # Явное ожидание


def test_my_pets():
    WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located
                                           ((By.XPATH, "//button[contains(text(), 'Выйти')]")))  # Явное ожидание
    pytest.driver.find_element(By.XPATH, "//a[@href='/my_pets']").click()
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'


def test_all_pets_are_presents(test_my):
    """Проверяем, что на странице со списком моих питомцев присутствуют все питомцы"""

    WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located
                                           ((By.CSS_SELECTOR, ".\\.col-sm-4.left")))  # Явное ожидание

    # Сохраняем в переменную stat элементы статистики
    stat = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located
                                           ((By.CSS_SELECTOR, ".table.table-hover tbody tr")))  # Явное ожидание

    # Сохраняем в переменную pets элементы карточек питомцев
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Получаем количество питомцев из данных статистики
    qte_of_pets = stat[0].text.split('\n')
    qte_of_pets = qte_of_pets[1].split(' ')
    qte_of_pets = int(qte_of_pets[1])

    # Получаем количество карточек питомцев
    qte_of_cards = len(pets)

    # Проверяем, что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert qte_of_pets == qte_of_cards


def test_half_pets_photo_available(test_my):
    """ Проверяем, что на странице со списком моих питомцев хотя бы у половины питомцев есть фото """

    WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located
                                           ((By.CSS_SELECTOR, ".\\.col-sm-4.left")))  # Явное ожидание

    # Сохраняем в переменную statistic элементы статистики
    stat = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    # Сохраняем в переменную images элементы с атрибутом img
    qte_of_images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Получаем количество питомцев из данных статистики
    qte_of_pets = stat[0].text.split('\n')
    qte_of_pets = qte_of_pets[1].split(' ')
    qte_of_pets = int(qte_of_pets[1])

    # Находим количество питомцев с фотографией
    qte_of_photos = 0
    for i in range(len(qte_of_images)):
        if qte_of_images[i].get_attribute('src') != '':
            qte_of_photos += 1

    # Проверяем, что количество питомцев с фотографией больше или равно половине количества питомцев
    assert qte_of_photos >= qte_of_pets//2
    print(f'\nФото есть у {qte_of_photos} из {qte_of_pets} животных, что больше половины')
