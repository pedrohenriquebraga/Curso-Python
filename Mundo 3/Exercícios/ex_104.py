# Ler apenas números inteiros

def leiaint(msg="DIGITE UM NÚMERO: "):
    num = str(input(msg))
    if num.isnumeric() == False:
        while num.isnumeric() == False:
            num = input("\033[0;31mERRO!! Digite um número: \033[m")
    return int(num)
    
    
n = leiaint("DIGITE UM NÚMERO: ")
print(f"Você digitou o número {n}")