# Mostra o seno, cosseno e tangente

import math

ang = int(input("Digite o valor do ângulo: "))
sine = math.sin(math.radians(ang))
cosine = math.cos(math.radians(ang))
tangent = math.tan(math.radians(ang))
print(f"Seno:{sine:.2f}\nCosseno:{cosine:.2f}\nTangente:{tangent:.2f}")