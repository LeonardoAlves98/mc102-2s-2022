##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome:
# RA:
##################################################

# Leitura do valor da hora
V = int(input())

# Leitura do numero de dias trabalhados na semana
D = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia
hora_extra = 0
trabalho_dia = 0
for c in range(D):
    periodo = int(input())
    for c in range(periodo):
        hora_inicio = int(input())
        hora_final = int(input())
        if (hora_final - hora_inicio ) > 8:
            hora_extra += (hora_final - hora_inicio) - 8
        trabalho_dia += hora_final - hora_inicio
# Calculo do valor devido ao funcionário
horas_trabalhadas = trabalho_dia
if trabalho_dia > 44:
    hora_extra += trabalho_dia-44
horas_extras = hora_extra
valor = (horas_trabalhadas * V)+(V/2* horas_extras)
# Impressão da saída
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))
