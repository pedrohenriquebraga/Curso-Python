def metade(valor=0):
    res = valor / 2
    return res

def dobro(valor=0):
    res = valor * 2
    return res

def aumentar(valor=0, p=10):
    res = valor + ((valor * p) / 100)
    return res

def diminuir(valor=0, p=10):
    res = valor - ((valor * p) / 100)
    return res

def moeda(valor=0, moeda="R$"):
    return f"{moeda} {valor:.2f}".replace(".", ",")