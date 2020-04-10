# Mostra um preço com 5% de desconto

valor = float(input("Digite o valor do produto R$ "))
print(f"O preço desse produto com 5% de desconto é R$ {valor - (valor * 5 / 100):.2f}")