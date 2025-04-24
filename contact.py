from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from login_demoblaze import login

        
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/index.html")

login(driver)

contact_button = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Contact']"))
 )

driver.execute_script("arguments[0].scrollIntoView(true);", contact_button)
contact_button.click()

time.sleep(3)

print("✅ Contact button successfully clicked!")

driver.find_element(By.ID, "recipient-email").send_keys("mail@mail.com")
driver.find_element(By.ID, "recipient-name").send_keys("usertester")
driver.find_element(By.ID, "message-text").send_keys("hi, this is for testing puporses")
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="exampleModal"]/div/div/div[3]/button[2]').click()
time.sleep(5)

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
print("✅ Popup!:", alert.text)
alert.accept()

driver.quit()
