# Guardando números em tupla

num1 = int(input("Digite o 1° valor: "))
num2 = int(input("Digite o 2° valor: "))
num3 = int(input("Digite o 3° valor: "))
num4 = int(input("Digite o 4° valor: "))
numeros = (num1, num2, num3, num4)
print("~" * 50)
print(f"Os números digitados foram:{numeros}")
print(f"O número nove apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O número três apareceu pela primeira vez na posição {numeros.index(3) + 1}")
else:
    print("O número três não foi digitado!!")
print(f"Os números pares digitados foram:")
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=" ")