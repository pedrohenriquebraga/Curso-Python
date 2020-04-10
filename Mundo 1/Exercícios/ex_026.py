# Ocorrências de A

frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra a aparece {frase.count('A')} vezes")
print(f"A letra a aparece pela primeira vez na posição {frase.find('A') + 1}")
print(f"A letra a aparece pela última vez na posição {frase.rfind('A') + 1}")
