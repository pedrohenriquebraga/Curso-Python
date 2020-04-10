# Verifica se é um ano Bissexto ou não

from datetime import date

year = int(input("Digite um ano(0 para ver o ano atual): "))

if year == 0:
    year = date.today().year
    
if year % 4 == 0 or year % 400 == 0:
    if year % 100 != 0:
        print(f"O ano {year} É BISSEXTO!!")
    else:
        print(f"O ano {year} NÃO É BISSEXTO!!")