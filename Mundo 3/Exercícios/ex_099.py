# Maior valor em funções

from time import sleep

def maior(*num):
    maior = cont = 0
    print("=" * 45)
    print("ANALISANDO OS VALORES PASSADOS...")
    for n in num:
        sleep(0.5)
        print(n, end=" ", flush=True)
        if cont == 0:
            maior = n
            cont += 1
        else:
            if n > maior:
                maior = n
    print()   
    print(f"Você digitou {len(num)} valores e maior valor foi {maior}")

maior(9, 2, 5)
maior(2, 1)
maior(7, 4, 0, 3, 1)
maior()