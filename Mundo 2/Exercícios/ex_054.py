# Mostrar quantas pessoas não estão na maioridade

from datetime import date

mr = 0
ano = date.today().year
for c in range(0, 7):
    nasc = int(input(f"Ano de nascimento({c + 1}° Pessoa): "))
    if ano - nasc < 21:
        mr += 1
print(f"{mr} pessoas tem menos de 21 anos!")
print(f"{7 - mr} pessoas tem mais de 21 anos!!")