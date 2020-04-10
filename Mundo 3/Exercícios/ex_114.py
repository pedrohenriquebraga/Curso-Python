# Ver se o site "pudim.com.br" está acessível

import requests

try:
    url = "http://www.pudim.com.br"
    requests.get(url)
except:
    print("\033[1;31mO SITE NÃO ESTÁ ACESSÍVEL\033[m")
else:
    print("\033[1;32mO SITE ESTÁ ACESSÍVEL\033[m")