def metade(valor=0, formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)

def dobro(valor=0, formato=False):
    res = valor * 2
    return res if formato is False else moeda(res)

def aumentar(valor=0, p=10, formato=False):
    res = valor + ((valor * p) / 100)
    return res if formato is False else moeda(res)

def diminuir(valor=0, p=10, formato=False):
    res = valor - ((valor * p) / 100)
    return res if formato is False else moeda(res)

def moeda(valor=0, moeda="R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")