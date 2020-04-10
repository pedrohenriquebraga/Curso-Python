# Números pares e ímpares em uma única lista

números = [[], []]

for i in range(0, 7):
    num = int(input(f"Digite o {i + 1}° valor: "))
    if num % 2 == 0:
        números[0].append(num)
    else:
        números[1].append(num)
números[0].sort()
números[1].sort()
print(f"Os números pares digitados foram: {números[0]}")
print(f"Os números ímpares digitados foram: {números[1]}")