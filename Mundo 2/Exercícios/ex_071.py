# CAIXA ELETRÔNICO

valor = int(input("Qual valor você quer sacar? = "))
total = valor
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédulas de R$ {ced:.2f}")
        if ced == 50:
            ced = 20
            totced = 0
        elif ced == 20:
            ced = 10
            totced = 0
        elif ced == 10:
            ced = 1
            totced = 0
        if valor == 0:
            break
print("OBRIGADO, VOLTE SEMPRE!!")
        