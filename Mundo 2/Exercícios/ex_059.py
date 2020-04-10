# Calculadora

from time import sleep

print("=" * 30)
valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))

while True:
    print("=" * 30)
    opcao = int(input("""Você deseja:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair Do Programa
SUA OPÇÃO: """))
    print("=" * 30)
    while True:
        if opcao > 5 or opcao < 1:
            opcao = int(input("OPÇÃO INVÁLIDA!! Digite uma opção válida: "))
        else:
            print("=" * 30)
            break
    if opcao == 1:
        print(f"{valor1} + {valor2} = {valor1 + valor2}")
    elif opcao == 2:
        print(f"{valor1} x {valor2} = {valor1 * valor2}")
    elif opcao == 3:
        if valor1 > valor2:
            print(f"O {valor1} é o maior número!!")
        elif valor1 < valor2:
            print(f"O {valor2} é o maior número!!")
        else:
            print("Os dois números são iguais!!")
    if opcao == 4:
        valor1 = float(input("Digite um valor: "))
        valor2 = float(input("Digite outro valor: "))
    if opcao == 5:
        print("OK, SAINDO DO PROGRAMA...")
        sleep(2)
        break

print("PROGRAMA ENCERRADO!!")