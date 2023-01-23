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
horas_extras = 0
horas_trabalhadas = 0
for c in range(D):
    periodo = int(input())
    total_dia = 0
    for c in range(periodo):
        hora_inicio = int(input())
        hora_final = int(input())
        total_dia += (hora_final - hora_inicio )
        horas_trabalhadas += (hora_final - hora_inicio)
if total_dia > 8:
    horas_extras += (total_dia - 8)
    
# Calculo do valor devido ao funcionário
if (horas_trabalhadas - horas_extras)> 44:
    horas_extras += ((horas_trabalhadas - 44)- horas_extras)
valor = (horas_trabalhadas * V) + (V/2 * horas_extras)
# Impressão da saída
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))
