# CLASSIFICAÇÃO DE IDADE PARA CNN

from datetime import date

ano = date.today().year
idade = int(input("Qual seu ano de nascimento?: "))
classi = ano - idade

if classi <= 9:
    print(f"Você tem {classi} anos, portanto você está na categoria MIRIM!!")
elif classi <= 14:
    print(f"Você tem {classi} anos, portanto você está na categoria INFANTIL!!")
elif classi <= 19:
    print(f"Você tem {classi} anos, portanto você está na categoria JÚNIOR!!")
elif classi <= 25:
    print(f"Você tem {classi} anos, portanto você está na categoria SÊNIOR!!")
elif classi > 25:
    print(f"Você tem {classi} anos, portanto você está na categoria MASTER!!")