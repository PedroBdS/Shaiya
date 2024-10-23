import pyautogui
from PIL import ImageGrab
import time

def click_ingame(coordenada, delay=0):
    coordenada2 = (coordenada[0]+1, coordenada[1])

    pyautogui.moveTo(coordenada)
    pyautogui.mouseDown()

    pyautogui.moveTo(coordenada)

    pyautogui.moveTo(coordenada)

    pyautogui.mouseUp()

def get_pixel_color(x, y):
    # Captura a tela e pega a cor do pixel na coordenada (x, y)
    screen = ImageGrab.grab()
    return screen.getpixel((x, y))

def esperar_mudanca_de_cor(coordenada_clique, coordenada_verificar):
    # Captura a cor inicial do pixel na coordenada_verificar
    cor_inicial = get_pixel_color(*coordenada_verificar)

    # Realiza o clique na coordenada_clique
    print("Clicando na coordenada:", coordenada_clique)
    click_ingame((coordenada_clique))

    # Marca o tempo do clique
    tempo_inicial = time.time()

    # Fica verificando até que a cor do pixel mude
    while True:
        cor_atual = get_pixel_color(*coordenada_verificar)
        if cor_atual != cor_inicial:
            # Se a cor mudou, sai do loop
            break
        # Espera um curto intervalo antes de verificar novamente
        # time.sleep(0.1)

    # Calcula o tempo total decorrido
    tempo_total = time.time() - tempo_inicial
    print(f"A cor mudou após {tempo_total:.2f} segundos.")

# Coordenadas de exemplo (modifique conforme necessário)
coordenada_clique = (1250, 312)  # Coordenada onde o clique ocorrerá
coordenada_verificar = (779, 392)  # Coordenada onde a cor será verificada

# Chama a função
esperar_mudanca_de_cor(coordenada_clique, coordenada_verificar)
