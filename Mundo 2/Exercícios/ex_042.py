# DIZ QUAL TIPO DE TRIÂNGULO SE FORMARÁ

r1 = float(input("Digite a 1° reta: "))
r2 = float(input("Digite a 2° reta: "))
r3 = float(input("Digite a 3° reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Essas retas podem FORMAR um triângulo", end=" ")
    if r1 == r2 == r3:
        print("EQUILÁTERO!!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!!")
    else:
        print("ISÓSCELES!!")
else:
    print("Esse triângulo não pode existir!!")
