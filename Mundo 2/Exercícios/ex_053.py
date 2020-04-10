# Se é um palíndromo ou não

frase = str(input("Digite uma frase: ")).lower().replace(" ", "")
pl = frase[::-1]
if pl == frase:
    print("Está frase é um palíndromo!")
else:
    print("Está frase não é um palindromo!!")




