from selenium import webdriver # Importa o WebDriver para acesso ao navegador
from selenium.webdriver.common.by import By
import time # Biblioteca de tempo
from variables import * # Importa variáveis de urls e elementos para a automação
from tests import * # Importa testes

# Cria uma instância do Navegador (WebDriver Chrome) e inicializa
driver = webdriver.Chrome()

# Maximiza a tela do navegador
driver.maximize_window()

# Acessa o office
driver.get("https://www.office.com/")

time.sleep(120) # Aguarda 2 minutos para que o usuário faça login

# Navega até o link da playlist
driver.get(yt_playlist_url)

# Busca todos os vídeos da playlist pelo seu seletor css e armazena em uma lista
videos = driver.find_elements(By.CSS_SELECTOR, yt_playlist_video_selector)

# Extrai os links (href) de cada vídeo e armazena em uma lista (list comprehension)
playlist = [video.get_attribute("href") for video in videos]

# OPCIONAL -> Salvar os links em um arquivo

# Navega até a página do Sharepoint em Modo de Edição
driver.get(sp_page_edit_url)


# Aguarda 10s
time.sleep(1)