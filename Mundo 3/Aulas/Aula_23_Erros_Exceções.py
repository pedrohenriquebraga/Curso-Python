try:
    a = int(input("Numerador: "))
    b = int(input("Divisor: "))
    r = a / b
except (ValueError, TypeError):
    #Exception mostra o que ocorreu de errado
    print("Tivemos um erro o tipo de dados que você enviou!!")
except ZeroDivisionError:
    print("Nenhum número pode ser dividido por ZERO!!")
except KeyboardInterrupt:
    print("O Usuário preferiu não informar os valores")
else:
    print(f"O resultado é {r}")
finally:
    print("Volte Sempre!!Muito Obrigado!!")