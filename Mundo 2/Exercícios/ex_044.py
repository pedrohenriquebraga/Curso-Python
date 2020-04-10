# Pagamento de uma produto

valor = float(input("Qual o valor do produto? R$ "))
pagamento = int(input("""1 - Á Vista(Com 10% de desconto)
2 - À Vista no cartão(Com 5% de desconto)
3 - 2x no cartão(preço normal)
4 - 3x ou mais no cartão(com 20% de juros)
Forma de Pagamento: """))
print("=" * 50)

desconto10 = valor * 10 / 100
desconto5 = valor * 5 / 100
juros = valor * 20 / 100

if pagamento == 1:
    print(f"O valor do produto vai de R$ {valor} para R$ {valor - desconto10} com 10% de desconto!!")
elif pagamento == 2:
    print("O valor do produto vai de R$ {valor} para R$ {valor - desconto5} com 5% de desconto!!")
elif pagamento == 3:
    print(f"Você pagará o valor de R$ {valor} em 2x no cartão, cada parcela sairá por R$ {valor / 2}!!")
elif pagamento == 4:
    parcela = int(input("Em quantas parcelas você dividirá?: "))
    print(f"O valor vai de R$ {valor} para R$ {valor + juros} com 20% de juros, cada parcela sairá por R$ {(valor + juros) / parcela}")