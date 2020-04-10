# DADOS DE PESSOAS

ipm = media = maior = mm = 0
mh = ""
for c in range(1, 5):   
    # Dados das pessoas
    print("=" * 25)
    nome = str(input("Nome: ")).title().strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: "))[0].upper().strip()
    if idade > maior and sexo == "M":
        maior = idade
        mh = nome
    ipm = ipm + idade
    media = ipm / 5
    if idade < 20 and sexo == "F":
       mm  += 1   
print("=" * 50)
print(f"A média de idade é {media:.2f}")
print(f"O homem mais velho se chama {mh}")
print(f"{mm} mulheres tem menos de 20 anos")
