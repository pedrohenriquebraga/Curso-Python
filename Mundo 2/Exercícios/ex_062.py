# Desafio 061 Aprimorado

cont = 0
print("=" * 45)
pt = int(input("Primeiro Termo: "))
r = int(input("Razão: "))
print("=" * 45)

while cont != 10:
    print(pt, end=" ")
    pt = pt + r
    cont += 1

while True:
    mt = int(input("\nMais quantos termos?[0 para parar]: "))
    ct = cont + mt
    if mt != 0:
        while cont != ct:
            print(pt, end=" ")
            pt = pt + r
            cont += 1
    elif mt == 0:
        break
print("Fim")