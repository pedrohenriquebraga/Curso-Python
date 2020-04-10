# CADASTRO DE VÁRIOS PRODUTOS

print("~" * 45)
print(f"{' LOJÃO BARATÃO ':^45}")


soma = cont1000 = menor = cont = 0
nomemenor = ""
while True:
    print("~" * 45)
    produto = str(input("NOME DO PRODUTO: ")).title().strip()
    preco = float(input("PREÇO DO PRODUTO: R$ "))
    continuar = str(input("QUER CADASTRAR MAIS UM PRODUTO? [S/N]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("QUER CADASTRAR MAIS UM PRODUTO? [S/N]: ")).strip().upper()[0]
    soma += preco
    cont += 1
    if preco >= 1000:
        cont1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        nomemenor = produto
    if continuar == "N":
        break

print("~" * 45)
print(f"{cont} produtos foram registrados")
print(f"O TOTAL DAS COMPRAS FOI R$ {soma}")
print(f"{cont1000} produtos custam mais de R$ 1000")
print(f"O(a) {nomemenor} é o produto mais barato, custando R$ {menor}")  
print("~" * 45)

