from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

webdriver_path = "chromedriver/chromedriver.exe"

# Crea una instancia del servicio de WebDriver
service = Service(executable_path=webdriver_path)

# Inicializa el navegador
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")

action = ActionChains(driver)

search = driver.find_element(By.ID, 'id-search-field')

# key down y key up
# action.key_down('p', search).key_down('y')

# Para no escribir las letras una por una podemos usar el método send_keys, pero para usar este método primero debemos hacer un click en el elemento a escribir

# search.click()

# action.send_keys('python')

# action.click(search).send_keys('I love Python')


# Para las teclas especiales como Shift y espacio tenemos que importar la libreria Keys
# action.click(search).send_keys('Python').key_down(Keys.SPACE).send_keys('Chain')

# Se resetea para descartar las acciones anteriores, para que perform() realice solo las acciones que están luego del reset
# action.reset_actions()


action.perform()

time.sleep(5)

driver.quit()