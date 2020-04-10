from Comandos import cadastrar
from Comandos.cadastrar import * 
from Comandos import interface
from Comandos.interface import *
from time import sleep

resp = ExisteArq("cadastros")
if resp is False:
    CriarArq("cadastros")

PrintPerso("SISTEMA DE CADASTROS")

while True:
    resp = menu(["Limpar Cadastro", "Ver Pessoas Cadastradas", "Cadastrar Nova Pessoa", "Sair Do Sistema"])
    
    if resp == 0:
        PrintPerso("LIMPAR CADASTRO")
        limpaCadastro()
        
    if resp == 1:
        PrintPerso("LISTAGEM DE PESSOAS")
        listar()
        
    if resp == 2:
        PrintPerso("NOVO CADASTRO")
        
        nome = str(input("Digite o nome: ")).title().strip()
        idade = ValidaOp("Digite a idade: ", False)
        cadastrar(nome, idade)
        
    if resp == 3:
        PrintPerso("ATÉ LOGO!! MUITO OBRIGADO!!")
        sleep(1)
        break
            
        