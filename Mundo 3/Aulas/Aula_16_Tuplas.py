# TUPLAS: Variáveis que guardam vários valores
# PARA BUSCAR ELEMENTOS EM TUPLAS, SE USA []
# PODE - SE USAR O len() EM TUPLAS
# TUPLAS SÃO IMUTÁVEIS
# enumerate() mostra a posição do elemento na tupla
# sorted() organiza a tupla em ordem alfabética
# tupla.count(elemento) conta quantas vezes um determinado elemento aparece na tupla
# tupla.index(elemento) mostra em que posição está um determinado elemento
# del(tupla) apaga uma tupla

lanche = ("Pudim", "Salada", "Suco", "Batata")
print(lanche[:])
# OU
for pos, item in enumerate(lanche):
    print(f"Eu vou comer: {item} na posição {pos}")