#forma de encontrar elementos utilzando selenium - (EC.visibility_of_element_located) e (driver.execute_script)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

time.sleep(3)
WebDriverWait(driver, 3).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

try:
    #barra de pesquisa
    elemento_barra_pesquisa = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="legalone-search-model"]'))
    )

    # Interagir com o elemento
    elemento_barra_pesquisa.send_keys(processo)
    print('encotrei barra de pesquisa e escrevi o processo')
except TimeoutException:
    print("O elemento 'barra de pesquisa' não foi encontrado dentro do tempo limite.")

finally:
    print('SEGUI PARA A FASE 2')


#checa popup
try:
    time.sleep(3)
    WebDriverWait(driver, 3).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete'
    )
    try:
        #barra de pesquisa
        botao_popup = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="7695e86c-20c3-e615-556f-b48b6f5ba0f6"]'))
        )

        # Interagir com o elemento
        botao_popup.click()
        print('encotrei barra de pesquisa e escrevi o processo')
    except TimeoutException:
        print("O elemento 'barra de pesquisa' não foi encontrado dentro do tempo limite.")

except:
    print('não havia popup')


# localiza o botão pesuisar
time.sleep(3)
WebDriverWait(driver, 3).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

try:
    # botao pesquisar
    botao_pesquisar = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="global-search-find-btn"]'))
    )

    # Interagir com o elemento
    botao_pesquisar.click()
    print('encotrei botao pesquisar')
except TimeoutException:
    print("O elemento 'botao pesquisar' não foi encontrado dentro do tempo limite.")
