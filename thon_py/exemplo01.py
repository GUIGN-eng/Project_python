#Corrigir

nome1 = str(input("Digite seu nome: "))
nome2 = str(input("Digte seu nome: "))
n1 = int(input("Digite sua idade: "))
n2 = int(input("Digite sua idade: "))
if (nome1 != "Guilherme" and nome2 != "Matheus") or (n1 < 18 and n2 < 18):
 if (nome1 == "Guilherme" and nome2 != "Matheus") or (n1 >= 18 or n2 < 18):
  if (nome1 != "Guilherme" and nome2 == "Matheus") or (n1 < 18 or n2 >= 18):
         print("\033[36;01mNOME E IDADE NÃO RECONHECIDO PROTOCOLO DE SEGURANÇA ATIVADO\033[M")
elif(nome1 == "Guilherme" and nome2 == "Matheus") and (n1 >= 18 and n2 >= 18):
    print("USUARIOS RECONHECIDOS. BEM-VINDOS BIG BROTHERS")