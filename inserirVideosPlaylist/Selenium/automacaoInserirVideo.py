from selenium import webdriver # Importa o WebDriver para acesso ao navegador
from selenium.webdriver.common.by import By
import time # Biblioteca de tempo

# Cria uma instância do Navegador (WebDriver Chrome) e inicializa 
navegador = webdriver.Chrome()

# Maximiza a tela do navegador
navegador.maximize_window()

# Navega até o link da página da playlist
navegador.get("https://www.youtube.com/playlist?list=PLHz_AreHm4dmSj0MHol_aoNYCSGFqvfXV")

# Busca um vídeo da playlist pelo seu seletor css
video = navegador.find_element("css selector", "a.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer")

# Busca todos os vídeos da playlist pelo seu seletor css
videos = navegador.find_elements("css selector", "a.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer")


# # Clica no vídeo
# video.click()

# Aguarda 10s
time.sleep(10)