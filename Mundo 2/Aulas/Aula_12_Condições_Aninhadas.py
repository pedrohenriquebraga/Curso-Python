#if
#else
#elif

nome = str(input("Qual o seu nome? ")).title()

if nome == "Pedro":
    print("Que nome legal o seu!")
elif nome == "Creusa":
    print("Seu nome é bem diferente!")
else:
    print("Seu nome é bem normal!")
print(f"Tenha um bom dia, {nome}!")