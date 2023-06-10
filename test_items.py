from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def test_find_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    time.sleep(5)

    WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket"), )
    )
#    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket") #By.XPATH, "//form[@id='add_to_basket_form']/button[@type='submit']"

    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    except NoSuchElementException:
        assert False, 'button is not found'
