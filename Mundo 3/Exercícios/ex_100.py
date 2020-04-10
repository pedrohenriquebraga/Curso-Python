# Sorteio com funções

from random import randint

num = list()

def sorteia():
    for c in range(0, 5):
        num.append(randint(0, 10))
def somapar(lst):
    par = 0
    pos = 0
    while pos < len(lst):
        for n in lst:
            pos += 1
            if n % 2 == 0:
                par += n
    print(f"A SOMA DOS VALORES SORTEADOS SÃO {par}")
sorteia()
print(f"OS VALORES SORTEADOS FORAM {num}")
somapar(num)

