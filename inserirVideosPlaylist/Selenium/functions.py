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
    screen_height = driver.execute_script("return arguments[0].clientHeight;", scrollable_element) # altura de tela (da seção rolável)
    scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_element) # altura total da página/seção rolável (quanto a página pode ser rolada)
    current_position = 0 # posição atual

    # Loop
    while current_position < scroll_height:
        driver.execute_script("arguments[0].scrollBy(0, arguments[1]);", scrollable_element, screen_height) # Rola a seção para baixo pela altura da tela - (X=0 , Y=screen_height) 
        time.sleep(scroll_pause_time) # aguarda o intervalo
        current_position += screen_height # atualiza a posição atual, somando a altura da tela
        scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_element) # atualiza altura total (restante) da página
    # Aguarda 2s
    time.sleep(scroll_pause_time)
    # Rola de volta para o topo
    driver.execute_script("arguments[0].scrollTo(0, 0);", scrollable_element)
    # Aguarda mais 2s
    time.sleep(scroll_pause_time)


# BUSCAR BOTÕES DE ADICIONAR VÍDEO E ATUALIZAR PÁGINA SHAREPOINT

# def find_add_update_buttons(driver, scrollable_section_selector, scroll_pause_time = 2):
#     # Buscar botões da página

#     # Rola a página para garantir o carregamento de todos os botões
#     scroll_page(driver, sp_scrollable_section_selector, 2) # Função de rolagem

#     add_video_buttons = [] # Cria lista para botões de adicionar vídeo

#     # Busca todos os botões primários (adicionar vídeo e atualizar página)
#     primary_buttons = driver.find_elements(By.CLASS_NAME, sp_primary_button_class)

#     # Filtra os botões
#     for button in primary_buttons:
#         # Se o texto do botão contiver "Adicionar Vídeo"
#         if "Adicionar vídeo" in button.text:
#             # Adiciona o botão à lista específica
#             add_video_buttons.append(button)
#         # Se o texto for "Atualizar notícias (página)"
#         elif "Atualizar notícias" in button.text:
#             # Armazena o botão
#             update_page_button = button