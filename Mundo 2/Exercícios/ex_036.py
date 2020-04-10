# SIMULA UM EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA

valor = float(input("Quanto custa a casa? R$ "))
salario = float(input("Qual o seu salário? R$ "))
anos = int(input("Em quantos anos você quer pagar? "))
print("=" * 50)
prest = valor/(anos * 12)
situacao = (salario * 30) / 100

print(f"\033[1;33m30% do seu salário é R$ {situacao:.2f}\033[m")
if prest > situacao:
    print(f"\033[1;31mNão é possível fazer o empréstimo, pois o valor de R$ {prest:.2f} das prestações excede 30% do seu salário!\033[m")
elif prest <= situacao:
    print(f"\033[1;32mPARABÉNS!! Seu empréstimo foi aprovado, cada prestação custa R$ {prest:.2f}!\033[m")
