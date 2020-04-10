# CADASTRO DE PESSOAS

maior = homem = mulher20 = 0
while True:
    print("=" * 45)
    sexo = str(input("SEXO[M/F]: ")).upper().strip()[0]
    if sexo not in "MF":
        while sexo not in "MmFf":
            sexo = str(input("SEXO[M/F]: ")).upper().strip()[0]
    idade = int(input("IDADE: "))
    continuar = str(input("QUER CADASTRAR MAIS PESSOAS? [S/N] ")).strip()[0].upper()
    if continuar not in "SN":
        while continuar not in "SN":
            continuar = str(input("QUER CADASTRAR MAIS PESSOAS? [S/N] ")).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulher20 += 1
    if continuar == "N":
        break
print("=" * 45)
print(f"{maior} pessoas tem mais de 18 anos")
print(f"Foram cadastrados {homem} homens")
print(f"{mulher20} mulheres tem menos de 20 anos")
print("=" * 45)
