
from ast import Expression
from math import e
from selenium import webdriver
import pyperclip
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time



class basefunctions:
   

    
 def swipe_down(driver, pixels):
    
      try:
    
    # WebDriver'ı belirtilen piksel kadar aşağı kaydıran fonksiyon
       action = ActionChains(driver)
    # JavaScript kullanarak sayfayı belirli bir miktar aşağı kaydırma
       driver.execute_script("window.scrollBy(0, arguments[0]);", pixels)
    
       print("swipe down işlemi yapıldı")
    
      except TimeoutException:
    
       print("swipe down işlemi yapıamadı")
    
 
        
 def reklami_kapat(driver):
     
     reklam_turu_1 = None
     reklam_turu_2 = None
     try:
        # İlk reklam türünü belirleme
        reklam_turu_1 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@id='ad_position_box'])[1]"))  # Reklamın tür 1 XPath'i buraya girilir
        )
        if reklam_turu_1.is_displayed():
            # Reklam tür 1 için kapatma işlemi
            kapatma_dugmesi = reklam_turu_1.find_element(By.XPATH, "(//div[@id='dismiss-button'])[1]']")  # Kapatma düğmesinin XPath'i buraya girilir
            kapatma_dugmesi.click()
            print("Reklam türü 1 kapatıldı.")
     except:
        pass

     try:
        # İkinci reklam türünü belirleme
        reklam_turu_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@id='ad_position_box'])[1]"))  # Reklamın tür 2 XPath'i buraya girilir
        )
        if reklam_turu_2.is_displayed():
            # Reklam tür 2 için kapatma işlemi
            kapatma_dugmesi = reklam_turu_2.find_element(By.CLASS_NAME, "skip btn")  # Kapatma düğmesinin XPath'i buraya girilir
            kapatma_dugmesi.click()
            print("Reklam türü 2 kapatıldı.")
     except:
        pass

     if not (reklam_turu_1 or reklam_turu_2):
        print("Reklam belirmedi veya kapatılamadı.")
        
   
 def elementin_uzerine_gel(driver,element):
     
    
   try:
    # ActionChains objesi oluştur
      action = ActionChains(driver)
    # Belirtilen elementin üzerine gel
      action.move_to_element(element).perform()
      time.sleep(5)
      print("Elementin üzerine gelindi")
   
   except TimeoutException:
      print("Element Bulunamadı")
      
      
 def element_degerini_panoya_kopyala(driver, element_xpath):
    # Elementin değerini bulun
    
     try:
      
       element = driver.find_element(By.XPATH,element_xpath)
       element_degeri = element.text

    # Element değerini panoya kopyalayın
       pyperclip.copy(element_degeri)
       print("Element değeri panoya kopyalandı:", element_degeri)

     except Exception as e:
      print("Hata:", e)
      
       
 def element_degerini_kontrol_et(driver, panodaki_deger,aranan_deger): 
  try:
    # Panodaki değeri alın
     panodaki_deger = pyperclip.paste()

    # Aranan değer ile panodaki değeri karşılaştırın
     if aranan_deger in panodaki_deger:
            print(f"XPath {panodaki_deger} içinde '{aranan_deger}' metni bulundu.")
     else:
            print(f"XPath {panodaki_deger} içinde '{aranan_deger}' metni bulunamadı.")
  except Exception as e:
         print("Hata:",e)
    
    
         
   
   
 def xpath_metinlerini_karsilastir(driver, xpath1, xpath2):
           
     try:
        
        xpath1 = None
        xpath2 = None
        # İlk XPath ile belirtilen elementleri bul
        elements1 = driver.find_elements_by_xpath(xpath1)
        # İkinci XPath ile belirtilen elementleri bul
        elements2 = driver.find_elements_by_xpath(xpath2)
        
        # İlk XPath içindeki metin değerlerini al ve bir listeye ekle
        metin_degerleri1 = [element.text for element in elements1]
        # İkinci XPath içindeki metin değerlerini al ve bir listeye ekle
        metin_degerleri2 = [element.text for element in elements2]
        
        # İki metin listesini karşılaştır
        if metin_degerleri1 == metin_degerleri2:
            print("İki XPath içindeki metin değerleri aynıdır.")
        else:
            print("İki XPath içindeki metin değerleri farklıdır.")
            print("İlk XPath Metin Değerleri:", metin_degerleri1)
            print("İkinci XPath Metin Değerleri:", metin_degerleri2)
     except Exception as e:
        print("Hata:", e)
        
        
        
 def xpath_degeri_içeriyor_mu(driver, xpath, aranan_deger):
    try:
        # XPath ile belirtilen elementi bul
        element = driver.find_element_by_xpath(xpath)
        
        # Elementin metin değerini al
        element_metni = element.text
        
        # Aranan metni içerip içermediğini kontrol et
        if aranan_deger in element_metni:
            print(f"XPath {xpath} içinde '{aranan_deger}' metni bulundu.")
        else:
            print(f"XPath {xpath} içinde '{aranan_deger}' metni bulunamadı.")
    except Exception as e:
        print("Hata:", e)
        
        
 def reklam_kapat(driver):
  
   while True:
        
            # Reklamın görünür hale gelmesini bekleme stratejisi uygula
            reklam_locator = (By.XPATH, "//div[@id='ad_position_box']")
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located(reklam_locator))
            # Reklam kapatma düğmesini veya bağlantısını bulmak ve tıklamak için gerekli kodu buraya ekleyin
            print("Reklam göründü, kapatılıyor...")
            driver.back()

            # Bir sonraki reklamın varlığını tespit etmek için döngüyü sonlandır
            break
   
  
  