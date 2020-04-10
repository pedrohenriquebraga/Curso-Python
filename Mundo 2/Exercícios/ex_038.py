# Mostra o maior e o menor valor

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro valor: "))
maior = num1

if num2 > maior:
    print(f"O {num2} é maior que o {num1}!!")
elif num2 < maior:
    print(f"O {num1} é maior que o {num2}!!")
elif num1 == num2:
    print("Os dois são iguais!!")