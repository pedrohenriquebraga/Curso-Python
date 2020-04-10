# Organizar números em dicionários

from random import randint
from time import sleep
from operator import itemgetter

dado = {}
ranking = []
mai = 0
cont = 0

print("VALORES SORTEADOS:")
for c in range(1, 5):
    dado[f"jogador{c}"] = randint(1, 6)
    print(f"   O jogador {c} tirou {dado[f'jogador{c}']}")
    sleep(0.5)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print("RANKING DOS JOGADORES:")
for i, v in enumerate(ranking):
    print(f"   {i + 1}° lugar: {v[0]} com {v[1]}")
    sleep(0.5)
