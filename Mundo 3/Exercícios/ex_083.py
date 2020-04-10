# Verificação de expressões

conta = 0
contf = 0
expre = str(input("Digite uma expressão: "))

for i in range(0, len(expre)):
    if expre[i] == "(":
        conta += 1
    if expre[i] == ")":
        contf += 1
if conta == contf:
    print("Está expressão é valida!")
else:
    print("Está expressão não é válida!")