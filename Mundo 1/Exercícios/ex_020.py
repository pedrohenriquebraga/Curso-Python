# Embaralha nomes

from random import shuffle

alunos = []
for c in range(0, 4):
    alunos.append(str(input(f"{c + 1}° aluno: ")))
shuffle(alunos)
print(f"A ordem de apresentação será:")
for i in alunos:
    print(i, end=" ")
