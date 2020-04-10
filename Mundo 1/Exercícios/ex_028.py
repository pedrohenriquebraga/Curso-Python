# Jogo de adivinhação com o computador

from random import randint

comp = randint(0, 5)
user = int(input("Qual número de 0 a 5 eu pensei? = "))
if comp == user:
    print("Parabéns, você acertou!!")
else:
    print(f"Que pena, eu pensei no número {comp}!")
print("Fim do Programa")