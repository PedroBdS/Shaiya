from funcoes import *
'''
Autorizada compra de GM Link (NT) por 239000000
Autorizada compra de Espada do Intinito’ por 304500000
Autorizada compra de Runa de Recriagao (INT) por 165000000
Autorizada compra de Martelo de Conexao Divino por 21000

'''
leilao_aberto_1 = 2624999936

gold, prata, cobre = valor_para_gold(leilao_aberto_1)
valor_final = gold_para_valor(gold, prata, cobre)

print(leilao_aberto_1)

print(f'{gold}, {prata}, {cobre}')
