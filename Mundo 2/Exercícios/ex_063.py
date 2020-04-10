# Sequência de Fibonacci

qt = int(input("Quantos termos você quer mostrar? "))

t1 = 0
t2 = 1
cont = 3

print(f"{t1} • {t2}", end=" • ")

while cont <= qt:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3, end=" • ")
    cont += 1
    	
print("FIM")
    