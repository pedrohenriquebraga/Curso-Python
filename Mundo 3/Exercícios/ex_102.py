# Fatorial com função

def fatorial(num=1, show=False):
    """
    >>> FAZ UM CONTADOR NO PYTHON
    :param num: NÚMERO INICIAL DO FATORIAL
    :param show: (OPICIONAL)PARÂMETRO QUE QUE MOSTRA OU NÃO A CONTA
    :return: O RESULTADO DO FATORIAL
    """
    f = 1
    for n in range(num, 0, -1):
        f *= n
        if show == True:
            print(n, end="")
            if n > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
    return f
        
        
print(fatorial(5))