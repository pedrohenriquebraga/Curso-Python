# Sorteia um nome entre 4 nomes

from random import choice

alunos = list()
for c in range(0, 4):
    alunos.append(str(input(f"Nome do {c + 1}° aluno: ")))
print(f"O aluno escolhido para apagar o quadro foi o(a) {choice(alunos)}")