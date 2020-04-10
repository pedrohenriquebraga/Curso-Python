# Mostra o primeiro e o último nome de uma pessoa

name = str(input("Digite seu nome completo: ")).strip()
print(f"Seu primeiro nome é {name.split()[0]}")
print(f"Seu último nome é {name.split()[-1]}")