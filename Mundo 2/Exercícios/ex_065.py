# Mostra o maior número e o menor

maior = menor = 0
cont = 0
soma = 0
while True:
    cont += 1
    print("=" * 30)
    num = int(input("Digite um valor: "))
    soma += num
    continuar = str(input("Quer Continuar?[S/N]: "))[0].upper().strip()
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if continuar == "N":
        break
print("=" * 30)
print(f"Você digitou {cont} números")
print(f"A média entre os {cont} números digitados foi {soma / cont}")
print(f"O maior número digitado foi {maior}")
print(f"O menor número digitado foi {menor}")
    