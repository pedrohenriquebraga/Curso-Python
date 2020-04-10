# Aprimorar desafio 093

time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do Jogador: ")).title()
    part = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(0, part):
        gols.append(int(input(f"   Quantos gols na partida {c}? ")))   
    jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if resp in "SN":
            break
        print("ERRO! DIGITE APENAS S OU N")
    if resp == "N":
        break
print("-" * 45)
print("cod", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
while True:
    busca = int(input("Mostrar dados de qual jogador? "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"NÃO EXISTE JOGADOR COM O CÓDIGO {busca}")
    else:
        print(f" --LEVANTAMEMTO DO JOGADOR {time[busca]['nome']}:")
    for i, v in enumerate(time[busca]["gols"]):
        print("~" * 45)
        print(f"   => Na partida {i}, fez {v} gols")
print("~" * 45)
