###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome:
# RA:
###################################################

# Leitura de dados
d1 = int(input(""))
v1 = int(input(""))
t = int(input(""))
d2 = int(input(""))
v2 = int(input(""))
# Cálculo do tempo total gasto por cada espaçonave
space = d1 / v1
blue = d2 / (v2 * t)

if space < blue:
    chegou = True
else:
    chegou = False
# Impressão da resposta
print(chegou)