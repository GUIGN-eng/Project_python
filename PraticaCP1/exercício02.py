import os
os.system("cls")

idade = int(input("Idade: "))
if idade >= 18:
    print(f"Você tem {idade} anos. Maior de idade.")
else:
    print(f"Você tem {idade} anos. Menor de idade")