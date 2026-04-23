import os
os.system("cls")

#Nome do usúario
nome = input("Infoeme seu nome completo: ")
#Boas-Vindas ao usúario
print("Boas-Vindas! " + nome + ". A calculadoras de inteiros.")

#Quardar valores
primeiro_valor = input("Informe o primeiro valor: ")
segundo_valor = input("Informe o segundo valor: ")

#Soma dos valores
soma = primeiro_valor + segundo_valor
print("A soma entre os valores é: " + soma)
print(type(primeiro_valor))