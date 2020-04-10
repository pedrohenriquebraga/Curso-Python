# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# // Divisão Inteira
# % Resto da Divisão
# ** Potência

""" ORDEM DE PROCEDÊNCIA """

# 1° ()
# 2° Potência
# 3° Multiplicação, divisão(todas)
# 4° Adição e subtração

# Comando alternativo para fazer portencia pow()
# Pode-se achar a raiz quadrada com número**(1/2)

nome = str(input("Seu nome: "))

# COLOCA ESPAÇOS NA FRENTE
print("PRAZER EM CONHECER VOCÊ, {:20}".format(nome))

# Coloca espaços a direita
print("PRAZER EM CONHECER VOCÊ, {:>20}".format(nome))

# Coloca espaços a esquerda
print("PRAZER EM CONHECER VOCÊ, {:<20}".format(nome))

# CENTRALIZA O QUE DESEJAR ENTRE OS ESPAÇOS
print("PRAZER EM CONHECER VOCÊ, {:^20}".format(nome))

#SUBSTITUI OS ESPAÇOS PELO O QUE DESEJAR
print("PRAZER EM CONHECER VOCÊ, {:=^20}".format(nome))