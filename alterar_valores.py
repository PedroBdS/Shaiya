from functions.abrir_shaiya import *
from functions.funcoes import *
from functions.notificar_telegram import *
from functions.comprar_item import *
import tkinter as tk
from tkinter import messagebox
from functions.funcoes import *
from PIL import Image, ImageTk

def ver_qtd():
    img_qtd = capturar_tela((770, 394), (788, 402))
    img_qtd = filtrar_cor(img_qtd)

    img_qtd.show()

def analise_de_item():
    def a(indice):
        nome = ler_nome(indice)
        ValorT = ler_valor(indice)
        g1, s1, c1 = valor_para_gold(ValorT)
        qtd = ler_qtd(indice)
        valorU = int(ValorT/qtd)
        g, s, c = valor_para_gold(valorU)

        print(f'')
        print(f'Item {indice}: {nome}')
        print(f'Quantidade: {qtd}')
        print(f'Valor unitário:  {g}g  {s}s  {c}c')

    itens = [1, 2, 3, 4, 5, 6, 7]
    os.system('cls')
    for item in itens:
        a(item)

def rgb_to_hex(r, g, b):
    return '#%02x%02x%02x' % (r, g, b)

rgb_color = (12, 22, 34)  # Vermelho claro
hex_color = rgb_to_hex(*rgb_color)

def atualizar_valor():
    # Lê o novo nome e o valor
    global nome_lido, qtd, label_qtd
    if not leilao_posicao_correta():
        corrigir_leilao()
    nome_lido = ler_nome()
    valor_na_lista, qtd =  procurar_ou_adicionar(nome_lido)
    valor_na_lista = int(valor_na_lista)
    gold, silver, copper = valor_para_gold(valor_na_lista)
    
    # Atualiza o ícone
    img_icone = printar_coordenadas((756, 375), (788, 407))
    icone = ImageTk.PhotoImage(img_icone)
    icone_sla.config(image=icone)  # Atualiza o ícone
    icone_sla.image = icone  # Necessário para o garbage collector não remover a imagem

    # Atualiza o nome e o valor nas labels
    if qtd:
        text_qtd = f'Qtd: SIM'
    else:
        text_qtd = f'Qtd: NÃO'
    label_qtd.config(text=f'{text_qtd}')
    label_nome.config(text=f'{nome_lido}')
    label_valor.config(text=f'{gold}g  {silver}s  {copper}c')

def atualizar_qtd():
    global qtd, label_qtd
    if qtd:
        atualizar_qtd_csv(nome_lido, False)
    else:
        atualizar_qtd_csv(nome_lido, True)
    
    valor_na_lista, qtd =  procurar_ou_adicionar(nome_lido)
    valor_na_lista = int(valor_na_lista)

    if qtd:
        text_qtd = f'Qtd: SIM'
    else:
        text_qtd = f'Qtd: NÃO'
    label_qtd.config(text=f'{text_qtd}')
    
# Função para confirmar a alteração do valor
def confirmar_alteracao(event=None):
    try:
        # Obtém os valores das moedas digitados pelo usuário
        valor_moedas = entry_valor.get()
        gold_novo, silver_novo, copper_novo = map(int, valor_moedas.split())
        valor_novo = gold_para_valor(gold_novo, silver_novo, copper_novo)

        # Atualiza o valor no CSV ou em algum banco de dados
        atualizar_valor_csv(nome_lido, valor_novo)

        # Atualiza os itens na interface principal
        atualizar_valor()

        # Fecha apenas a janela de alteração (janela_alteracao)
        janela_alteracao.destroy()

    except Exception as e:
        # Exibe uma mensagem de erro caso ocorra um problema
        messagebox.showerror("Erro", f"Erro ao alterar valor: {e}")

# Função para abrir a janela de alteração
def abrir_janela_alteracao():
    global entry_valor
    global janela_alteracao

    janela_alteracao = tk.Toplevel(root)
    janela_alteracao.resizable(False, False)
    janela_alteracao.title("Alterar Valor")
    janela_alteracao.geometry("400x220+-470+380")  # Janela de 400x300 posicionada 500px à direita e 200px para baixo

    imagem = Image.open("./arquivos_tkinter/fundo2.png")  # Use o caminho da sua imagem
    imagem_fundo = ImageTk.PhotoImage(imagem)
    
    # Cria um Label para a imagem de fundo e mantém uma referência
    label_fundo = tk.Label(janela_alteracao, image=imagem_fundo)
    label_fundo.image = imagem_fundo  # Mantém a referência à imagem
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    label_instrucoes = tk.Label(janela_alteracao, text="Digite o valor em ouro, prata e cobre", font=("Arial", 10), bg=hex_color, fg="white")
    label_instrucoes.pack(pady=10)

    entry_valor = tk.Entry(janela_alteracao)
    entry_valor.pack(pady=5)

    # Aqui é onde a janela de alteração é passada como argumento para a função confirmar_alteracao
    btn_confirmar = tk.Button(janela_alteracao, text="Confirmar", command=lambda: confirmar_alteracao(janela_alteracao))
    janela_alteracao.bind('<Return>', confirmar_alteracao)

    btn_confirmar.pack(pady=10)

# Função principal para iniciar o processo

def iniciar_processo():
    global nome_lido, root, icone_sla, label_nome, label_valor, qtd, label_qtd

    nome_lido = ler_nome()
    valor_na_lista, qtd =  procurar_ou_adicionar(nome_lido)
    valor_na_lista = int(valor_na_lista)
    gold, silver, copper = valor_para_gold(valor_na_lista)

    root = tk.Tk()
    root.iconbitmap("./arquivos_tkinter/shaiya.ico")
    root.title("Alteração de Valor")
    root.resizable(False, False)
    root.geometry("400x220+-470+380")  # Janela de 400x220 posicionada 470px à esquerda e 380px para baixo

    imagem = Image.open("./arquivos_tkinter/fundo.png")  # Use o caminho da sua imagem
    imagem_fundo = ImageTk.PhotoImage(imagem)
    
    label_fundo = tk.Label(root, image=imagem_fundo)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    img_icone = printar_coordenadas((756, 375), (788, 407))
    icone = ImageTk.PhotoImage(img_icone)

    icone_sla = tk.Label(root, image=icone)
    icone_sla.place(x=27, y=38)

    label_nome = tk.Label(root, text=f'{nome_lido}', font=("Arial", 10, "bold"), bg=hex_color, fg="white")
    label_nome.place(x=72, y=31)

    if qtd:
        label_qtd = tk.Label(root, text=f'Qtd: SIM', font=("Arial", 10, "bold"), bg=hex_color, fg="white")
        label_qtd.place(x=200, y=55)
    else:
        label_qtd = tk.Label(root, text=f'Qtd: NÃO', font=("Arial", 10, "bold"), bg=hex_color, fg="white")
        label_qtd.place(x=200, y=55)

    label_valor = tk.Label(root, text=f'{gold}g  {silver}s  {copper}c', font=("Arial", 10), bg=hex_color, fg="white")
    label_valor.place(x=72, y=55)

    btn_alterar = tk.Button(root, text="ALTERAR VALOR", font=("Arial", 9, "bold"), command=abrir_janela_alteracao, bg='darkgray')
    btn_alterar.place(x=27, y=170)

    btn_qtr = tk.Button(root, text=" Alterar ", font=("Arial", 8), command=atualizar_qtd, bg='darkgray')
    btn_qtr.place(x=270, y=55)

    verificar_qtr = tk.Button(root, text="Análise", font=("Arial", 8), command=ver_qtd, bg='darkgray')
    verificar_qtr.place(x=270, y=80)

    avaliar_leilao = tk.Button(root, text="Avaliar leilao", font=("Arial", 8), command=analise_de_item, bg='darkgray')
    avaliar_leilao.place(x=27, y=140)

    btn_reiniciar = tk.Button(root, text="Atualizar item", font=("Arial", 8), command=atualizar_valor, bg='darkgray')
    btn_reiniciar.place(x=27, y=83)

    root.mainloop()

iniciar_processo()
# cor de fundo 12, 22, 34

# COORDENADAS DO ICONE NO LEILÃO: (756, 375), (788, 407)