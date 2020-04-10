def leiaDinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[1;31mERRO!! '{entrada}' NÃO É VÁLIDO!!\033[m")
        else:
            break
    return float(entrada)