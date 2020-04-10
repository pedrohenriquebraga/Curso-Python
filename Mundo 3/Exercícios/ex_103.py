# Função paa ficha do jogador

def ficha(nome="<desconhecido>", gols=0):
    return f"O jogador {nome} fez {gols} gol(s)"


n = str(input("Nome do jogador: "))
g = input("Quantos gols ele fez?: ")

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(n, g))