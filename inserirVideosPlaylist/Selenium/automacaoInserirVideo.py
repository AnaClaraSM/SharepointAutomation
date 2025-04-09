from selenium import webdriver # Importa o WebDriver para acesso ao navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Importa o WebDriverWait para esperas dinâmicas
from selenium.webdriver.support import expected_conditions as EC
import time # Biblioteca de tempo
from variables import * # Importa variáveis de urls e elementos para a automação
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
    login_wait.until(EC.url_contains("https://m365.cloud.microsoft/?auth=2"))
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
playlist = [video.get_attribute("href") for video in videos]

# OPCIONAL -> Salvar os links em um arquivo

# 4. SHAREPOINT

# OBS.: O layout da página onde estarão os cursos deve estar previamente definido. Deve conter todas as youtube webparts necessárias, conforme o número de vídeos da playlist.

# Navega até a página do Sharepoint em Modo de Edição
driver.get(sp_page_edit_url)

# Busca todos os botões de adicionar vídeo da página


# 


# Aguarda 10s
time.sleep(1)