import os
os.system("cls")

nome1 = str(input("Digite o nome do host: "))
nome2 = str(input("Digite o nome do subhost: "))
n1 = int(input("Digite a idade do host: "))
n2 = int(input("Digite a idade do subhost: "))
if nome1 != "Guilherme" or nome2 != "Matheus" and n1 < 18 or n2 < 18:
    print("HOSTS NÃO DETECTADOS.....ATIVANDO PROTOCOLO ARMAGEDON")
else:
    print(f"Bem-Vindos {nome1} e {nome2}, Garotos de Programa")
