"""18. Números Múltiplos de 3 e 5

Tarefa: Peça ao usuário um número N e exiba todos os números de 1 até N que são múltiplos de 3 e 5.
"""

print("Múltiplos de 3 E 5 ")
n = int(input("Digite o valor de N: "))


resultados = []


for i in range(1, n + 1):


    if i % 3 == 0 and i % 5 == 0:
        resultados.append(i)


print("-" * 30)
if len(resultados) > 0:
    print(f"Os números entre 1 e {n} que são múltiplos de 3 e 5 são:")
    print(resultados)
    print(f"Total encontrado: {len(resultados)} números.")
else:
    print(f"Nenhum número entre 1 e {n} é múltiplo de 3 e 5 ao mesmo tempo.")