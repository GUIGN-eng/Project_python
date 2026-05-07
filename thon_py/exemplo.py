import os
os.system("cls")

nome = input("Informe seu nome completo: ")
ano_nascimento = int(input("Informe o ano em que voçê nasceu: "))

idade = 2026 - ano_nascimento

if nome == "Guilherme" and idade == 21:
    print("GOSTOÃO DO HOST RECONHECIDO")
else:
    print("Deixa de tentar vagabunda, não te conheço" \
    "\nEntão voçê não entra")
