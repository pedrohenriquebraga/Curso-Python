# Mostra vogais

palavras = ("programar", "vencedor", "python",
"tutoriais", "jogar", "brincar", "javascript",
"ruby", "braga", "guanabara", "deschamps",
"web", "mobile", "rocketseat","programacao")

print("~" * 45)
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos as vogais:", end=" ")
    for i in p:
       if i in "aeiou":
           print(i.upper(), end=" ")
print()
print("~" * 45)