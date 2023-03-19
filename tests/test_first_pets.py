import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.selectors import *


def test_login():
    WebDriverWait(pytest.driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'email'))).send_keys('pronyazpv@ya.ru')
    WebDriverWait(pytest.driver, 5).until(
        EC.element_to_be_clickable((By.ID, 'pass'))).send_keys('07111986')
    WebDriverWait(pytest.driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

    assert WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text == "PetFriends"


def test_web_elements():
    test_login()
    assert WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, HEAD_CSS)))
    assert WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, LOGO_CSS)))
    assert WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, MY_PETS_LINK_CSS)))
    assert WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ALL_PETS_LINK_CSS)))
    assert WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, BTN_EXIT_CSS)))
    assert WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, HEAD_TEXT_CSS)))
    assert WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ALL_PETS_CARD_DECK)))


def test_show_my_pets():
    """ Требуется выполнить с использованием неявного ожидания
        """
    test_login()
    pytest.driver.implicitly_wait(5)
    images = pytest.driver.find_elements(By.CSS_SELECTOR, ALL_PETS_FOTO_CSS)
    names = pytest.driver.find_elements(By.CSS_SELECTOR, ALL_PETS_NAMES_CSS)
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, ALL_PETS_DESCRIPTIONS_CSS)

    for i in range(len(descriptions)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(', ')
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
        age = parts[1].split(' ')[0]
        try:
            assert float(age)
        except ValueError:
            raise AssertionError('age mast be a number')
