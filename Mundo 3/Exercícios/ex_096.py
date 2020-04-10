# Função para área de terrenos

def área(larg, comp):
    área = larg * comp
    print(f"A área do terreno({larg} x {comp}) é de {área}M²")


larg = float(input("Digite a largura(m): "))
comp = float(input("Digite o comprimento(m): "))
área(larg, comp)