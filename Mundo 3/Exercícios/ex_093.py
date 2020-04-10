# Aproveitamento de um jogador

jogador = dict()
gols = []
aprov = cont = 0

jogador["nome"] = str(input("Nome do Jogador: ")).title()
part = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for c in range(0, part):
    gol = int(input(f"   Quantos gols na partida {c}? "))
    aprov += gol
    gols.append(gol)

jogador["gols"] = gols.copy()
jogador["total"] = aprov
print("~" * 45)
print(jogador)
print("~" * 45)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("~" * 45)
print(f"O jogador {jogador['nome']} jogou {part} partidas.")
for v in jogador["gols"]:
    print(f"   => Na partida {cont}, fez {v} gols")
    cont += 1
print(f"Foi um total de {aprov} gols.")
print("~" * 45)

    