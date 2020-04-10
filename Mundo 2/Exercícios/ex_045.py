# Criar Um Jokenpô

from random import choice
from time import sleep

jk = ("pedra", "papel", "tesoura")
comp = choice(jk)
jogador = int(input("""1 - Pedra
2 - Papel
3 - Tesoura
ESCOLHA UM: """))
print("AGUARDE...")
sleep(2)

if jogador == 1 and comp == "pedra":
    print("O computador escolheu Pedra, EMPATE!!")
elif jogador == 1 and comp == "papel":
    print("O computador escolheu Papel, VOCÊ PERDEU!!")
elif jogador == 1 and comp == "tesoura":
    print("O computador escolheu Tesouro, VOCÊ GANHOU!!")

if jogador == 2 and comp == "pedra":
    print("O computador escolheu Pedra, VOCÊ GANHOU!!")
elif jogador == 2 and comp == "papel":
    print("O computador escolheu Papel, EMPATE!!")
elif jogador == 2 and comp == "tesoura":
    print("O computador escolheu Tesoura, VOCÊ PERDEU!!")

if jogador == 3 and comp == "pedra":
    print("O computador escolheu Pedra, VOCÊ PERDEU!!")
elif jogador == 3 and comp == "papel":
    print("O computador escolheu Papel, VOCÊ GANHOU!!")
elif jogador == 3 and comp == "tesoura":
    print("O computador escolheu Tesoura, EMPATE!!")    
