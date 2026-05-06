import os
os.system("cls")

#1.
'''contador = 1
while contador <= 10:
     print(contador)
     contador += 1'''

#2.
'''n = int(input("Digete um número inteiro: "))
print("Digite zero para se quiser finalizar o loop erevelar a soma dos mesmos!")
soma = 0

while n != 0:
    n = int(input("Digete um número inteiro: "))
    soma += n
print(f"Soma dos números digitados: {soma}")'''

#3.
'''senha = input("Imforme a senha do host: ")

while senha != "HOSTMASTER":
    print("SENHA INCORRETA! PROTOCOLO DE SEGURANÇA ATIVADO.....")
    senha = input("Imforme a senha do host: ")
    if senha == "HOSTMASTER":
        print("HOST ACEITO! Bem-Vindo!")'''

#4.
'''maior = 0
while True:
    n = int(input("Digite um número: "))

    if n == -1:
        break
    
    if n > maior:
        maior = n

print(f"O maior número é {maior}")'''

#5.
'''n = int(input("Digite um número: "))

qtd_pares = 0
qtd_impares = 0

while n != 0:
    n = int(input("Digite um número: "))

    if n % 2 == 0:
         qtd_pares+= 1
    else:
        qtd_impares += 1

#print(f'''
#    Quantidade de positivos: {qtd_pares}
#    Quantidade de negativos: {qtd_impares}
#''')

#6.
while True:
    n = int(input("Digite um número: "))
    if n == 10:
        break
    if n >= 1 and n <= 5:
        print("Não está proximo!")
    elif n >= 6 and n <= 7:
        print("Está proximo")
    elif