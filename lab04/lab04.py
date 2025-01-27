###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome:
# RA:
###################################################

# leitura da sequência de compras e vendas
estoque = unidade = vendas = 0
while True:
    num = int(input())
    if num != 0:
        if num > 0:
            estoque += num
        elif num < 0:
            if estoque > 0:
                if (estoque + num) < 0:
                    unidade = num
                    print(f'Quantidade indisponível para a venda de {unidade * -1} unidades.')
                else:
                    estoque += num
                    vendas +=1
            else:
                unidade = num
                print(f'Quantidade indisponível para a venda de {unidade * -1} unidades.')
    else:
        break
# impressão da saída
print(f'Quantidade de vendas realizadas: {vendas}')
print(f'Quantidade em estoque: {estoque}')