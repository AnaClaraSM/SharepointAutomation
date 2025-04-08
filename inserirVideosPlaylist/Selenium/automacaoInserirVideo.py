from selenium import webdriver # Importa o WebDriver para acesso ao navegador
from selenium.webdriver.common.by import By
import time # Biblioteca de tempo
from variables import * # Importa variáveis de urls e elementos para a automação
from tests import *

# Cria uma instância do Navegador (WebDriver Chrome) e inicializa
driver = webdriver.Chrome()

# Maximiza a tela do navegador
driver.maximize_window()

# Navega até o link da playlist
driver.get(yt_playlist_url)

# Busca todos os vídeos da playlist pelo seu seletor css e armazena em uma lista
videos = driver.find_elements(By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer")

# Extrai os links (href) de cada vídeo e armazena em lista
playlist = [] # cria lista vazia
# Para cada vídeo
for video in videos:
    playlist.append(video.get_attribute("href")) # adiciona o link do vídeo na lista
findVideosTest(playlist, 17)

# video.click()

# Aguarda 10s
time.sleep(1)