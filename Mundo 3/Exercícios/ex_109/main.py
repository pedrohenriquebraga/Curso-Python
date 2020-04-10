# Modularização para moeda

from ex109 import *

v = float(input("Digite um valor: R$ "))
print(f"A metade de {moeda(v)} é {metade(v, True)}")
print(f"O dobro de {moeda(v)} é {dobro(v, True)}")
print(f"{moeda(v)} com 10% de aumento fica {aumentar(v, 10, True)}")
print(f"{moeda(v)} com 13% de diminuição fica {diminuir(v, 13, True)}")