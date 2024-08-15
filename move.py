from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

webdriver_path = "chromedriver/chromedriver.exe"

# Crea una instancia del servicio de WebDriver
service = Service(executable_path=webdriver_path)

# Inicializa el navegador
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")

action = ActionChains(driver)

#btn = driver.find_element(By.CLASS_NAME, 'donate-button')

# Así es como se mueve el mouse hacia un elemento
#action.move_to_element(to_element=btn)

#action.perform()

# Añadimos un time.sleep() para ver que efectivamente está funcionando
#time.sleep(15)

# Mover el cursor hacia una coordenada específica en la pantalla
#action.move_by_offset(xoffset=100, yoffset=100)

btn2 = driver.find_element(By.LINK_TEXT, 'About')

# Mover el cursor hacia un elemento y luego hacer un desplazamiento
action.move_to_element_with_offset(btn2, 150, 0).click()

action.perform()

time.sleep(20)

driver.quit()