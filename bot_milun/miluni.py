from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import random


komentari = ['Hvala puno!', 'Jako poučno!', 'Legenda si!', 'Hvala!', 'Veoma poučno!',
             'super', 'odlično', 'ekstra', 'hvala', 'Bog si!', 'ovo mi je jako pomoglo', 'dobio sam 5 radi tebe!', 'poučno', 'zanimljivo', 'hvala puno', 'ekstra objašnjeno', 'svaka čast', 'svaka ti dala', 'čudo si', 'e da si mi bar profesor', 'nisam skužio ali hvala', 'bit ce 2 valjda']

driver = webdriver.Firefox()
driver.get('https://www.tonimilun.hr/prijava/')
main_window = driver.current_window_handle


def cookies():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="cookie_action_close_header"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="onesignal-popover-allow-button"]'))).click()


def prijava(email, password):
    driver.find_element(
        By.XPATH, '/html/body/div[4]/div/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/input').send_keys(email)
    driver.find_element(
        By.XPATH, '/html/body/div[4]/div/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/input').send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/div/div/div[1]/div[2]/div[1]/form/button'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/div/div/div[1]/div[2]/div[1]/form/button'))).click()


def video():
    # driver.switch_to.frame(driver.find_element(
    #    By.XPATH, '/html/body/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div/iframe'))
    # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
    #   (By.XPATH, '/html/body/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div/iframe')))  # video frame
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    #    (By.XPATH, '/html/body/div/div[3]'))).click()  # play button
    # driver.switch_to.default_content()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[3]/div/div/a'))).click()  # komentiraj 1
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[3]/div/div/div/textarea'))).send_keys(random.choice(komentari))  # text area
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[3]/div/div/div/div/a[2]'))).click()  # post koment
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/ul/li[5]'))).click()  # 5 star
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/a/span'))).click()  # ocjeni button


def findopen_links():
    driver.execute_script(
        'window.open("https://www.tonimilun.hr/gradivo/razlika-kvadrata-1s1p/","_blank");')
    driver.switch_to.window(driver.window_handles[1])
    sleep(5)
    playlist = driver.find_elements(By.CLASS_NAME, 'slide.ignore')
    for url in playlist:
        driver.switch_to.window(driver.window_handles[1])
        sleep(3)
        driver.execute_script(
            'window.open("{}" ,"_blank");'.format(url.get_attribute('href')))
        sleep(3)
        driver.switch_to.window(
            driver.window_handles[2])
        video()
        sleep(3)


cookies()
sleep(1)
prijava('nikola007f1@gmail.com', 'kapula123456')
sleep(2)
findopen_links()
sleep(30)
driver.quit()


'''if __name__ == "__main__":
    main()'''



'''
elements = driver.find_elements_by_class_name('blue')
for url in elements:
    print(url.get_attribute('href'))
    url.get_attribute('href').send_keys(Keys.COMMAND + 't')
'''
'''for handle in driver.window_handles:
    driver.switch_to_window(handle)'''
