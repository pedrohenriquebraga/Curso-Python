# Informações sobre o alistamento militar

from datetime import date

idade = int(input("Qual seu ano de nascimento?: "))
alist = (date.today().year) - idade

if alist < 18:
    print(f"Você tem {alist} anos, portanto, você só poderá se alistar daqui {18-alist} anos!!")
elif alist == 18:
    print("Você tem 18 anos, portanto, está na hora de se alistar no exército!")
else:
    print(f"Você tem {alist} anos, portanto, você já passou {alist - 18} anos do tempo de alistamento!")

