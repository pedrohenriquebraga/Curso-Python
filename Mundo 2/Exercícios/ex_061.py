# Desafio 051 Aprimorado

cont = 0
pt = int(input("Primeiro Termo: "))
r = int(input("Razão: "))

while cont != 10:
    print(pt, end=" • ")
    pt = pt + r
    cont += 1
print("Fim")