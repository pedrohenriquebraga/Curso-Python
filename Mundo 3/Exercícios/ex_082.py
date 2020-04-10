# Separar pares de ímpares

valores = []
par = []
impar = []

while True:
    valores.append(int(input("Digite um número: ")))
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar not in "SsNn":
        while continuar not in "SsNn":
            continuar = str(input("Escolha uma opção válida: "))
    if continuar == "N":
        valores.sort(reverse=True)
        break

for i in range(0, len(valores)):
    if valores[i] % 2 == 0:
        par.append(valores[i])
    else:
        impar.append(valores[i])
print(f"Os valores pares digitados foram {par}")
print(f"Os valores ímpares digitados foram {impar}")