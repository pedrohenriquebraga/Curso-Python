# Mostra o valor da multa de um carro que passou do limite de 80KM/h

speed = float(input("Qual a velocidade do carro? = "))
if speed > 80:
    value = (speed - 80) * 7
    print(f"Você foi multado em R$ {value:.2f}!")
else:
    print("Parabéns, você tá dentro do limite de velocidade!")
print("Fim do Programa")
