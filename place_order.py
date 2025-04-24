from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from login_demoblaze import login
from addtocart_nokialumia1520 import addtocart_nokialumia1520
from addtocart_macbookpro import addtocart_macbookpro

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/index.html")

login(driver)
addtocart_nokialumia1520(driver)
addtocart_macbookpro(driver)

driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[4]/a').click()
time.sleep(5) 

driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr[1]/td[4]/a').click()
first_item = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="tbodyid"]/tr[1]/td[2]'))
)
item_text = first_item.text

driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr[1]/td[4]/a').click()
print("🗑️ Item yang dihapus:", item_text)
time.sleep(5)

cart_items = driver.find_elements(By.XPATH, '//*[@id="tbodyid"]/tr')

print("🛒 Daftar item di cart:")
total_harga = 0

for index, item in enumerate(cart_items, start=1):
    try:
        # Ambil nama item dan harga
        nama = item.find_element(By.XPATH, './td[2]').text
        harga = item.find_element(By.XPATH, './td[3]').text
        total_harga += int(harga)
        print(f"{index}. {nama} - ${harga}")
    except Exception as e:
        print(f"❌ Gagal membaca item ke-{index}: {str(e)}")

print(f"\n💰 Total harga: ${total_harga}")

driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button').click()
time.sleep(5) 

name = "usertester"
country = "Negara Api"
city = "Konoha"
credit_card = "1234567890"
month = "February"
year = "2025"

name_field = driver.find_element(By.ID, "name")
country_field = driver.find_element(By.ID, "country")
city_field = driver.find_element(By.ID, "city")
credit_card_field = driver.find_element(By.ID, "card")
month_field = driver.find_element(By.ID, "month")
year_field = driver.find_element(By.ID, "year")

name_field.send_keys(name)
country_field.send_keys(country)
city_field.send_keys(city)
credit_card_field.send_keys(credit_card)
month_field.send_keys(month)
year_field.send_keys(year)

time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]').click()
time.sleep(4)

driver.find_element(By.XPATH, '/html/body/div[10]/div[7]/div/button').click()

driver.quit()

