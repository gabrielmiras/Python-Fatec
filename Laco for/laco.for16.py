"""16. Contagem de Números Múltiplos de 3 e 5

Tarefa: Peça ao usuário um número N e exiba quantos números entre 1 e N são múltiplos de 3 ou 5.
"""
print("Contador de Múltiplos de 3 ou 5")

n = int(input("Digite o valor de N: "))
contador = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        contador += 1


print(f"Existem {contador} números entre 1 e {n} que são múltiplos de 3 ou 5.")