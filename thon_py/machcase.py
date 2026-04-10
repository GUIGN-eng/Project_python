# Etrututa de seleção: match case
# comparações equivalentes
dia = int(input("Número: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sabado")
    case _:
        print("ERRO, Digite um número de 1 a 7")