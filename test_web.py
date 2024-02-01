from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chromedriver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)
    return driver


def test_name1_h1(chromedriver):
    chromedriver.get('https://concretehouse.by/proekty/doma-so-skatnoy-kryshey/proekt-doma-157-kvm-na-4-spalni.html')
    title = chromedriver.find_element(By.TAG_NAME, 'h1')
    assert title.text == 'Проект дома с крышей скатной 157 кв.м. на 4 спальни'


def test_name2_h1(chromedriver):
    chromedriver.get('https://concretehouse.by/proekty/doma-so-skatnoy-kryshey/proekt-doma-8807-kvm.html')
    title = chromedriver.find_element(By.TAG_NAME, 'h1')
    assert title.text == 'Проект дома 88 кв.м.'
