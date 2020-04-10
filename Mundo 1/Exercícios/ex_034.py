# Calcula aumento de salário

salary = float(input("Qual o valor do salário? = R$ "))
if salary > 1250:
    gain = salary + (salary * 10 / 100)
    print(f"Com o aumento de 10%, seu salário será R$ {gain}!")
else:
    gain = salary + (salary * 15 / 100)
    print(f"Com o aumento de 15%, seu salário será R$ {gain}!!")