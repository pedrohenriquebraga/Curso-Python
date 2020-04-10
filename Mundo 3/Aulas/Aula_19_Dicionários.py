# {} para declarar dicionários ou dict()
# del deleta dados
# Valor = dados do dicionário (dicionário.values())
# Chaves(keys) = identificadores do dicionário (dicionário.keys())
# Para pegar as keys junto com os values = dicionário.items()
# 

"""pessoas = {"nome":"Pedro", "sexo":"M", "idade":14}

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print("~" * 40)
for k, v in pessoas.items():
    print(f"{k} = {v}")"""

"""estado1 = {"uf":"Rio De Janeiro", "sigla":"RJ"}
estado2 = {"uf":"Goiás", "sigla":"GO"}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]["sigla"])"""

estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input("Estado: "))
    estado["sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
