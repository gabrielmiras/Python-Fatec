"""
7. Tabuada de um Número

Tarefa: Peça ao usuário um número e exiba a tabuada desse número de 1 a 10.
"""


numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 21):
    print(f"{numero} x {i} = {numero * i}")
