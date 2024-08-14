from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver_path = "chromedriver/chromedriver.exe"

# Crea una instancia del servicio de WebDriver
service = Service(executable_path=webdriver_path)

# Inicializa el navegador
driver = webdriver.Chrome(service=service)

# Abre una página web
driver.get("https://www.python.org")

#LOCALIZADORES
#find_element devuelve un elemento, mientras que fiend_elements devuelve una lista de elementos

element1 = driver.find_element(By.ID, 'mainnav')
elements1 = driver.find_elements(By.ID, 'mainnav')

#print(element1)

element2 = driver.find_element(By.CLASS_NAME, 'donate-button')
elements2 = driver.find_elements(By.CLASS_NAME, 'donate-button')

#print(elements2)

element3 = driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[1]/a')

#print(element3)

element4 = driver.find_element(By.LINK_TEXT, 'Donate')

#print(element4)

element5 = driver.find_element(By.TAG_NAME, 'div')
elements5 = driver.find_elements(By.TAG_NAME, 'div')

#print(elements5)

element6 = driver.find_element(By.NAME, 'q')

print(element6)

driver.quit()

