# Aprimorar desafio passado

matriz = list()
dado = list()
cont = 0
par = scol = maior = 0
for q in range(0, 3):
    dado.clear()
    for c in range(0, 3):
        pos = int(input(f"Digite um número na posição[{len(matriz) + 1}, {c + 1}]: "))
        if pos % 2 == 0:
            par += pos
        dado.append(pos)
        if c == 2:
            matriz.append(dado[:])
print("~" * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[ {matriz[l][c]:^3} ]", end="")
        
    print()
print("~" * 40)
print(f"A soma dos valores pares digitados é {par}")
for l in range(0, 3):
    scol += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {scol}")
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é {maior}")