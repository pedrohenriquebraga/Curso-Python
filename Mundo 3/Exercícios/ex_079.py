# Verificação de valores em listas

valores = list()

while True:
    print("~" * 45)
    num = int(input("Digite um valor: "))
    if num not in valores:
        valores.append(num)
        print("VALOR ADICIONADO COM SUCESSO...")
    else:
        print("VALOR DUPLICADO!! NÃO VOU ADICIONAR...")
    continuar = str(input("Quer adicionar outro? [S/N] ")).strip().upper()[0]
    if continuar not in "SsNn":
        while continuar not in "SsNn":
            continuar = str(input("Digite uma opção válida: "))
    if continuar == "N":
        valores.sort()
        break
print("~" * 45)
print(f"Você digitou os valores {valores}")