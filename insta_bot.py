from time import sleep
from selenium import webdriver


browser = webdriver.Firefox()

browser.get('https://www.instagram.com/accounts/login')
sleep(2)
browser.find_element_by_name('username').send_keys('nikola_franicevic18')
browser.find_element_by_name('password').send_keys('KaRIOla293$@')
sleep(2)
browser.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]').click()
