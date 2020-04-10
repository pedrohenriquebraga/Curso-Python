# Fatorial

num = int(input("Digite uma número para saber seu fatorial: "))
f = num
print(f"O fatorial de {num}! = ", end="")

while num > 1:
    print(f"{num}", end="")
    print(" x " if num > 2 else " x 1 = ", end="")
    num -= 1
    f *= num
print(f"{f}")