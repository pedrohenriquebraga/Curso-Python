# Soma de números

cont = 0
soma = 0

while True:
    num = float(input("Digite um número[999 para parar]: "))
    if num != 999:
        cont += 1
        soma += num
    else:
        break
print(f"Você digitou {cont} números e a soma deles é {soma}")
    