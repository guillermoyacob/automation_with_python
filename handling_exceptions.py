from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

webdriver_path = "chromedriver/chromedriver.exe"

# Crea una instancia del servicio de WebDriver
service = Service(executable_path=webdriver_path)

# Inicializa el navegador
driver = webdriver.Chrome(service=service)

# Abre una página web
driver.get("https://www.python.org")

action = ActionChains(driver)

# Ponemos el código que puede fallar dentro del bloque 'try' y la excepción dentro del bloque 'except'. También tenemos que importar la excepción de la librería 'exceptions'
try:
  search = driver.find_element(By.CLASS_NAME, 'dinate-button')
except NoSuchElementException:
  print("Element with the specified classname does not exist")

# Ponemos un time.sleep(10) para que no se cierre inmediatamente el navegador
time.sleep(10)

driver.quit()