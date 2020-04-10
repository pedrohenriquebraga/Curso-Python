# Contador com função

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 0
    print("=" * 40)
    print(f"CONTAGEM DE {i} ATÉ {f} DE {p} EM {p}")
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.3)
            cont += p
        print("FIM")
    if i > f:
        cont = i
        while cont >= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.3)
            cont -= p
        print("FIM")
contador(0, 10, 1)
contador(10, 0, 2)
print("=" * 40)
print("Agora é sua vez de personalizar!")
print("=" * 40)
ini = int(input("INÍCIO: "))
fim = int(input("FIM:    "))
pas = int(input("PASSO:  "))
contador(ini, fim, pas)