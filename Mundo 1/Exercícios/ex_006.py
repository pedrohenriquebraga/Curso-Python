# Algoritmo que mostrará o dobro, triplo e a raiz quadrada de um número

num = float(input("Digite um número: "))

print(f"Você digitou o número {num}")
print(f"Seu dobro é {num * 2} e seu triplo é {num * 3}")
print("A sua raiz quadrada é {:.2f}".format(num ** (1/2)))