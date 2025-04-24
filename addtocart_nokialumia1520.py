from selenium import webdriver #driver untuk website
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

from login_demoblaze import login

def addtocart_nokialumia1520 (driver) :
    driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/div/h4/a').click()
    time.sleep(4)

    user = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/h2')
    print("✅ Item ini adalah:", user.text)

    driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a').click()
    time.sleep(4)

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    print("✅ Terima Kasih!:", alert.text)
    alert.accept()

    driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a').click()
    time.sleep(4)