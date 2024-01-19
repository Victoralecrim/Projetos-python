import pyautogui as pg
import time
import os

pg.alert("Por favor não mexa em nada no seu computador enquanto o codigo está rodando.")
pg.PAUSE = 0.5

# 1-Abrir ou Alternar de janela e abrir o telegram no meu computador

# Alterna de janela e move o cursor até a janela desejada atrvés de uma determinada posição
pg.hotkey('winleft', '9')

# Aguarda um curto período para garantir que a troca de janelas seja concluída
time.sleep(5)

# 2-Após aberto o telegram, mover o cursor do mouse para a barra de pesquisa
pg.moveTo(154, 48)

# clica no campo de pesquisa
pg.click(154, 48)

# Aguarda um tempo antes de escrever no campo
time.sleep(2)

# 3-Buscar no campo de pesquisa por ".NET"
pg.write(".NET")

# 4-Mover o cursor do mouse para o curso com o titulo ".NET MAUI"
pg.moveTo(156, 290)
# clica com o botão esquerdo do mouse em cima do curso desejado
pg.click(button='left')
#  Espera um tempo
time.sleep(3)

# Mover e Clicar com o mouse em cima do icone escrito "pinned message" ao abrir o curso a primeira vez
pg.moveTo(881, 92)
pg.click(button='left')

# 4-Mover o cursor do mouse para perto de onde está escrito "=1 Introdução" e selecionar a hashtag #F01 localizada na parte de introdução
pg.moveTo(775, 456)
time.sleep(1)
pg.click(button='left')
# #Aguarda um tempo
time.sleep(2)

# 5-Move o cursor e Clica no curso desejado com o botão esquerdo do mouse
pg.moveTo(173, 278)
pg.click(button='left')

# Espera um tempo novamente
time.sleep(3)

# 6-Mover o cursor do mouse para selecionar o video desejado
pg.moveTo(778, 486)
# clica no video
pg.click(button='left')
# Espera um tempo
time.sleep(2)
# move o cursor do mouse até o botão de download do video
pg.moveTo(1802, 1049)
# clica com o botão esquerdo do mouse
pg.click(button='left')
# Aguarda um tempo
time.sleep(2)
# Move o cursor do mouse para o botão de passar para o proximo video do video 1
pg.moveTo(1880, 533)
# Clica com o botão esquerdo do mouse
pg.click(button='left')
# #Espera um tempo
time.sleep(2)
# Move novamente o cursor do mouse até o botão de download depois de ter passado para o segundo video
pg.moveTo(1805, 1048)
# clica com o botão esquerdo do mouse em cima do botão de download do video
pg.click(button='left')
# #Espera um tempo
time.sleep(2)
# Move novamente o cursor do mouse para passar para o proximo video
pg.moveTo(1878, 538)
# clica no video com o botão esquerdo do mouse
pg.click(button='left')

# Move o cursor do mouse até o botão de download do video
pg.moveTo(1808, 1046)
# Aguarda um tempo
time.sleep(1)
# Clica com o mouse em cima do botão de download
pg.click(button='left')
# Aguarda um tempo
time.sleep(2)

# 11-Mover o cursor do mouse até o botão de passar o video na determinada posição
pg.moveTo(1877, 537)
# clicar com o botão esquerdo do mouse
pg.click(button='left')
# Espera um tempo
time.sleep(2)

# 12 - Mover novamente o cursor do mouse até o botão de passar o video
pg.moveTo(1804, 1058)
# clicar com o botão esquerdo do mouse
pg.click(button='left')
# pressiona esc para sair do video depois de baixado
pg.press('esc')
# #Espera um tempo
time.sleep(2)

# 14-Abrir o explorer e navegar até a pasta Telegram Desktop

# Abrir o Explorer (Windows)
pg.hotkey('winleft', 'e')

# Aguardar um curto período para garantir que o Explorer seja aberto
time.sleep(1)

# 13- Digitar o caminho da pasta Telegram Desktop na barra de endereço do Explorer

# Obter a posição atual do cursor antes de movê-lo
posicao_atual = pg.position()

# Mover o cursor apenas se a posição atual do explorer for diferente da especificada
match posicao_atual:
    case (1471, 183):
        pg.moveTo(568, 126)
    case (568, 126):
        pg.moveTo(565, 137)
    case (565, 137):
        pg.moveTo(534, 74)
    case (534, 74):
        pg.moveTo(552, 98)
    case (552, 98):
        pg.moveTo(549, 75)
    case (549, 75):
        pg.moveTo(1025, 183)
    case _:
        pg.moveTo(1357,282)

# Espera um tempo
time.sleep(2)
# clicar com o botão esquerdo do mouse na barra de endereço
pg.click(button='left')
# Armezenando o caminho da pasta em uma variavel
caminho_telegram_desktop = r'C:\Users\victo\Downloads\Telegram Desktop'
# Escrevendo o caminho especificado na barra de endereço
pg.write(caminho_telegram_desktop)
pg.press('enter')
# Aguardando um tempo
time.sleep(1.5)

# # 14-Criar 6 pastas dentro do diretorio Telegram Desktop
for i in range(1, 7):
   # Criar uma outra pasta dentro do diretorio Telegram Desktop
    nova_pasta_nome = f'modulo_{i}'
    nova_pasta_caminho = os.path.join(
        caminho_telegram_desktop, nova_pasta_nome)

    # Verificar se a pasta já existe
    if not os.path.exists(nova_pasta_caminho):
        os.makedirs(nova_pasta_caminho)
        print(
            f"Pasta '{nova_pasta_nome}' criada com sucesso em '{caminho_telegram_desktop}'")
    else:
        print(
            f"A pasta '{nova_pasta_nome}' já existe em '{caminho_telegram_desktop}'")

# Espera um tempo
time.sleep(4.5)

# Move o cursor do mouse para o canto do primeiro arquivo de video e em seguida para os demais baixados após o termino do loop
pg.moveTo(1619,615)
butao_esquerdo_mouse = pg.click(button='left')  
pg.hold(butao_esquerdo_mouse) 
time.sleep(1)
pg.moveTo(1322,785)
# Pressiona a tecla control + x do teclado em cima dos arquivos para seleciona-los e copia-los
pg.hotkey('ctrl','x')

pg.alert("Fim do programa")