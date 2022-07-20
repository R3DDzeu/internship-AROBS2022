from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium. webdriver.common.keys import Keys

def navigator():
    browser: WebDriver = webdriver.Firefox()
    browser.get('https://www.youtube.com/c/Fireship') #pentru a accepta cookies-urile mai usor, am ales sa evit iframeul, folosind link-ul unui canal oarecare
    browser.find_element(By.XPATH, "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span").click()
    browser.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input').send_keys('dQw4w9WgXcQ' + Keys.RETURN)
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='Rick Astley - Never Gonna Give You Up (Official Music Video)']"))).click()

    #este apelat in obsrecorder
