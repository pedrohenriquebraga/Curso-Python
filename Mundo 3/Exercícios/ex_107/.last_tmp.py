# Modularização para moeda

import moeda

v = float(input("Digite um valor: R$ "))
print(f"A metade do valor é R$ {moeda.metade(v)}")
print(f"O dobro do valor é R$ {moeda.dobro(v)}")
print(f"Com aumento de 10% fica R$ {moeda.aumentar(v, 10)}")
print(f"Com desconto de 13% fica R$ {moeda.diminuir(v, 13)}")