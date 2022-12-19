###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome:
# RA:
###################################################

# leitura de dados

Dia = int(input(': '))
Hora = str(input(': '))
Minuto = str(input(': '))
Estudante = str(input(':'))
Forma_pag = str(input(':'))
# valor do ingresso inteiro
ingresso = 0
sessao = 1829
periodo = Hora + Minuto

if int(periodo) <= sessao:
    if Dia == 1 or Dia == 7:
        ingresso = 30
    elif Dia == 2 or Dia == 3 or Dia == 4:
        ingresso = 15
    elif Dia == 5 or Dia == 6:
        ingresso = 20
else:
    int(periodo) >= sessao
    if Dia == 1 or Dia == 4 or Dia == 5:
        ingresso = 30
    elif Dia == 2 or Dia == 3:
        ingresso = 20
    elif Dia == 6 or Dia == 7:
        ingresso = 40

# valor a pagar
if Estudante == 'N' and  Forma_pag == 'C':
    if int(periodo) <= sessao:
        if Dia == 1:
            ingresso = ingresso * 0.7
        elif Dia == 2 or Dia == 3 or Dia == 4 or Dia == 5 or Dia == 6:
            ingresso = ingresso * 0.5
        elif Dia == 7:
            ingresso = ingresso * 0.8
    else:
        int(periodo) >= sessao
        if Dia == 1 or Dia == 6:
            ingresso = ingresso * 0.7
        elif Dia == 2 or Dia == 3 or Dia == 4 or Dia == 5:
            ingresso = ingresso * 0.5
        elif Dia == 7:
            ingresso = ingresso * 0.8

elif Estudante == 'S':
    ingresso = ingresso * 0.5
# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))
