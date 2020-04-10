# Várias informações em dicionários

from datetime import date
trabalhador = dict()
anoatual = date.today().year

trabalhador["nome"] = str(input("Nome: ")).title()
nasc = int(input("Ano de nascimento: "))

trabalhador["idade"] = anoatual - nasc

trabalhador["ctps"] = int(input("Carteira de Trabalho(0 não tem): "))
if trabalhador["ctps"] != 0:
    trabalhador["anocont"] = int(input("Ano da contratação: "))
    trabalhador["salario"] = float(input("Salário: R$ "))
    apos = (trabalhador["anocont"] - nasc) + 35
    trabalhador["aposentadoria"] = apos
print("~" * 45)
print(trabalhador)
print("~" * 45)
for k, v in trabalhador.items():
    print(f"{k.title()} = {v}")
