# Números em ordem decrescente

valores = []

while True:
    valores.append(int(input("Digite um número: ")))
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar not in "SsNn":
        while continuar not in "SsNn":
            continuar = str(input("Escolha uma opção válida: ")).upper().strip()[0]
    if continuar == "N":
        valores.sort(reverse=True)
        break
print(f"Você digitou {len(valores)} números")
print(f"Em ordem decrescente fica: {valores}")
if 5 in valores:
    print("O valor 5 está na lista")
else:
    print("O valor 5 não está na lista")