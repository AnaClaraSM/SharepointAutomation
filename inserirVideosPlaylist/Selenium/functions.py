from selenium import webdriver # Importa o WebDriver para acesso ao navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Importa o WebDriverWait para esperas dinâmicas
from selenium.webdriver.support import expected_conditions as EC
import time # Biblioteca de tempo
from variables import * # Importa variáveis de urls e elementos para a automação


# FUNÇÕES


# ROLAR PÁGINA SHAREPOINT

def scroll_page(driver, scrollable_section_selector, scroll_pause_time = 2):
# Recebe como parâmetros o navegador (driver), a seção rolável e o intervalo entre rolagens (2s por padrão)

    # Obtém o elemento rolável
    scrollable_element = driver.find_element(By.CSS_SELECTOR, scrollable_section_selector)
    
    # Variáveis de rolagem
    screen_height = driver.execute_script(f"return {scrollable_element}.clientHeight;") # altura de tela (da seção rolável)
    scroll_height = driver.execute_script(f"return {scrollable_element}.scrollHeight;") # altura total da página/seção rolável (quanto a página pode ser rolada)
    current_position = 0 # posição atual

    # Loop
    while current_position < scroll_height:
        driver.execute_script(f"window.scrollBy(0, arguments[0]);", screen_height) # Rola a página para baixo pela altura da tela (argumento) - (X=0 , Y=screen_height) 
        time.sleep(scroll_pause_time) # aguarda o intervalo
        current_position += screen_height # atualiza a posição atual, somando a altura da tela
        scroll_height = driver.execute_script(f"return {scrollable_element}.scrollHeight;") # atualiza altura total (restante) da página