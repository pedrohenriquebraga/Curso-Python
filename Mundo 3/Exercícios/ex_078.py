# MAIOR E MENOR NÚMERO EM LISTA

num = list()

for c in range(0, 5):
    num.append(int(input(f"Digite o {c}° valor: ")))
print(f"Você digitou os números:{num}")
print(f"O maior valor digitado foi o {max(num)} nas posições ", end="")
for i, v in enumerate(num):
    if v == max(num):
        print(i, end=" ")
print()
print(f"O menor valor digitado foi o {min(num)} nas posições ", end="")
for i, v in enumerate(num):
    if v == min(num):
        print(i, end=" ")
print()
