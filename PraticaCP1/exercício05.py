import os
os.system("cls")

n = int(input("Número: "))
if n % 5 != 0:
    n = (n // 5 + 1) * 5
print(n)