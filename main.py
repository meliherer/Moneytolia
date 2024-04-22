
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from base import basefunctions


service = Service (executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver)
driver.implicitly_wait(5)

siteUrl = "https://automationexercise.com/"
driver.get(siteUrl)
print("1. Web sayfasına gidiliyor...")
time.sleep(5)

#Products tabına tıkla
products = driver.find_element(By.XPATH,"//a[@href='/products']")
products.click()
time.sleep(4)
print("2. Product tabına tıklandı")
basefunctions.swipe_down(driver,500)




#Sayfadaki ilk ürünün üzerine gel ve sepete ekle
ilkUrun = driver.find_element(By.XPATH,"(//div[@class='product-overlay'])[1]")
addToChartilkUrun = driver.find_element(By.XPATH,"/html[1]/body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/a[1]")
ilkUrunDeger = "(//h2[contains(text(),'Rs. 500')])[2]"
ikinciUrunDeger = "(//h2[contains(text(),'Rs. 400')])[2]"
addToChartikinciUrun = driver.find_element(By.XPATH,"/html[1]/body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/a[1]")
continueShopping = driver.find_element(By.XPATH,"/html[1]/body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]")

basefunctions.elementin_uzerine_gel(driver,ilkUrun) 
basefunctions.swipe_down(driver,200)
basefunctions.element_degerini_panoya_kopyala(driver,ilkUrunDeger)
addToChartilkUrun.click()
continueShopping.click()
#Sepete git ve kontrol et
cart =driver.find_element(By.XPATH,"//a[normalize-space()='Cart']")
cart.click()
basefunctions.element_degerini_kontrol_et(driver, ilkUrunDeger,"Rs. 500")
time.sleep(5)
driver.back()
basefunctions.swipe_down(driver,200) 

#Sayfadaki ikinci ürünün üzerine gel ve sepete ekle
ikinciUrun = driver.find_element(By.XPATH,"(//div[@class='product-overlay'])[2]")
basefunctions.elementin_uzerine_gel(driver,ikinciUrun)
basefunctions.swipe_down(driver,200) 
basefunctions.element_degerini_panoya_kopyala(driver,ikinciUrunDeger)
addToChartikinciUrun.click()
continueShopping.click()


#Sepete git ve kontrol et

cart =driver.find_element(By.XPATH,"//a[normalize-space()='Cart']")
cart.click()
basefunctions.element_degerini_kontrol_et(driver, ikinciUrunDeger,"Rs. 400")
driver.quit()