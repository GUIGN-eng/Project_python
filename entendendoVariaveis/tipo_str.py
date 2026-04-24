import os
os.system("cls")

#Criação e exibição de uma variável texto com quebra de linha e tabulação
texto = "Este texto quebra de linha \n aqui. porem aqui \t temos uma tabulação"
print(texto)

#O método capitalize() torna a primeira letra do texto em maiúscula
texto = "\ntexto em minusculas AINDA É texto"
print(texto.capitalize())

#O método cont() conta quantas vezes um texto aparece dentro de outro
texto = "\ntexto em minusculas AINDA É texto"
print(texto.count("ex"))

#O método endswith() verifica se um texto termina com determinada sequencia de caracteres
texto = "\ntexto em minusculas AINDA É texto"
print(texto.endswith("!"))

#O método startswith() verifica se um texto inicia com determinada sequencia de caracteres
texto = "\ntexto em minusculas AINDA É texto"
print(texto.startswith("te"))

#Os métodos upper() e lower() tornam um texto maiúsculo ou minúsculo, respectivamente 
texto = "\ntexto em minusculas AINDA É texto"
print(texto.upper())
print(texto.lower())

#O método replace() substitui uma parte do texto
texto = "\ntexto em minusculas AINDA É texto"
print(texto.replace("texto", "palavras"))

#O operador in verifica se umt texto está em outro
texto1 = "\ntexto em minusculas AINDA É texto"
texto2 = "em"
print(texto2 in texto1)