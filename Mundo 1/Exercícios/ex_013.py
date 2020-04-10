# Mostra quanto será o salário de um funcionário com 15% de desconto

salario = float(input("Digite o salário do funcionário R$ "))
print(f"O funcionário receberá R$ {salario + (salario * 15 / 100) :.2f} se receber um aumento de 15%") 