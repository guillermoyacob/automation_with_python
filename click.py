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

tab = driver.find_element(By.CLASS_NAME, 'donate-button')

# hacer un click
# action.click(on_element=tab)

#hacer un doble click
# action.double_click(on_element=tab)

# hacer click y mantener
action.click_and_hold(on_element=tab)

# agregamos un timer para diferenciar el click normal del click mantenido
time.sleep(5)

# si se realiza un hold es una buena idea luego hacer un release para "soltar" el click
action.release(tab)

# al final de las acciones que indiquemos siempre debe ir un action perform
action.perform()

time.sleep(10)

# cerrar solo la pestaña actual en la que el driver está trabajando
# driver.close()

# cerrar el navegador
driver.quit()