# Nota de vários alunos em listas

from time import sleep
ficha = list()

while True:
    print("~" * 40)
    aluno = str(input("Nome: ")).title()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([aluno, [nota1, nota2], media])
    resp = str(input("Quer continuar? [S/N]: "))
    if resp in "Nn":
        break
print("=" * 40)       
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("=" * 40)

for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.2f}")
while True:
    print("=" * 40)
    opc = int(input("Mostrar nota de qual aluno(999 interrompe)? = "))
    if opc == 999:
        print("FINALIZANDO...")
        sleep(2)
        break
    if opc <= len(ficha):
        print(f"As notas do aluno {ficha[opc][0]} são {ficha[opc][1]}")
print("~" * 40)
print("PROGRAMA FINALIZADO!")