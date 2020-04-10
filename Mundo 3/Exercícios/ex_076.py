# Tupla com produtos e preços

listagem = ("Pão", 3, "Leite", 4, "Lápis", 2.50,
"Caneta", 2, "Mouse", 150)

print("~" * 50)
print(f"{'LISTA DE PREÇOS':^50}")
print("~" * 50)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<20}",end="")
    else:
        print(f"R$ {listagem[pos]:>6.2f}")
print("~" * 50)