# Informações do Brasileirão

brasileirao = ("Flamengo", "Santos", "Palmeiras", "Grêmio", "Athletico-PR",
"São Paulo", "Internacional", "Corinthians", "Fortaleza",
"Goiás", "Bahia", "Vasco da Gama", "Atlético-MG", "Fluminense",
"Botafogo", "Ceará SC", "Cruzeiro","CSA", "Chapecoense", "Avaí")
chapecoense = brasileirao.index("Chapecoense")

print()
print(f"{'BRASILEIRÃO 2019':^50}")
print()

print("OS 5 PRIMEIROS COLOCADOS: ")
print("~" * 50)
for item in brasileirao[0:5]:
    print(f"{item:^50}")

print("~" * 50)
print("OS 4 ÚLTIMOS COLOCADOS: ")
print("~" * 50)
for item in brasileirao[16:]:
    print(f"{item:^50}")

print("~" * 50)
print("OS TIMES PARTICIPANTES: ")
print("~" * 50)
for item in sorted(brasileirao):
    print(f"{item:^50}")

print("~" * 50)
print(f"A Chapecoense ficou em {chapecoense + 1}° na competição")
