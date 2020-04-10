# SOMA DE VÁRIOS NÚMEROS

soma = cont = 0
while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"A soma dos {cont} valores é {soma}")