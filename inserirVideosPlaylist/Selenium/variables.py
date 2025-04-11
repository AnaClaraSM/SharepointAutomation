# ELEMENTOS PARA A AUTOMAÇÃO

# OFFICE

# URL Office 365 - Home
office_home_url = "https://m365.cloud.microsoft/?auth=2"


# YOUTUBE

# Link da Playlist de Vídeos
yt_playlist_url = "https://www.youtube.com/playlist?list=PLpdAy0tYrnKyjrY1Fr72DhmrRmeWI_5C8"

# Seletor de Vídeo Individual da Playlist (Tag a)
yt_playlist_video_selector = "a.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer"


# SHAREPOINT

# Link da Página
sp_page_url = "https://governosp.sharepoint.com/sites/SEADE-Gecon2/SitePages/LogicaProgramacaoCursoEmVideo.aspx"

# Link da Página em Modo de Edição
sp_page_edit_url = "https://governosp.sharepoint.com/sites/SEADE-Gecon2/SitePages/Automacoes-com-Python.aspx?Mode=Edit"

# Seletor da seção rolável da página
sp_scrollable_section_selector = "[data-automation-id=\"contentScrollRegion\"]"

# Número de Colunas (Elementos por Linha) na Página
sp_page_columns = 3

# # Classe do campo de inserção de link do Youtube (div)
# sp_video_url_field_class = "fieldGroup-373"

# Seletor do campo de inserção de link do Youtube (div)
sp_video_url_field_selector = "textarea[placeholder*='https://www.youtube.com']"

# Classe dos botões de adicionar vídeo e atualizar notícias
sp_primary_button_class = "ms-Button--primary"

# Seletor da thumbnail de vídeo do youtube adicionado
sp_video_thumbnail_selector = "iframe[src*='youtube.com/embed']" # iframe com src contendo youtube...