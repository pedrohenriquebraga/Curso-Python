# Separa números

num = int(input("Digite um número de 0 a 9999: "))

print(f"Unidade de milhar: {num // 1000 % 10}")
print(f"Centena: {num // 100 % 10}")
print(f"Dezena: {num // 10 % 10}")
print(f"Unidade: {num // 1 % 10}")