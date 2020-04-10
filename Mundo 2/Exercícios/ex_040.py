# Mostra médias de alunos

nota1 = float(input("1° nota do aluno: "))
nota2 = float(input("2° nota do aluno: "))
media = (nota1 + nota2) / 2

if media < 5:
    print(f"A média é {media:.2f}, o aluno está REPROVADO!!")
elif media >= 5 and media <= 6.9:
    print(f"A média é {media:.2f}, o aluno está de RECUPERAÇÃO!!")
else:
    print(f"A média é {media:.2f}, o aluno está APROVADO!!")