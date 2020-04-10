#Soma de ímpares entre 1 e 500

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 
        s += c
print(f"A soma de todos os {cont} números impares entre 1 e 500 é {s}")