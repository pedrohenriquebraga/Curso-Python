# Ler apenas números inteiros e reais com  exceções

def leiaInt(msg, num=0):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mERRO!! DIGITE UM NÚMERO INTEIRO!!\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mO USUÁRIO PREFERIU NÃO INFORMAR O NÚMERO!!\033[m")
            break
        else:
            return num
    
def leiaFloat(msg, num=0):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print("\033[1;31mERRO!! DIGITE UM NÚMERO REAL!!\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mO USUÁRIO PREFERIU NÃO INFORMAR O NÚMERO!!\033[m")
            break
        else:
            return num

    
numInt = leiaInt("Digite um número inteiro: ")
numFloat = leiaFloat("Digite um número real: ")
print(f"Você digitou o número inteiro {numInt}")
print(f"Você digitou o número real {numFloat}")
