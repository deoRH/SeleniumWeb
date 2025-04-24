from selenium import webdriver #driver untuk website
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

driver = webdriver.Chrome()

driver.get("https://www.demoblaze.com/index.html")

print("⏳ Halaman ditampilkan selama 10 detik...")
time.sleep(5)

driver.find_element(By.ID, "signin2").click()
time.sleep(5)

username = "ultratester2"
password = "p@ssw0rd"

username_field = driver.find_element(By.ID, "sign-username")
password_field = driver.find_element(By.ID, "sign-password")

username_field.send_keys(username)
password_field.send_keys(password)

driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
time.sleep(2)

WebDriverWait(driver, 5).until(EC.alert_is_present())
alert = driver.switch_to.alert
print("ALERT:", alert.text)
alert.accept()

driver.quit()