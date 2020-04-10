# Mostra o valor da hipotenusa

import math

co = float(input("Comprimento cateto oposto: "))
ca = float(input("Comprimento cateto adjacente: "))
h = (co ** 2 + ca ** 2) ** (1/2)
print(f"O valor da hipotenusa é {h:.2f}")

# ou usando o hypot()

print(f"O valor dá hipotenusa é {math.hypot(co, ca):.2f}")