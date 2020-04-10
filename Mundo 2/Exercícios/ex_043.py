# MOSTRA SEU IMC

peso = float(input("Seu Peso: "))
altura = float(input("Sua Altura: "))
imc = peso / (altura * altura)

if imc <= 18.5:
    print(f"Seu IMC é {imc:.2f}, você está ABAIXO DO PESO!!")  
elif imc > 18.5 and imc <= 25:
    print(f"Seu IMC é {imc:.2f}, você está no PESO IDEAL!!")
elif imc > 25 and imc <= 30:
    print(f"Seu IMC é {imc:.2f}, você está ACIMA DO PESO!!")
elif imc > 30 and imc <= 45:
    print(f"Seu IMC é {imc:.2f}, você está com OBESIDADE!!")
elif imc > 45:
    print(f"Seu IMC é {imc:.2f}, você está com OBESIDADE MÓRBIDA!!")