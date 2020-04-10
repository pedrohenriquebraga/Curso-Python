# Modularização para moeda

from ex108 import *

v = float(input("Digite um valor: R$ "))
print(f"A metade de {moeda(v)} é {moeda(metade(v))}")
print(f"O dobro de {moeda(v)} é {moeda(dobro(v))}")
print(f"{moeda(v)} com 10% de aumento fica {moeda(aumentar(v, 10))}")
print(f"{moeda(v)} com 13% de diminuição fica {moeda(diminuir(v, 13))}")