from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket_button_visibility(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')

    assert basket_button != None, '"Add to basket" button is not visible'