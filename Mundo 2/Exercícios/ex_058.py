# Jogo Desafio 021 aprimorado

from random import randint

cont = 0
jc = randint(0, 10)
jogador = int(input("Eu pensei em um número de 0 a 10. Em qual número eu pensei? = "))
while jogador != jc:
    if jogador < jc:
        jogador = int(input("MAIS!! Tente novamente = "))
        cont += 1
    elif jogador > jc:
        jogador = int(input("MENOS!! Tente novamente = "))
        cont += 1
print("=" * 40)
print(f"PARABÉNS VOCÊ ACERTOU COM {cont + 1} TENTATIVAS!!")    
