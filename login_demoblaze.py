from selenium import webdriver #driver untuk website
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests


def login (driver):

    print("⏳ Halaman ditampilkan selama 3 detik...")
    time.sleep(3)

    driver.find_element(By.ID, "login2").click()
    time.sleep(3)

    username = "ultratester2"
    password = "p@ssw0rd"

    username_field = driver.find_element(By.ID, "loginusername")
    password_field = driver.find_element(By.ID, "loginpassword")

    username_field.send_keys(username)
    password_field.send_keys(password)

    driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()

    time.sleep(5)
    try : 
        user = driver.find_element(By.ID, "nameofuser")
        print("✅ User ini adalah:", user.text)
    except:
        print("❌ ID tidak ditemukan.")

    print("✅ Sudah masuk ke halaman login")
    time.sleep(15)
