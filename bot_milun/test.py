from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import random


def cookies():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="cookie_action_close_header"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="onesignal-popover-allow-button"]'))).click()


def find_links():
    playlist = driver.find_elements(By.CLASS_NAME, 'slide.ignore')
    for url in playlist:
        driver.execute_script(
            'window.open("{}" ,"_blank");'.format(url.get_attribute('href')))


driver = webdriver.Firefox()
driver.get('https://www.tonimilun.hr/gradivo/uvod-u-vedsku-matematiku/')
main_window = driver.current_window_handle

cookies()
sleep(3)
find_links()

sleep(25)
driver.quit()
