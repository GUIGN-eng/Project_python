import os
os.system("cls")

#Cadastro do usuário 
print("Cadastro de doadores de sangue")
nome_completo = input("Informe seu nome completo: ")
peso_quilograma = float(input("Agora, informe seu peso em quilos: "))
altura_centimetros = int(input("Certo, agora informe sua altura em centímetros: "))
ano_nascimento = int(input("Por ultimo, informe seu ano de nascimento: "))

#Confirmção das informções do usuário
print(f"     NOME: {nome_completo}")
print(f"     PESO: {peso_quilograma}km")
print(f"   ALTURA: {altura_centimetros}cm")
print(f"    IDADE: {ano_nascimento}")

#Analise de validação para a doação de sangue
peso_minimo = peso_quilograma > 50
print(f"TEM PESO MÍNIMO PARA DOAR? {peso_minimo}")

idade = 2026 - ano_nascimento
idade_minima = idade >= 20
print(f"TEM A IDADE MÍNIMA PARA DOAR? {idade_minima}")