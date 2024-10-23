from funcoes import *

shaiya_aberto = checar_cor((939, 1061), (251, 239, 185))

if not shaiya_aberto:
    iniciar_shaiya('PedroGeromito')

abrir_leilao()
time.sleep(0.4)
click_ingame((931, 444))

while True:
    if keyboard.is_pressed('F1'):
        print("Encerrando.")
        exit()

    if not leilao_posicao_correta():
        corrigir_leilao()

    atualizar_leilao()

    try:
        nome, valor = ler_nome(), ler_valor()
        # print(f'\nItem: {nome}\nValor lido: {valor}')

    except:
        continue

    if not valor:
        corrigir_leilao()
        continue

    comprar = comparar_item(nome, valor)

    if comprar:

        CONFERIR_E_COMPRAR(nome, valor)
        print(f'Autorizada compra de {nome} por {valor}')

    if keyboard.is_pressed('F1'):
        print("Encerrando.")
        exit()
