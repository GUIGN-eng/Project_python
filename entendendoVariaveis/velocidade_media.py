import os
os.system("cls")

#Boas-Vindas ao usúario
nome = input("Informe seu nome: ")
print("Boas-Vindas! " + nome + ".Ao simulador de bordo")

#Informções do painel do veículo
km = float(input("Informe os quilometros percorridos pelo veículo: "))
viagem_horas = float(input("Informe em quantas horas foi feita a viagem com o veículo: "))

#Calculo da velocidade média
velocidade_media = km / viagem_horas
print(f"A velocidade média do veículo é: {velocidade_media:.2f}")