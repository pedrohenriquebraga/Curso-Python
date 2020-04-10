def ExisteArq(nome):
    try:
        open(nome, "rt")
    except:
        return False
    else:
        return True

def CriarArq(nome):
    try:
        open(nome, "wt+")
    except:
        print("HOUVE UM ERRO!!")
    finally:
        nome.close()
        
def cadastrar(nome="<desconhecido>", idade=0):
    try:
        arq = open("cadastros", "r")
    except:
        return print("ERRO AO TENTAR ABRIR O ARQUIVO")
    else:
        try:
            conteudo = arq.readlines()
            conteudo.append(nome + "\n")
            conteudo.append(str(idade) + "\n")
            arq = open("cadastros", "w")
            arq.writelines(conteudo)
            arq.close()
        except:
            return print("ERRO AO TENTAR GRAVAR INFORMAÇÃO")
        else:
            print(f"REGISTRO {nome} CADASTRADO COM SUCESSO")

def listar():
    arq = open("cadastros", "r")
    conteu = arq.readlines()
    pessoas = []
    for cont in conteu:
        pessoas.append(cont.replace("\n", ""))
    for v, i in enumerate(pessoas):
        if v % 2 == 0:
            print(f"{i:<30}",end="")
        else:
            print(f"\t{i:<3} anos")

def limpaCadastro():
    arq = open("cadastros", "w")
    arq.close()