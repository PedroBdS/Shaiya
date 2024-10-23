from funcoes import *

# ------ teste pixel branco ------

def ver_qtd():
    img_qtd = capturar_tela((770, 394), (788, 402))
    img_qtd = filtrar_cor(img_qtd)

    img_qtd.show()

ver_qtd()