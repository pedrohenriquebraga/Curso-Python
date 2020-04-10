# Mini-Menu para Interactive Help

from time import sleep

cores = {"limpa":"\033[m", 
"azul":"\033[7;36m",
"roxo":"\033[7;35m", 
"negrito":"\033[1m",
"branco":"\033[7m", 
"verde":"\033[7;32m",
"amarelo":"\033[33m",
"vermelho":"\033[7;31m"}

while True:
    print(f"{cores['verde']}=" * 50)
    print(f"{'SISTEMA DE AJUDA PYHELP':^50}")
    print("=" * 50), print(f"{cores['limpa']}")
    
    funcao = str(input(f"{cores['negrito']}QUAL COMANDO VOCÊ QUER PESQUISAR?[FIM para] = "))
    if funcao.upper() == "FIM":
        break
    print()
    print(f"{cores['azul']}=" * 50)
    print(f"{f'ACESSANDO PYHELP PARA {funcao.upper()}':^50}")
    print("=" * 50)
    
    sleep(1)
    
    print(f"{cores['amarelo']}")
    print(help(funcao))
    print()

print(f"{cores['vermelho']}=" * 50)
print(f"{'ATÉ LOGO':^50}")
print("=" * 50)