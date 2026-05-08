import os
os.system("cls")


print("Digite o nome dos candidatos:")
nome1 = input("1: ")
nome2 = input("2: ")
nome3 = input("3: ")
'''print("Digite o nome dos candidatos:")
nome1 = input("1: ")
nome2 = input("2: ")
nome3 = input("3: ")
if nome1 or nome2 or nome3 == " ":
    print("Nome em branco, digite algo.")'''
    

while True:
    '''qtd_vt_candidato1 = 0
    qtd_vt_candidato2 = 0
    qtd_vt_candidato3 = 0
    cont_nulo = 0'''

    print("CANDIDATOS")
    print(f"\n1 - {nome1}")
    print(f"2 - {nome2}")
    print(f"3 - {nome3}")
    print("0 - FIM DA VOTAÇÃO")
    
    votos = int(input("\nVOTO: "))
    qtd_vt_candidato1 = 0
    qtd_vt_candidato2 = 0
    qtd_vt_candidato3 = 0
    cont_nulo = 0

    total_votos = votos
    match votos:
        case 1:
            qtd_vt_candidato1 += 1
            pct_votos = (qtd_vt_candidato1 * 100) / total_votos
        case 2:
            qtd_vt_candidato2 += 1
            pct_votos = (qtd_vt_candidato2 * 100) / total_votos
        case 3:
            qtd_vt_candidato3 += 1
            pct_votos = (qtd_vt_candidato3 * 100) / total_votos
        case 0:
            print("CANDIDATOS")
            print(f"TOTAIS DE VOTOS: {total_votos}")
            print(f"1 - {nome1} -> {qtd_vt_candidato1} votos -> {pct_votos}")
            print(f"2 - {nome2} -> {qtd_vt_candidato2} votos -> {pct_votos}")
            print(f"3 - {nome3} -> {qtd_vt_candidato3} votos -> {pct_votos}")
            print(f"    NULOS   -> {cont_nulo} votos -> {pct_votos}")
            break
        case _:
            cont_nulo += 1
            pct_votos = (cont_nulo * 100) / total_votos
            
    '''print("CANDIDATOS")
    print(f"TOTAIS DE VOTOS: {total_votos}")
    print(f"1 - {nome1} -> {qtd_vt_candidato} -> {pct_votos}")
    print(f"2 - {nome2} -> {qtd_vt_candidato} -> {pct_votos}")
    print(f"3 - {nome3} -> {qtd_vt_candidato} -> {pct_votos}")
    print(f"    NULOS   -> ")'''