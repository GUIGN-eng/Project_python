import os
os.system("cls")

#Condições bolleanas
logica = True
print(f"A variável contém valor {logica}")

logica = False
print(f"\nAgora a variável contém valor {logica}")

logica = 1 > 2
print(f"\n1 é maior que 2? {logica}")

logica = 1 < 2
print(f"\n1 é menor que 2? {logica}")

logica = 1 >= 2
print(f"\n1 é maio ou igual a 2? {logica}")

logica = 1 <= 2
print(f"\n1 é menor ou igual a 2? {logica}")

logica = 1 == 2
print(f"\n1 é igual a 2? {logica}")

logica = 1 != 2
print(f"\n1 é diferente de 2? {logica}")

logica = bool(0)
print(f"\nO valor de 0 convetido em lógico é {logica}")

logica = bool(15)
print(f"\nO valor de 15 convertido em lógico é {logica}")