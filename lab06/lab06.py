##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome:
# RA:
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]
ok = torre
ok.sort()
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
# Impressão da saída
if torre == ok:
    print('Torre estavel')
else:
    print('Torre instavel')