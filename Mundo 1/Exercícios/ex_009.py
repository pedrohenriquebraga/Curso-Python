# Mostra a tabuada de um número

num = int(input("Digite um número: "))

for c in range(1, 11):
    print("{: > 2} x {} = {:<2}".format(num, c, num * c))
