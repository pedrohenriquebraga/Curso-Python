# Criar uma matriz

matriz = list()
dado = list()
cont = 0

for q in range(0, 3):
    dado.clear()
    for c in range(0, 3):
        pos = int(input(f"Digite um número na posição[{len(matriz) + 1}, {c + 1}]: "))
        dado.append(pos)
        if c == 2:
            matriz.append(dado[:])
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[ {matriz[l][c]:^3} ]", end="")
    print()