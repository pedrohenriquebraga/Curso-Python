# Mostra o maior e o menor peso

maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input(f"Peso da {c + 1}° pessoa(KG): "))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f"O maior peso digitado foi {maior}KG")
print(f"O menor peso digitado foi {menor}KG")