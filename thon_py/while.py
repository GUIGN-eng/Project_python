import os
os.system("cls")

'''
Exemplo: Forçar o usuário à digitar im número.

Execução 1:
Número: 6
Digitou o número 6

Execução 2:
Número: ABC
Erro! Digite um número
Número: &
Erro! Digite um número



'''



while True:
    n = input("Número: ")
    if not n.isnumeric():
        print("Erro! Não digitou um número")
        continue
    else:
        break
    
n = int(n)
    
print(f"Dobro: {n + n}")

'''n = input("Número: ")

while not n.isnumeric():
    print("Erro! Não digitou um número")
    n = input("Número: ")
else:
    n = int(n)
    
print(f"Dobro: {n + n}")'''


'''n = input("Número: ")
if n.isnumeric():
    print(f"{n} é um número")
else:
    print(f"{n} não é um número")'''

'''valor = "34"
print(valor.isnumeric())

valor = "ABC"
print(valor.isnumeric())'''

'''n = int(input("Número: "))
print(n, type(n))'''