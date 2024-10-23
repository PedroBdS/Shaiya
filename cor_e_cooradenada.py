import pyautogui
import keyboard
from PIL import ImageGrab
import time

def get_pixel_color(x, y):
    # Captura a cor do pixel nas coordenadas (x, y)a
    screen = ImageGrab.grab()
    return screen.getpixel((x, y))

# Loop principal
print("Pressione 'a' para capturar as coordenadas e a cor do pixel, ou 'q' para sair.")
while True:
    # Se 'q' for pressionado, o programa será encerrado
    if keyboard.is_pressed('q'):
        print("Encerrando o programa.")
        break
    
    # Se 'a' for pressionado, captura a posição do mouse e a cor do pixel
    if keyboard.is_pressed('a'):
        # Obtém as coordenadas do mouseaa
        x, y = pyautogui.position()

        # Captura a cor do pixel na posição (x, y)
        color = get_pixel_color(x, y)
        
        # Imprime as coordenadas e a cor do pixel
        print(f"Posição do mouse: ({x}, {y}), Cor do pixel: {color}")
        
        # Pausa pequena para evitar capturar várias vezes com um único aperto
        time.sleep(0.2)
