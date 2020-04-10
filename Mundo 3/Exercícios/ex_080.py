# Colocar em ordem crescente sem sort()

valores = list()

for c in range(0, 5):
    num = int(input(f"Digite o {c}° número: "))
    if c == 0 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1
print(f"Você digitou os valores {valores}")