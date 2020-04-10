# Nome e situação de um aluno em um dicionário

aluno = {}

aluno["nome"] = str(input("Nome: ")).title()
aluno["média"] = float(input(f"Média de {aluno['nome']}: "))

if aluno["média"] >= 7:
    aluno["situacao"] = "APROVADO!!"
elif 5 <= aluno['média'] < 7:
    aluno["situacao"] = "RECUPERAÇÃO"
else:
    aluno["situacao"] = "REPROVADO!!"
print(f"O aluno {aluno['nome']} com média de {aluno['média']} está {aluno['situacao']}")