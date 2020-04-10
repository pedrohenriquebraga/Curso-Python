# Se um número é primo ou não

primo = 0
num = int(input("Digite um número: "))

for c in range(1, num + 1):
    if num % c == 0:
        primo += 1
        
if primo == 2:
    print("Este número é primo!!")
if primo > 2:
    print("Este número não é primo!")
        