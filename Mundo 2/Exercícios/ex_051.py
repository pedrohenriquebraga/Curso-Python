# Progressão Aritmética

pt = int(input("Primeiro Termo: "))
r = int(input("Razão: "))
dc = pt + (10 - 1) * r

for c in range(pt, dc + r, r):
    print(c, end=" • ")
print("Fim")