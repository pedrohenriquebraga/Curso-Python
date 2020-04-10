# Função para votantes

def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f"COM {idade} ANOS SEU VOTO É NEGADO!!"
    if 16 <= idade < 18 or idade > 65:
        return f"COM {idade} ANOS SEU VOTO É OPCIONAL!!"
    else:
        return f"COM {idade} ANOS SEU VOTO É OBRIGATÓRIO!!"
        
        
ano = int(input("EM QUE ANO VOCÊ NASCEU?: "))
print(voto(ano))