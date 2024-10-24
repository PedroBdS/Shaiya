from functions.funcoes import *
from functions.ler_leilao import *


def comparar_item(nome, valor, indice=1):
    
    if nome == '':
        return False, 0, False, 1
    if valor == False:
        return False, 0, False, 1
    
    conversion = {'True': True, 'False': False}
    with open('lista.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for linha in reader:
            if linha[0] == nome:
                valor_arquivo = float(linha[1])  # Converte o valor para float
                ler_qtd_bolean = conversion.get(linha[2])
                if ler_qtd_bolean:
                    # print(f'qtd: {ler_qtd_bolean}')
                    qtd = ler_qtd(indice)
                    valor = int(valor/qtd)
                else:
                    qtd = 1
                    
                if valor > valor_arquivo:
                    return False, valor, ler_qtd_bolean, qtd
                elif valor < valor_arquivo:
                    return True, valor, ler_qtd_bolean, qtd
                else:
                    return True, valor, ler_qtd_bolean, qtd
    
    with open('lista.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nome, 0, False])  # Adiciona o nome com valor 0
        # print(f'NOVO ITEM ADICIONADO: {nome}')
    return False, 0, False, 1

def CONFERIR_E_COMPRAR(nome, valor, indice=False):

    if not indice:
        indice = 1

    nome_lido = ler_nome(indice)
    valor_lido = ler_valor(indice)

    if nome != nome_lido:
        print('\nERRO DE COMPRA DE ITEM ERRADO!')
        print(f'NOME AUTORIZADO: {nome}')
        print(f'NOME  CONFERIDO: {nome_lido}')
        print(f'VALOR AUTORIZADO: {valor}')
        print(f'VALOR  CONFERIDO: {valor_lido}')

        return False
    if valor != valor_lido:
        print('\nERRO DE COMPRA DE VALOR ERRADO!')
        print(f'VALOR AUTORIZADO: {valor}')
        print(f'VALOR  CONFERIDO: {valor_lido}')

        return False

    print('iniciando a compra...')

    y = 393 + (indice-1)*51

    # Item do indice
    click_ingame((992, y))
    time.sleep(0.25)

    # Comprar Agora
    click_ingame((1060, 818))
    time.sleep(0.25)

    # Entrar
    click_ingame((913, 541))
    time.sleep(0.25)

    print('COMPRA EFETUADA!!!')

    # Entrar
    click_ingame((960, 541))

    # Selecionar o ultimo item novamente
    click_ingame((931, 697))

    return True