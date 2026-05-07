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
'''while True:
    n = int(input("Digite um número: "))
    if n == 10:
        print("Parabéns Você Acertou!")
        break
    if n >= 1 and n <= 5:
        print("Não está proximo!")
    elif n >= 6 and n <= 8:
        print("Está proximo!")
    elif n == 9:
        print("Falta só mais um")
    else:
        print("Passou longe!")'''

#7.
'''login_correto = "Host"
senha_correta = "1234"

tentativas = 0

while tentativas < 3:
    login = input("Imforme seu login: ")
    senha = input("Imforme sua senha: ")
    if login == login_correto and senha == senha_correta:
        print("Login e Senha validos. Bem-Vindo!")
        break
    else:
        tentativas += 1
        print("Login e senha invalidos!")
if tentativas == 3:
    print("Limite de tentativas alcançado.")'''

#8.
saldo = 5000
while True:
    print('''
       1-Sacar
       2-Depositar
       3-Consultar saldo
       Exit-Sair
    ''')
    opcao = input("\nDigite uma das opções: ").title()
    match opcao:
        case "1":
            print("\nQuanto gostaria de sacar?")
            sacar = float(input("Saque: R$"))
            if sacar > 0:
                if sacar <= saldo:
                    saldo -= sacar
                else:
                    print("\nSaldo invalido!")
            else:
                print("\nO valor tem que ser maior que 0")
        case "2":
            print("\nQuanto gostaria de depositar?")
            depositar = float(input("Deposito: R$"))
            if depositar > 0:
                saldo += depositar
                print(f"\nSeu deposito no valor de R${depositar} foi realizado com sucesso!")
            else:
                print("\nO valor tem que ser maior que 0")
        case "3":
            print(f"\nSeu Saldo é de: R${saldo}")
        case "Exit":
            break
        case _:
            print("\nOpção digitada invalido. Por favor digite de 1 a 3 ou Exit")
