"""Peça ao usuário para digitar 5 nomes e armazene-os em uma lista. Depois, exiba os nomes um por um."""
lista_nomes = []
for i in range(5):
    nome=input(f"Digite o {i+1}º nome: ")
    lista_nomes.append(nome)

for nome in lista_nomes:
    print(nome)