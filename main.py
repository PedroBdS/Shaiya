from funcoes import *
from functions.notificar_telegram import *

shaiya_aberto = checar_cor((939, 1061), (251, 239, 185))

if not shaiya_aberto:
    iniciar_shaiya('PedroGeromito')

abrir_leilao()
time.sleep(0.4)
click_ingame((931, 697))

while True:

    if keyboard.is_pressed('F1'):
        print("Encerrando.")
        exit()

    if not leilao_posicao_correta():
        corrigir_leilao()

    atualizar_leilao()

    try:
        
        teste1 = printar_coordenadas((737, 365),(1308, 519))

        nome_1, valor_1, nome_2, valor_2, nome_3, valor_3 = ler_leilao()

        teste2 = printar_coordenadas((737, 365),(1308, 519))
    except:
        print('Erro ao ler leilão.')
        continue
    
    itens = [(nome_3, valor_3, 3), (nome_2, valor_2, 2), (nome_1, valor_1, 1)]

    for nome, valor, indice in itens:
        comprar, valor2, ler_qtd_bolean, qtd = comparar_item(nome, valor, indice)
        if comprar:
            print(f'Autorizada compra de {nome} por {valor}')
            comprou = CONFERIR_E_COMPRAR(nome, valor, indice)
            if not comprou:
                teste3 = printar_coordenadas((737, 365),(1308, 519))
                teste1.save('./teste_antes_da_leitura.png')
                teste2.save('./teste_após_a_leitura.png')
                teste3.save('./teste_após_verificacao.png')
                # exit()
            else:

                if ler_qtd_bolean:
                    g, s, c = valor_para_gold(valor2)

                    try:
                        notificar_via_telegram(f'Item: {nome}\nQuantidade: {qtd}\nValor: {g}🟡 {s}⚪ {c}🟤')
                    except:
                        print('Falha ao notificar')
                        
                else:
                    g, s, c = valor_para_gold(valor)

                    try:
                        notificar_via_telegram(f'Item: {nome}\nValor: {g}🟡 {s}⚪ {c}🟤')
                    except:
                        print('Falha ao notificar')

            continue
    

    if keyboard.is_pressed('F1'):
        print("Encerrando.")
        exit()
