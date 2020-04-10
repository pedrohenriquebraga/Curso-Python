# JOGANDO ÍMPAR OU PAR

from random import randint

cores = {"vermelho":"\033[1;31m", "limpa":"\033[m",
"verde":"\033[1;32m", "azul":"\033[1;36m"}

vitorias = 0

while True:
    comp = randint(0, 10)
    print("~" * 45)
    jogador = int(input(f"{cores['azul']}Escolha um número: {cores['limpa']}"))
    
    pi = str(input(f"{cores['azul']}Escolha Ímpar ou Par[I/P]: {cores['limpa']}")).strip().upper()[0]
    while pi not in "PpIi":
        pi = str(input("Escolha Ímpar ou Par[I/P]: ")).strip().upper()[0]
    
    vencedor = (comp + jogador) % 2
    
    if vencedor == 0 and pi == "P":
        print("~" * 45)
        print(f"{cores['verde']}{'PARABÉNS, VOCÊ VENCEU!!':^45}{cores['limpa']}")
        vitorias += 1
    elif vencedor == 1 and pi == "I":
        print("~" * 45)
        print(f"{cores['verde']}{'PARABÉNS, VOCÊ VENCEU!!':^45}{cores['limpa']}")
        vitorias += 1
    else:
        print("~" * 45)
        print(f"{cores['vermelho']}{'VOCÊ PERDEU!!':^45}{cores['limpa']}")
        break
print("~" * 45)
print(f"{cores['verde']}Você ganhou {vitorias} vezes!!{cores['limpa']}")