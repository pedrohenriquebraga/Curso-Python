# TABUADA COM FLAG DE NÚMERO NEGATIVO

while True:
    print("=" * 45)
    n = int(input("Número para fazer a tabuada: "))
    print("=" * 45)
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} x {c:2} = {n * c}")
print("FIM DO PROGRAMA!!")