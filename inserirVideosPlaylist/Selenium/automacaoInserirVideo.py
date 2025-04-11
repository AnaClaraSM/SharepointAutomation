from selenium import webdriver # Importa o WebDriver para acesso ao navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Importa o WebDriverWait para esperas dinâmicas
from selenium.webdriver.support import expected_conditions as EC
import time # Biblioteca de tempo
from variables import * # Importa variáveis de urls e elementos para a automação
from functions import *  # Importa funções criadas para a automação
from tests import * # Importa testes


# 1. NAVEGADOR

# Cria uma instância do Navegador (WebDriver Chrome) e inicializa
driver = webdriver.Chrome()

# Maximiza a tela do navegador
driver.maximize_window()


# 2. LOGIN OFFICE

# Acessa o office
driver.get("https://www.office.com/")

# Define espera máxima do navegador para o login
login_wait =  WebDriverWait(driver, 300) # 5min (300s)

# Espera até que a página tenha sido redirecionada para o Office (login realizado)
try:
    login_wait.until(EC.url_contains(office_home_url))
# Se após 5 minutos o login não tiver sido realizado
except:
    # Retorna mensagem de erro no terminal (em vermelho)
    print("\033[91mAUTOMAÇÃO INTERROMPIDA: Login não realizado.\033[0m")
    # Fecha o navegador
    driver.close()
    # Interrompe o programa
    exit()


# 3. YOUTUBE

# Navega até o link da playlist
driver.get(yt_playlist_url)

# Busca todos os vídeos da playlist pelo seu seletor css e armazena em uma lista
videos = driver.find_elements(By.CSS_SELECTOR, yt_playlist_video_selector)

# Extrai os links (href) de cada vídeo e armazena em uma lista (list comprehension)
href_playlist = [video.get_attribute("href") for video in videos]
print(f"HREFs: {href_playlist}")

# Corrige os links da playlist, se necessário 
url_playlist = [] #lista para armazenar urls completas 
# OBS.: Poderia-se modificar a lista original ao invés de criar uma nova
for video_href in href_playlist:
    # Se o link não começa com https...com
    if not video_href.startswith("https://www.youtube.com"):
        url_playlist.append(f"https://www.youtube.com{video_href}") # completa o link e adiciona
    # Se já começa com https...com
    else:
        url_playlist.append(video_href) # apenas adiciona o link
    # OBS.: Verificar possibilidade de outros casos
print(f"URLs: {url_playlist}")



# OPCIONAL -> Salvar os links em um arquivo


# 4. SHAREPOINT

# OBS.: O layout da página onde estarão os cursos deve estar previamente definido. Deve conter todas as youtube webparts necessárias, conforme o número de vídeos da playlist.

# Navega até a página do Sharepoint em Modo de Edição
driver.get(sp_page_edit_url)

# Aguarda o carregamento da página e do modo de edição
time.sleep(5) # 5s

# Buscar botões da página

# Rola a página para garantir o carregamento de todos os botões
scroll_page(driver, sp_scrollable_section_selector, 2) # Função de rolagem

add_video_buttons = [] # Cria lista para botões de adicionar vídeo

# Busca todos os botões primários (adicionar vídeo e atualizar página)
primary_buttons = driver.find_elements(By.CLASS_NAME, primary_button_class)

# Filtra os botões
for button in primary_buttons:
    # Se o texto do botão contiver "Adicionar Vídeo"
    if "Adicionar vídeo" in button.text:
        # Adiciona o botão à lista específica
        add_video_buttons.append(button)
    # Se o texto for "Atualizar notícias (página)"
    elif "Atualizar notícias" in button.text:
        # Armazena o botão
        update_page_button = button

# TRATAR ERROS
# Se total de botões Adicionar vídeo < total de vídeos OU se !update_page_button -> REALIZA A ROLAGEM, BUSCA E FILTRAGEM NOVAMENTE, com intervalo igual a intervalo+1 (demora mais para rolar); Por mais uma tentativa (tentativa = 1; tentativa <= 2; tentativa +=1;). Se erro. Fechar execução e retornar erro de webparts insuficientes.

# Para cada botão de adicionar vídeo (enumerando os índices)
for index, add_button in enumerate(add_video_buttons):
    # Rola até que o botão esteja visível
    driver.execute_script("arguments[0].scrollIntoView()", add_button)
    # Aguarda a visibilidade do botão ou até 10s
    WebDriverWait(driver, 10).until(EC.visibility_of(add_button))
    # Clica no botão de adicionar vídeo
    # Se for o primeiro botão, clica duas vezes
    if index == 0:
        add_button.click()
        time.sleep(2) # Aguarda 2s
        add_button.click()
    # Para os próximo, clica apenas uma vez
    else:
        add_button.click()
    # Busca o campo de inserção de link pela classe
    url_field = driver.find_element(By.CLASS_NAME, sp_video_url_field_class)
    # Digita o link correspondente ao índice do botão
    url_field.send_keys(url_playlist[index])


# Aguarda 1s
time.sleep(1)