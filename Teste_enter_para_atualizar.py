from funcoes import *


def atualizar_com_enter(delay=0):

    nome_antigo = capturar_tela((808, 380), (1025, 383))
    valor_antigo = capturar_tela((1176, 400), (1287, 403))

    while True:

        click_ingame((1250, 312))

        time.sleep(delay)

        nome_novo = capturar_tela((808, 380), (1025, 383))

        if not imagens_iguais(nome_antigo, nome_novo):
            return nome_novo

        valor_novo = capturar_tela((1176, 400), (1287, 403))

        if not imagens_iguais(valor_antigo, valor_novo):
            return nome_novo
        
        if keyboard.is_pressed('F1'):
            print("Encerrando.")
            exit()


while True:
    nome = atualizar_com_enter()
    nome_novo = capturar_tela((808, 380), (1025, 383))
    if not imagens_iguais(nome, nome_novo):
        print(f'nomes diferentes\n')
        break
    if keyboard.is_pressed('F1'):
            print("Encerrando.")
            exit()