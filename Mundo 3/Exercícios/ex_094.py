# Ler e mostrar várias informações de pessoas em dicionários

pessoas = []
pessoa = {}
cont = media = 0

while True:
    print("=" * 35)
    pessoa["nome"] = str(input("Nome: ")).title()
    pessoa["sexo"] = str(input("Sexo[M/F]: ")).upper().strip()[0]
    if pessoa["sexo"] not in "MF":
        while pessoa["sexo"] not in "MF":
            print("ERRO! DIGITE APENAS M OU F.")
            pessoa["sexo"] = str(input("Sexo[M/F]: ")).upper().strip()[0]
    pessoa["idade"] = int(input("Idade: "))
    media += pessoa["idade"]
    cont += 1
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resp = str(input("Quer continuar? [S/N] = ")).upper().strip()[0]
    if resp not in "SN":
        while resp not in "SN":
            print("ERRO! RESPONDA APENAS S OU N.")
            resp = str(input("Quer continuar? [S/N] = ")).upper().strip()[0]
    if resp == "N":
        break
media /= cont
print("~" * 35)
print(f"Você cadastrou {cont} pessoas!!")
print(f"A média de idade do grupo é {media:.2f}")
print("As mulheres cadastradas foram: ")
for p in pessoas:
    if p["sexo"] == "F":
        print(f'{p["nome"]:^36}')
print("As pessoas com idade acima da média são: ")
for p in pessoas:
    if p["idade"] > media:
        print(f"{p['nome']:^36}")
