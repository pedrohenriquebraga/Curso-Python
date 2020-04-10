# Modularização para moeda

from utilidadescev import moeda
from utilidadescev import dado

v = dado.leiaDinheiro("Digite um valor: R$ ")
moeda.resumo(v)