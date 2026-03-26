import os
os.system("cls")

nota = float(input("Nota: "))
if nota > 0 and nota < 10:
    print(f"{nota} é uma nota valida")
else:
    print(f"{nota} é uma nota invalida")