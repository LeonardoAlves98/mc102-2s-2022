##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome:
# RA:
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]

# Leitura e processamento dos movimentos
l = []
while True:
    m = int(input())
    count = 0
    l.clear
    if m > 0:
        l = torre[:m]
        l.reverse()
        for x in l:
            torre[count] = x
            count += 1
    else:
        break
next = 1
for x in range(len(torre)-1):
    if x < torre[next]:
        next +=1
# Impressão da saída
if next == len(torre):
    print('Torre estavel')
else:
    print('Torre instavel')