from functions.ler_leilao import *
import pyautogui
import time
import keyboard
from PIL import ImageGrab, Image
import numpy as np
import pytesseract
import csv
import os

lista_csv = '/.lista_nova.csv'

def click_ingame(coordenada, delay=0):

    pyautogui.moveTo(coordenada)
    pyautogui.mouseDown()

    pyautogui.moveTo(coordenada)

    pyautogui.moveTo(coordenada)

    pyautogui.mouseUp()
    
    time.sleep(delay)

def leilao_posicao_correta():
    if not checar_cor((596, 248), (3, 2, 2)):
        # print('Leilão fechado ou fora de posição.')
        return False

    if not checar_cor((596, 845), (70, 70, 71)):
        # print('Leilão fechado ou fora de posição.')
        return False

    if not checar_cor((965, 254), (255, 255, 255)):
        # print('Leilão fechado ou fora de posição.')
        return False   

    if not checar_cor((1335, 847), (56, 56, 55)):
        # print('Leilão fechado ou fora de posição.')
        return False
    if not checar_cor((595, 259), (9, 9, 9)):
        # print('Leilão fechado ou fora de posição.')
        return False
    return True

def esperar_cor_e_clicar(coordenada, cor=False, delay=0, ingame=True, nome=False):

    nome = False

    pyautogui.moveTo(coordenada)
    if not ingame:
        while True:
            if not cor:
                time.sleep(delay)
                pyautogui.click(coordenada)
                break
            if ImageGrab.grab().getpixel((coordenada)) == (cor):
                time.sleep(delay)
                pyautogui.click(coordenada, duration=delay)
                break
            if nome != False:
                print(f'esperando cor {nome}')
        return

    if ingame:
        while True:
            if not cor:
                time.sleep(delay)
                click_ingame(coordenada)
                break
            if ImageGrab.grab().getpixel((coordenada)) == (cor):
                time.sleep(delay)
                click_ingame(coordenada, delay=delay)
                break
            if nome != False:
                print(f'esperando cor {nome}')
        return

def esperar_cor(coordenada, cor, nome=False):
    nome = False
    while True:
        if ImageGrab.grab().getpixel((coordenada)) == (cor):
            break
        if nome != False:
            print(f'esperando cor {nome}')

def checar_cor(coordenada, cor):
    if ImageGrab.grab().getpixel((coordenada)) == (cor):
        return True
    else:
        return False

def comparar_img(img1, img2):
    
    img_array1 = np.array(img1)
    img_array2 = np.array(img2)
    
    return np.array_equal(img_array1, img_array2)

def printar_coordenadas(cord1, cord2):

    x1, y1 = cord1
    x2, y2 = cord2
    
    top = min(y1, y2)
    left = min(x1, x2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    return screenshot

def capturar_tela(coordenada1, coordenada2, arquivo_saida=False):
    # Obter as coordenadas de referência
    x1, y1 = coordenada1
    x2, y2 = coordenada2
    
    # Definir a área de captura (top, left, width, height)
    top = min(y1, y2)
    left = min(x1, x2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    # Capturar a área da tela
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    
    if not arquivo_saida:
        return screenshot
    
    # Salvar a captura de tela em PNG
    screenshot.save(arquivo_saida)
    

    print(f"Imagem salva como {arquivo_saida}")

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

def procurar_ou_adicionar(nome_item):
    caminho_csv = './lista.csv'
    # Verifica se o arquivo CSV existe
    item_encontrado = False
    novo_dados = []
    conversion = {'True': True, 'False': False}

    # Lê o arquivo CSV
    if os.path.exists(caminho_csv):
        with open(caminho_csv, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            # Ignora o cabeçalho
            cabecalho = next(leitor)
            for linha in leitor:
                item, valor, qtd = linha
                novo_dados.append([item, valor, qtd])
                if item == nome_item:
                    item_encontrado = True
    
    if item_encontrado:
        # Retorna o valor do item encontrado
        for item, valor, qtd in novo_dados:
            if item == nome_item:
                return float(valor), conversion.get(qtd)  # Converte o valor para float
    
    # Se o item não foi encontrado, adiciona ao novo_dados com valor 0
    novo_dados.append([nome_item, 0, 'False'])

    # Salva os dados de volta no arquivo CSV
    with open(caminho_csv, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Itens', 'Valor', 'qtd'])  # Escreve o cabeçalho
        escritor.writerows(novo_dados)  # Escreve todos os dados

    return novo_dados[1], conversion.get(novo_dados[2])

def atualizar_valor_csv(nome_item, novo_valor):
    caminho_csv = './lista.csv'
    item_encontrado = False
    novo_dados = []

    with open(caminho_csv, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)  # Lê o cabeçalho

        # Adiciona o cabeçalho aos novos dados
        novo_dados.append(cabecalho)

        for linha in leitor:
            item, valor, qtd = linha
            if item == nome_item:
                # Se o item for encontrado, atualiza o valor
                novo_dados.append([item, novo_valor, qtd])
                item_encontrado = True
            else:
                # Mantém o valor original dos outros itens
                novo_dados.append([item, valor, qtd])

    # Reescreve o CSV com os dados atualizados
    with open(caminho_csv, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(novo_dados)

    if not item_encontrado:
        print(f"Item '{nome_item}' não encontrado no arquivo.")

def atualizar_qtd_csv(nome_item, nova_qtd):
    caminho_csv = './lista.csv'
    item_encontrado = False
    novo_dados = []

    with open(caminho_csv, mode='r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)  # Lê o cabeçalho

        # Adiciona o cabeçalho aos novos dados
        novo_dados.append(cabecalho)

        for linha in leitor:
            item, valor, qtd = linha
            if item == nome_item:
                # Se o item for encontrado, atualiza o valor
                novo_dados.append([item, valor, str(nova_qtd)])
                item_encontrado = True
            else:
                # Mantém o valor original dos outros itens
                novo_dados.append([item, valor, qtd])

    # Reescreve o CSV com os dados atualizados
    with open(caminho_csv, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(novo_dados)

    if not item_encontrado:
        print(f"Item '{nome_item}' não encontrado no arquivo.")
    
def abrir_leilao():
    click_ingame((1422, 1036))
    time.sleep(0.3)
    click_ingame((1250, 312))
       
    if not(checar_cor((595, 246), (73, 73, 72)) and checar_cor((597, 249), (35, 34, 36))):
        return False

def imagens_iguais(imagem1, imagem2):
    
    # Verificar se as dimensões são iguais
    if imagem1.size != imagem2.size:
        return False
    
    # Converter as imagens para arrays de NumPy
    imagem1_array = np.array(imagem1)
    imagem2_array = np.array(imagem2)
    
    # Comparar os arrays (que correspondem aos pixels)
    return np.array_equal(imagem1_array, imagem2_array)

def _corrigir_leilao():
    try:
        # Tenta localizar a imagem na tela
        localizacao = pyautogui.locateOnScreen('./images/leilao.png', confidence=0.8)
        
        if localizacao:
            if localizacao.left == 658 and localizacao.top == 378:
                return True
            else:
                pyautogui.mouseDown(localizacao.left, localizacao.top-50)
                pyautogui.moveTo(658, 328)
                pyautogui.mouseUp(658, 328)

                # if not leilao_posicao_correta():
                #     return False
                return True
        else:
            abrir_leilao()
            if not leilao_posicao_correta():
                return False
            return True

    except pyautogui.ImageNotFoundException:
        abrir_leilao()
    if not leilao_posicao_correta():
            return False
    return True

def corrigir_leilao():
    # if leilao_posicao_correta():
    if not _corrigir_leilao():
        if not _corrigir_leilao():
            print('não foi possível abrir o leilão corretamente')
            return False
        else:
            return True
    else:
        return True

def atualizar_leilao(delay=0):

    nome_antigo = capturar_tela((808, 380), (1025, 383))
    valor_antigo = capturar_tela((1176, 400), (1287, 403))

    while True:

        click_ingame((1250, 312))

        time.sleep(delay)

        nome_novo = capturar_tela((808, 380), (1025, 383))

        if not imagens_iguais(nome_antigo, nome_novo):
            return

        valor_novo = capturar_tela((1176, 400), (1287, 403))

        if not imagens_iguais(valor_antigo, valor_novo):
            return
        
        if keyboard.is_pressed('F1'):
            print("Encerrando.")
            exit()
