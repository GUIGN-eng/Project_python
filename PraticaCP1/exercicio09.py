import os
os.system("cls")

nota1 = float(input("Nota 1: "))
if nota1 < 0 or nota1 > 10:
    print(f"Nota {nota1} é invalida")
else:
    nota2 = float(input("Nota 2: "))
    if nota2 < 0 or nota2 > 10:
        print(f"Nota {nota2} é invalida")
    else:
     media = (nota1 + nota2) / 2
    if media >= 5:
        print(f"Média {media} - APROVADO")
    else:
        print(f"Média {media} - REPROVADO")