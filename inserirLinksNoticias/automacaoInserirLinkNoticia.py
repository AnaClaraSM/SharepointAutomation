import pyautogui # PyAutoGUI para automações RPA
import time # Biblioteca de tempo
from links import links # Importa a lista links do arquivo links.py
from coordenadasAutomacao import * # Importa tudo do arquivo de coordenadas

pyautogui.PAUSE = 0.5 # Pausa de 0.5s entre cada ação do pyautogui

# Para cada link da lista de links
for link in links:
    pyautogui.moveTo(addNewsBtn["x"], addNewsBtn["y"])
    pyautogui.click()
    pyautogui.moveTo(addNewsLinkBtn["x"], addNewsLinkBtn["y"])
    pyautogui.click()
    pyautogui.moveTo(newsLinkField["x"], newsLinkField["y"])
    pyautogui.click()
    pyautogui.typewrite(link)
    pyautogui.moveTo(postNewsLinkBtn["x"], postNewsLinkBtn["y"])
    time.sleep(5)
    pyautogui.click()
    time.sleep(5)
    print(f"Link '{link}' adicionado com sucesso!")
print(f"{len(links)} links adicionados!")