from functions.funcoes import *

def iniciar_shaiya(conta):
    time.sleep(0.2)

    # Pressiona a tecla Windows
    keyboard.press('windows')
    keyboard.release('windows')

    # Espera um pouco para o menu iniciar abrir
    time.sleep(0.2)

    # Digita "fawkes"
    pyautogui.write('fawkes')

    # Pressiona Enter
    pyautogui.press('enter')

    # PLAY Posição do mouse: (670, 552), Cor do pixel: (236, 56, 36)
    esperar_cor_e_clicar((670, 552),(236, 56, 36), ingame=False, nome='PLAY')

    # Connect Posição do mouse: (1841, 1021), Cor do pixel: (233, 69, 53)
    esperar_cor_e_clicar((1841, 1021), (233, 69, 53), ingame=False, nome='Connect')

    # Login Posição do mouse: (1006, 819), Cor do pixel: (22, 21, 22)
    esperar_cor_e_clicar((1006, 819), (22, 21, 22), nome='Login')
    pyautogui.write(conta)

    # Senha Posição do mouse: (996, 875), Cor do pixel: (23, 24, 27)
    esperar_cor_e_clicar((996, 875), (23, 24, 27), nome='Senha')
    pyautogui.write('Bolinho123321')

    # Entrar Posição do mouse: (991, 965), Cor do pixel: (68, 33, 33)
    esperar_cor_e_clicar((991, 965), (68, 33, 33), nome='Entrar')

    time.sleep(0.3)

    # Por favor espere um momento antes de iniciar novamente a sessão.
    # Posição do mouse: (1023, 509), Cor do pixel: (34, 34, 37)

    if checar_cor((1023, 509), (34, 34, 37)):
        return False

    # A conexão com o servidor foi encerrada.
    # Posição do mouse: (1077, 504), Cor do pixel: (28, 24, 24)

    if checar_cor((1077, 504), (28, 24, 24)):
        return False

    # Servidor Posição do mouse: (951, 658), Cor do pixel: (24, 24, 24)
    esperar_cor_e_clicar((951, 658), (24, 24, 24), nome='Servidor')
                         
    # OK Posição do mouse: (921, 971), Cor do pixel: (63, 32, 32)
    esperar_cor_e_clicar((921, 971), (63, 32, 32), nome='OK')

    # Esperar tela personagens Posição do mouse: (803, 455), Cor do pixel: (11, 8, 5)
    esperar_cor((803, 455), (11, 8, 5), nome='Esperar tela personagens')

    # P1 Posição do mouse: (468, 255), Cor do pixel: (27, 22, 15)
    # esperar_cor_e_clicar((468, 255), nome='P1')

    # P2 Posição do mouse: (468, 378), Cor do pixel: (30, 12, 41)
    esperar_cor_e_clicar((468, 378), nome='P2')

    # P3 Posição do mouse: (468, 508), Cor do pixel: (17, 19, 26)
    # esperar_cor_e_clicar((468, 508), nome='P3')

    # P4 Posição do mouse: (468, 634), Cor do pixel: (16, 23, 21)
    # esperar_cor_e_clicar((468, 634), nome='P4')

    # P5 Posição do mouse: (468, 768), Cor do pixel: (18, 21, 28)
    # esperar_cor_e_clicar((468, 768), nome='P5')

    # Início do jogo Posição do mouse: (1385, 1024), Cor do pixel: (250, 249, 247)
    esperar_cor_e_clicar((1385, 1024), (250, 249, 247))

    # Confirmar ingame Posição do mouse: (939, 1061), Cor do pixel: (251, 239, 185)
    esperar_cor((939, 1061), (251, 239, 185))

    return True