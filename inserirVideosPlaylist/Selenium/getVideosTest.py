# Verifica se foram encontrados todos os vídeos da playlist (obtidos com find_elements e armazenados em lista)

def checkVideosInPlaylist (videos_encontrados, total_videos_playlist):
    counter = 0 # contador para os elementos da lista
    # Para cada vídeo da lista encontrada
    for video in videos_encontrados:
        counter += 1 # Conta o vídeo
        print(f"Video {counter}: {video}")
        print(f"FORAM ENCONTRADOS {counter} VÍDEOS.")
        # Verifica se o número achado é igual ao total esperado
        if counter == total_videos_playlist:
            print("TODOS OS VÍDEOS FORAM ENCONTRADOS COM SUCESSO!")