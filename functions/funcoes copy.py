import pyautogui
import time
import keyboard
from PIL import ImageGrab, Image
import numpy as np
import pytesseract
import csv
import os

lista_csv = '/.lista_nova.csv'

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

matriz_mestre = [
    (0,0,1,0,0,0,0,0),
    (0,1,0,0,0,0,0,1),
    (0,1,0,0,0,0,1,0),
    (0,0,0,0,1,1,0,0),
    (0,0,1,1,0,0,1,0),
    (0,1,1,1,1,1,1,0),
    (1,0,0,0,0,0,0,0),
    (0,1,1,0,1,1,1,0),
    (0,1,1,1,0,0,1,0)
]

cores_predefinidas = [
    (255, 255, 255),
    (255, 255, 0),
    (255, 128, 0),
    (255, 0, 255),
    (128, 255, 255),
    (128, 0, 255),
    (0, 255, 64),
    (0, 128, 255)
    ]

def adiciona_coluna_zerada(matriz):
    # Cria uma coluna de zeros com o mesmo número de linhas da matriz original
    coluna_zeros = np.zeros((matriz.shape[0], 1), dtype=int)
    # Concatena a coluna de zeros à esquerda da matriz original
    return np.hstack((coluna_zeros, matriz))

def click_ingame(coordenada, delay=0):

    pyautogui.moveTo(coordenada)
    pyautogui.mouseDown()

    pyautogui.moveTo(coordenada)

    pyautogui.moveTo(coordenada)

    pyautogui.mouseUp()
    
    time.sleep(delay)

def matriz_para_tuplas(matriz):
    return [tuple(int(valor) for valor in linha) for linha in matriz]

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
    
    # Verificar se as dimensões são diferentes
    # if imagem1.size != imagem2.size:
    #     return False
    
    # Converter as imagens para arrays NumPy para comparar pixel a pixel
    img_array1 = np.array(img1)
    img_array2 = np.array(img2)
    
    # Verificar se os arrays são idênticos
    return np.array_equal(img_array1, img_array2)

def printar_coordenadas(cord1, cord2):
    # Obter as coordenadas de referência
    x1, y1 = cord1
    x2, y2 = cord2
    
    # Definir a área de captura (top, left, width, height)
    top = min(y1, y2)
    left = min(x1, x2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    # Capturar a área da tela
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    return screenshot

def identificar_erros():
    tela_img = printar_coordenadas((854, 461), (895, 493))

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
    pyautogui.write('Bolinho123321!')

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

def cor_do_nome(imagem):

    pixels = list(imagem.getdata())
    for pixel in pixels:
        if pixel in cores_predefinidas:
            return pixel
    
    print(f'Falha ao identificar a cor do nome.')
    return (0, 0, 0)

def checar_novo_item():

    # novo_nome = ler_nome()
    novo_valor = ler_valor()

def filtrar_cor(image, cor_rgb=False):

    if not cor_rgb:
        cor_rgb = (255, 255, 255)

    img = image.convert('RGB')  # Garantir que a imagem está no formato RGB
    
    # Criar uma nova imagem vazia (preta e branca)
    nova_img = Image.new('L', img.size)
    pixels = nova_img.load()

    # Obter os dados da imagem original
    img_pixels = img.load()

    # Percorrer todos os pixels
    for i in range(img.size[0]):  # Largura
        for j in range(img.size[1]):  # Altura
            # Se o pixel for da cor informada, pintá-lo de branco (255), senão preto (0)
            if img_pixels[i, j] == cor_rgb:
                pixels[i, j] = 255  # Branco
            else:
                pixels[i, j] = 0    # Preto

    return nova_img

def printar_preco():
    valor = capturar_tela((1182, 398), (1287, 406))
    valor_formatado = filtrar_cor(valor, (255,255,255))
    return valor_formatado

def process_matrix(matriz):
    matriz1 = remove_duplicated_zero_columns(matriz)
    matriz2 = adiciona_coluna_zerada(matriz1)
    return colunas_direita_de_zeros(matriz2)

def remove_duplicated_zero_columns(matrix):
    # Convertemos a lista para um array numpy para facilitar a manipulação
    matrix = np.array(matrix)
    
    # Identificamos colunas com apenas zeros
    zero_columns = np.all(matrix == 0, axis=0)
    
    # Inicializamos a nova matriz de saída
    result_matrix = []
    
    # Percorremos as colunas da matriz original
    last_was_zero = False
    for i in range(matrix.shape[1]):
        if zero_columns[i]:
            if not last_was_zero:
                result_matrix.append(matrix[:, i])  # Mantemos a primeira coluna zerada
            last_was_zero = True  # Marcamos que a coluna anterior foi de zeros
        else:
            result_matrix.append(matrix[:, i])  # Mantemos colunas não zeradas
            last_was_zero = False  # Resetamos o marcador
    
    # Convertemos a lista de colunas de volta para uma matriz
    result_matrix = np.column_stack(result_matrix)
    
    return result_matrix

def colunas_direita_de_zeros(matriz):
    # Identificar as colunas que estão completamente zeradas
    colunas_zeradas = [i for i in range(matriz.shape[1]) if np.all(matriz[:, i] == 0)]
    
    # Inicializar uma lista para armazenar as colunas selecionadas
    colunas_selecionadas = []
    
    # Iterar pelas colunas zeradas
    for col in colunas_zeradas:
        # Verificar se existem ao menos duas colunas à direita
        if col + 2 < matriz.shape[1]:
            # Adicionar as duas colunas à direita da coluna zerada
            colunas_selecionadas.append(matriz[:, col + 1])
            colunas_selecionadas.append(matriz[:, col + 2])
    
    # Concatenar as colunas selecionadas em uma nova matriz
    nova_matriz = np.column_stack(colunas_selecionadas)
    
    return nova_matriz

def ler_matrizes_preco(matriz):

    indices_iguais = []

    matriz = matriz.T
    tuplas = matriz_mestre
    for index, tupla in enumerate(tuplas):
        for i in range(1, 8, 2):  # linhas ímpares (1, 3, 5, 7)
            if all(matriz[i][j] == tupla[j] for j in range(8)):
                indices_iguais.append(index)
                break  # Se encontrar um igual, não precisa verificar as outras linhas
    
    return indices_iguais

def separa_matriz(matriz):
    # Converte a matriz para um array NumPy (caso ainda não seja)
    matriz = np.array(matriz)
    
    # Verifica se o número de colunas é par
    if matriz.shape[1] % 2 != 0:
        raise ValueError("O número de colunas deve ser par")
    
    # Seleciona as colunas ímpares (índices 0, 2, 4, ...)
    colunas_impares = matriz[:, ::2]
    
    # Seleciona as colunas pares (índices 1, 3, 5, ...)
    colunas_pares = matriz[:, 1::2]
    
    return matriz_para_tuplas([tuple(linha) for linha in colunas_impares.T]), matriz_para_tuplas([tuple(linha) for linha in colunas_pares.T])

def converte_para_numero(matriz_impar, matriz_par):
    resposta = ''
    i = 0
    for numero in matriz_impar:
        for num in matriz_mestre:
            if numero == num:
                if numero == (0,1,1,1,1,1,1,0):
                    if matriz_par[i][3]==1:
                        resposta= resposta+str(6)
                        break
                    else:
                        resposta= resposta+str(0)
                        break
                resposta= resposta+str(matriz_mestre.index(num)+1)
                break
        i += 1
    try:
        a = int(resposta)
        return a
    except:
        return False
                 
def gold_para_valor(gold, silver, copper):
    if gold > 9999:
        print(f'Gold: {gold}')
        print('deu ruim pra converter Gold pra valor')
    if silver > 9999:
        print(f'Silver: {silver}')    
        print('deu ruim pra converter Silver pra valor')
    if copper > 99999:
        print(f'Copper: {copper}')
        print('deu ruim pra converter Copper pra valor')

    return gold*1000000000 + silver*100000 + copper

def extrair_texto_imagem(imagem):

    # Usa o pytesseract para extrair o texto
    texto = pytesseract.image_to_string(imagem).strip()  # Remove quebras de linha e espaços extras
    return texto



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

def conferir_e_NAO_comprar(nome, valor,indice=1):

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

    print('iniciando a compra... (fake)')
    print('COMPRA EFETUADA!!! (fake)')
    return True

def valor_para_gold(valor):

    # print(f'valor: {valor}')

    valor_str = str(valor).zfill(13)
    
    moedas_ouro = int(valor_str[:4])
    # print(f'moedas_ouro: {moedas_ouro}')
    moedas_prata = int(valor_str[4:8])
    # print(f'moedas_prata: {moedas_prata}')
    moedas_cobre = int(valor_str[8:])
    # print(f'moedas_cobre: {moedas_cobre}')   

    return moedas_ouro, moedas_prata, moedas_cobre

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

def imagem_esta_totalmente_preta(imagem):
    
    # Converte a imagem para um array NumPy
    imagem_array = np.array(imagem)
    
    # Verifica se todos os pixels são pretos
    return np.all(imagem_array == 0)

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

def matriz_zerada(matriz):
    # Verifica se todos os elementos da matriz são iguais a 0
    for linha in matriz:
        for elemento in linha:
            if elemento != 0:
                return False
    return True

def ler_qtd(indice):

    y1 = 394 + (indice-1)*51
    y2 = 402 + (indice-1)*51

    qtd_print = printar_coordenadas((770, y1), (788, y2))
    qtd_print = filtrar_cor(qtd_print, (255, 255, 255))
    qtd_print = qtd_print.convert('1')
    matriz = np.array(qtd_print, dtype=int)
    if matriz_zerada(matriz):
        return 1
    matriz = remove_duplicated_zero_columns(matriz)
    matriz = colunas_direita_de_zeros(matriz)

    matriz1, matriz2 = separa_matriz(matriz)
    qtd = converte_para_numero(matriz1, matriz2)
    if qtd > 255:
        qtd = 1
    return qtd

def ler_valor(indice=1, imagem=False):

    if not leilao_posicao_correta():
        return False

    y1 = 398 + (indice-1)*51
    y2 = 406 + (indice-1)*51

    if not imagem:
        imagem = capturar_tela((1176, y1), (1287, y2))

    imagem = filtrar_cor(imagem, (255,255,255))
    imagem = imagem.convert('1')   
    matriz = np.array(imagem, dtype=int)
    
    # matriz1 = remover_primeiras_colunas_zeradas(matriz)
    for i in range(matriz.shape[1]):
        if np.any(matriz[:, i] == 1):
            matriz1 = matriz[:, i:]
            break

    # m_gold, matriz3 = quebrar_na_primeira_sequencia_zerada(matriz1)
    n_colunas = matriz1.shape[1]
    for i in range(n_colunas - 3):
        # Verificar se as 4 colunas consecutivas a partir da i-ésima são todas zeradas
        if np.all(matriz1[:, i] == 0) and np.all(matriz1[:, i+1] == 0) and np.all(matriz1[:, i+2] == 0) and np.all(matriz1[:, i+3] == 0):
            # Parte esquerda: até a coluna imediatamente antes da sequência zerada
            m_gold = matriz1[:, :i]

            # Parte direita: da coluna após a sequência zerada até o final
            matriz3 = matriz1[:, i+4:]
            break

    # matriz4 = remover_primeiras_colunas_zeradas(matriz3)
    for i in range(matriz3.shape[1]):
        # Verificar se a coluna atual é toda composta por zeros
        if np.any(matriz3[:, i] == 1):
            matriz4 = matriz3[:, i:]
            break
        
    # m_silver, matriz5 = quebrar_na_primeira_sequencia_zerada(matriz4)
    n_colunas = matriz4.shape[1]
    for i in range(n_colunas - 3):
        # Verificar se as 4 colunas consecutivas a partir da i-ésima são todas zeradas
        if np.all(matriz4[:, i] == 0) and np.all(matriz4[:, i+1] == 0) and np.all(matriz4[:, i+2] == 0) and np.all(matriz4[:, i+3] == 0):
            # Parte esquerda: até a coluna imediatamente antes da sequência zerada
            m_silver = matriz4[:, :i]

            # Parte direita: da coluna após a sequência zerada até o final
            matriz5 = matriz4[:, i+4:]
            
            break

    # m_copper = remover_primeiras_colunas_zeradas(matriz5)
    for i in range(matriz5.shape[1]):
        # Verificar se a coluna atual é toda composta por zeros
        if np.any(matriz5[:, i] == 1):
            m_copper = matriz5[:, i:]

            break
    
    # print('\n\n-------- TESTES com as matrizes da OURO ---------\n')
    # print(f'm_silver antes:\n{m_gold}')

    # m_gold = remove_duplicated_zero_columns(m_gold)
    # print(f'\nremove_duplicated_zero_columns:\n{m_gold}')

    # m_gold = adiciona_coluna_zerada(m_gold)
    # print(f'\nadiciona_coluna_zerada:\n{m_gold}')

    # m_gold = colunas_direita_de_zeros(m_gold)
    # print(f'\ncolunas_direita_de_zeros:\n{m_gold}')

    # print('\n\n-------- TESTES com as matrizes da PRATA ---------\n')
    # print(f'm_silver antes:\n{m_silver}')

    # m_silver = remove_duplicated_zero_columns(m_silver)
    # print(f'\nremove_duplicated_zero_columns:\n{m_silver}')

    # m_silver = adiciona_coluna_zerada(m_silver)
    # print(f'\nadiciona_coluna_zerada:\n{m_silver}')

    # m_silver = colunas_direita_de_zeros(m_silver)
    # print(f'\ncolunas_direita_de_zeros:\n{m_silver}')

    # print('\n\n-------- TESTES com as matrizes da COBRE ---------\n')
    # print(f'm_silver antes:\n{m_copper}')

    # m_copper = remove_duplicated_zero_columns(m_copper)
    # print(f'\nremove_duplicated_zero_columns:\n{m_copper}')

    # m_copper = adiciona_coluna_zerada(m_copper)
    # print(f'\nadiciona_coluna_zerada:\n{m_copper}')

    # m_copper = colunas_direita_de_zeros(m_copper)
    # print(f'\ncolunas_direita_de_zeros:\n{m_copper}')

    m_gold = process_matrix(m_gold)

    m_silver = process_matrix(m_silver)

    m_copper = process_matrix(m_copper)

    # print(f'm_copper:\n{m_copper}')
    m_gold_a, m_gold_b = separa_matriz(m_gold)
    # print(f'm_gold_a:\n{m_gold_a}')
    m_silver_a, m_silver_b = separa_matriz(m_silver)
    # print(f'm_silver_a:\n{m_silver_a}')
    m_copper_a, m_copper_b = separa_matriz(m_copper)
    # print(f'm_copper_a:\n{m_copper_a}')
    gold = converte_para_numero(m_gold_a, m_gold_b)
    # print(f'Gold: {gold}')

    silver = converte_para_numero(m_silver_a, m_silver_b)
    # print(f'silver: {silver}')

    copper = converte_para_numero(m_copper_a, m_copper_b)
    # print(f'copper: {copper}')

    if not gold:
        if gold != 0:
            return False
    if not silver:
        if silver != 0:
            return False
    if not copper:
        if copper != 0:
            return False

    valor = gold_para_valor(gold, silver, copper)

    return valor

def ler_nome(indice=1, imagem=False):

    y1 = 376 + (indice-1)*51
    y2 = 390 + (indice-1)*51

    if not imagem:
        imagem = capturar_tela((808, y1), (1025, y2))

    cor_nome = cor_do_nome(imagem)
    img_nome_tratado = filtrar_cor(imagem, cor_nome)

    if imagem_esta_totalmente_preta(img_nome_tratado):
        print('deu ruim pra filtrar a cor do nome')
        return False
    
    try:
        nome = extrair_texto_imagem(img_nome_tratado)
    except:
        nome = False

    if not isinstance(nome, str):
        print('deu ruim pra ler o nome')
        return False
    return nome

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

def ler_leilao(delay= 0.4):
    
    time.sleep(delay)
    
    nome_1 = capturar_tela((808, 376), (1025, 390))
    nome_2 = capturar_tela((808, 427), (1025, 441))
    nome_3 = capturar_tela((808, 478), (1025, 492))
    # nome_4 = capturar_tela((808, 529), (1025, 543))

    valor_1 = capturar_tela((1176, 398), (1287, 406))
    valor_2 = capturar_tela((1176, 449), (1287, 457))
    valor_3 = capturar_tela((1176, 500), (1287, 508))
    # valor_4 = capturar_tela((1176, 551), (1287, 559))

    nome_1 = ler_nome(imagem = nome_1)
    nome_2 = ler_nome(imagem = nome_2)
    nome_3 = ler_nome(imagem = nome_3)
    # nome_4 = ler_nome(imagem = nome_4)

    valor_1 = ler_valor(imagem = valor_1)
    valor_2 = ler_valor(imagem = valor_2)
    valor_3 = ler_valor(imagem = valor_3)
    # valor_4 = ler_valor(imagem = valor_4)

    # print(f'Nome 1: {nome_1}')
    # print(f'Valor 1: {valor_1}\n')
    # print(f'Nome 2: {nome_2}')
    # print(f'Valor 2: {valor_2}\n')
    # print(f'Nome 3: {nome_3}')
    # print(f'Valor 3: {valor_3}\n')

    return nome_1, valor_1, nome_2, valor_2, nome_3, valor_3
    # return nome_1, valor_1, nome_2, valor_2, nome_3, valor_3, nome_4, valor_4
