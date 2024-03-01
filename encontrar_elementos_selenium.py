forma de encontrar elementos utilzando selenium - (presence_of_element_located)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar o WebDriver (por exemplo, o ChromeDriver)
driver = webdriver.Chrome(executable_path='/caminho/para/chromedriver')

# Abrir a página da web desejada
driver.get('https://sua_pagina.com')

# Esperar até que o elemento seja visível (ajuste o tempo conforme necessário)
elemento = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'fPP:processosTable:3211868:j_id475'))
)

# Obter o texto do elemento
texto_do_elemento = elemento.text

# Imprimir o texto obtido
print("Texto do elemento:", texto_do_elemento)

# Fechar o navegador
driver.quit()
