# Ficha de alunos com funções

sala = dict()

def notas(*n, sit=False):
    sala["total"] = len(n)
    sala["maior"] = max(n)
    sala["menor"] = min(n)
    sala["média"] = sum(n) / len(n)
    if sit == True:
        if sala["média"] < 6:
            sala["situação"] = "RUIM"
        if sala["média"] == 6:
            sala["situação"] = "RAZOÁVEL"
        if sala["média"] > 7:
            sala["situação"] = "ÓTIMA"
    return sala
    
    
resp = notas(10, 9.8, 8.5, sit=True)
print(resp)