# Mostra o nome completo em maiúsculas e minúsculas

nome = str(input("Digite seu nome completo:")).strip()
print(f"Seu nome em maiúsculas:{nome.upper()}\nSeu nome em minúsculas:{nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(' ')} caracteres")
print(f"Seu 1° nome tem {nome.find(' ')} letras")