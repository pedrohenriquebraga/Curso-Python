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

def resumo(valor=0, taxaa=10, taxar=5):
    print("-" * 40)
    print("SISTEMA DE VALORES".center(40))
    print("-" * 40)
    print(f"Preço analisado: \t{moeda(valor)}")
    
    print(f"Dobro do preço: \t{dobro(valor, True)}")
    print(f"Metade do preço: \t{metade(valor, True)}")
    print(f"Aumentado em {taxaa}%: \t{aumentar(valor, taxaa, True)}")
    print(f"Diminuindo em {taxar}%: \t{diminuir(valor, taxar, True)}")
    print("-" * 40)
    