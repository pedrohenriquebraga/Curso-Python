# para pedir ajuda ao python, use help(função)
# Para documentar os próprios comandos usamos docstrings
# Para passar parâmetros opcionais em funções:
# Usamos o sinal de = e o parâmetro opcional
# Para usar uma variável global usamos o método global e a variável

# Docstring

#def contador(i, f, p):
#    """
#    >>> FAZ UM CONTADOR NO PYTHON
#    :param i: NÚMERO INICIAL DO CONTADOR
#    :param f: NÚMERO TERMINAL DO CONTADOR
#    :param p: NÚMERO DO PASSO DO CONTADOR
#    :return: NÃO RETORNA NADA
#    """
#help(contador)

# RETORNO DE VALORES

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
print(f"A SOMA VALE {somar(4, 9)}")