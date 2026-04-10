n = float(input("Digite um valor: "))
nome = str(input("Informe seu nome completo: "))
if n >= 5 and n <= 10:
    if n == 100:
        if nome != "Guilherme":
            print("ERRO USUARIO NÃO RECONHECIDO")

elif n <= 5 or n >= 10:
    if n == 2021:
        if nome == "Guilherme":
            print("USUARIO RECONHECIDO. ACEPTED")