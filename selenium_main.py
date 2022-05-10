from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

opciones = Options()

opciones.headless = True
opciones.add_argument("--incognito")
opciones.add_argument('log-level=3')
opciones.add_argument('--window-size=1920,1080')

def start_selenium(url):
    global navegador
    navegador = webdriver.Chrome(options=opciones) 
    navegador.implicitly_wait(2)
    navegador.get(url)
    time.sleep(2)

def get_ref():
    elemento = navegador.find_element(By.XPATH, '//*[@id="router-container"]/div/div[3]/div[3]/div[1]/div/div[5]/div[2]/a[1]')
    referencia = elemento.get_attribute('href')

    return referencia

def get_color():
    elemento = navegador.find_element(By.XPATH, '//*[@id="router-container"]/div/div[3]/div[3]/div[1]/div/div[5]/div[2]/a[1]')
    color = elemento.get_attribute('class')
    color = color.split()[-1]

    return color

def selenium_close():
    navegador.close() # Cerramos el navegador de selenium
