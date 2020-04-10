# Geração de Números e Tuplas

from random import randint

num = tuple(randint(0, 10) for c in range(0, 5))
maior = menor = num[0]

print(f"Os valores sorteados foram: {num}")
for c in range(0, len(num)):
    if num[c] < menor:
        menor = num[c]
    if num[c] > maior:
        maior = num[c]
print(f"O maior valor foi {maior}")
print(f"O menor valor foi {menor}")