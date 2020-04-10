from Comandos import Validar
from Comandos.Validar import *

def menu(lista):
    c = 0
    print("-" * 40)
    for i in lista:
        print(f"\033[1;32m[ {c} ] {i}")
        c += 1
    print("\033[m-" * 40)
    opc = ValidaOp("Digite sua escolha: ", True)
    return opc

def PrintPerso(msg):
    print("-" * 40)
    print(msg.center(40))
    print("-" * 40)