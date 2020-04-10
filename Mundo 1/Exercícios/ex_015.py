# Calcula o valor de um aluguel de um carro

km = float(input("Quantos Km foram percorridos? "))
dias = int(input("Quantos dias o carro ficou alugado? "))
valor = (60 * dias) + (0.15 * km)

print(f"O valor do aluguel é R${valor} por ter percorrido \n{km}Km e {dias} dias.")
