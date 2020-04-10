# Calcula valor de viagens

km = int(input("Distância da viagem: "))
if km <= 200:
    cost = km * 0.50
    print(f"A Viagem custará R$ {cost}!!")
else:
    cost = km * 0.45
    print(f"A viagem custará R$ {cost}!!")