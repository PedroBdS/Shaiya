from funcoes import *


while True:

    atualizar_leilao()

    teste1 = printar_coordenadas((737, 365),(1308, 519))

    nome_1, valor_1, nome_2, valor_2, nome_3, valor_3 = ler_leilao()

    teste2 = printar_coordenadas((737, 365),(1308, 519))

    itens = [(nome_3, valor_3, 3), (nome_2, valor_2, 2), (nome_1, valor_1, 1)]
    for nome, valor, indice in itens:
        comprar = comparar_item(nome, valor, indice)

        print(f'Autorizada compra de {nome} por {valor}')
        if not conferir_e_NAO_comprar(nome, valor, indice):
            teste3 = printar_coordenadas((737, 365),(1308, 519))
            teste1.save('./teste_antes_da_leitura.png')
            teste2.save('./teste_após_a_leitura.png')
            teste3.save('./teste_após_verificacao.png')
            break

        g, s, c = valor_para_gold(valor)
        print(f'\nItem {indice}: {nome}')
        print(f'Valor: {g}g  {s}s  {c}c\n\n')
        # notificar_via_telegram(f'Item: {nome}\nValor: {g}g {s}s {c}c')
