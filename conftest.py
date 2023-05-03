import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password


@pytest.fixture(autouse=True)
def test_first():
    pytest.driver = webdriver.Chrome('chromedriver.exe')
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    yield

    pytest.driver.quit()


@pytest.fixture()
def test_my():
    pytest.driver.find_element(By.XPATH, "//a[@href='/my_pets']").click()

    yield

    pytest.driver.quit()
