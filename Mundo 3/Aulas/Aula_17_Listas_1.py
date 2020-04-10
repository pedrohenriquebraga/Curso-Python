# PARA ADICIONAR ELEMENTOS A LISTAS USAMOS: lista.append(elemeto ser adicionado)
# PARA ADICIONAR ELEMENTOS EM LUGARES ESPECÍFICOS DA LISTA USAMOS:
# lista.insert(posição a ser adicionada, o que vai ser adicionado)
# PARA EXCLUIR ELEMENTOS: del lista[elemento]
# Também pode - se usar o lista.pop(elemento)
# OUTRA MANEIRA É USAR O lista.remove(valor a ser eliminado)
# PARA ORGANIZAR UMA LISTA USAMOS lista.sort()
# PARA ORGANIZAR EM ORDEM INVERSA USAMOS lista.sort(reverse=True)

num = []
num.append(5)
num.append(9)
num.append(3)

for c, v in enumerate(num):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Acabou a lista!")