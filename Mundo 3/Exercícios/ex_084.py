# Lê nome e peso de várias pessoas e guardar em uma lista

pessoas = list()
dado = []
cont = 0
maior = menor = 0
while True:
    dado.append(str(input("Digite o nome: ").title()))
    dado.append(int(input("Peso: [Kg] ")))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if pessoas[cont][1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    conti = str(input("Quer continuar? [S/N]: "))    
    if conti in "Nn":
        break
print("~" * 45)
print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"O maior peso foi {maior}KG de:")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]}", end=" ")
print(f"\nO menor peso foi {menor}KG de: ")
if p[1] == menor:
        print(f"{p[0]}", end=" ")
        