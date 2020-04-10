# Função para linha adaptativa

def escreva(msg):
    print("~" * (len(msg) + 2))
    print(f" {msg} ")
    print("~" * (len(msg)+2))


msg = str(input("Escreva uma mensagem: "))
escreva(msg)