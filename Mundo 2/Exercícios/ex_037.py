# Conversor para binário, octal e hexadecimal

num = int(input("Digite um número: "))
op = int(input("""Converter para: 
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
Sua Opção: """))
print("=" * 50)

if op == 1:
    print(f"Binário: {bin(num)[2:]}")
elif op == 2:
    print(f"Octal: {oct(num)[2:]}")
else:
    print(f"Hexadecimal: {hex(num)[2:]}")