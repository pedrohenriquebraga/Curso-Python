# Gerador para mega-sena

from random import randint
from time import sleep

dado = []
cont = 0

print("=" * 45)
print(f"{'JOGA NA MEGA SENA':^45}")
print("=" * 45)
palp = int(input("Quantos jogos você quer gerar? = "))
print("~" * 40)
for c in range(0, palp):
    for n in range(0, 6):
        sorteio = randint(1, 60)
        if c == 0:
            dado.append(sorteio)
        else:
            if sorteio not in dado:
                dado.append(sorteio)
            else:
                while sorteio in dado:
                    sorteio = randint(1, 60)
                dado.append(sorteio)
    dado.sort()
    sleep(0.3)
    cont += 1
    print(f"Jogo {cont}: {dado}")
    dado.clear()
