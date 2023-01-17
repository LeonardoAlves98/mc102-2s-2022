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
                    print(f'Quantidade indiponível para a venda {unidade} unidades.')
                else:
                    estoque += num
                    vendas +=1
            else:
                unidade = num
                print(f'Quantidade indiponível para a venda {unidade} unidades.')
    else:
        break
# impressão da saída
print(f'Quantidade de vendas realizdas: {vendas}')
print(f'Quantidade do estoque: {estoque}')