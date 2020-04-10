# Soma apenas de números pares

s = 0

for c in range(0, 6):
    n = int(input(f"{c + 1}° número: "))
    if n % 2 == 0:
        s += n
print(f"A soma dos números pares é {s}")
        