# Verifica se o nome de uma cidade começa com Santo

city = str(input("Digite o nome de uma cidade: ")).title().strip
city = city.split()[0]
santo = 'Santo' in city
print(f"É {santo}")
