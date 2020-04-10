# Validação de Resposta

sexo = str(input("Digite o sexo da pessoa[M/F]: ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("SEXO INVÁLIDO!! Digite um sexo válido[M/F]: ")).strip().upper()[0]