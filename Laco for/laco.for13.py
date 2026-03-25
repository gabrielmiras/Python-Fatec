"""
13. Soma dos Números Pares e Ímpares

Tarefa: Peça um número ao usuário e some separadamente os pares e os ímpares de 1 até esse número.
"""
print("Soma dos Números Pares e Ímpares")
numero=int(input("Digite um número:"))
soma_pares = 0
soma_impares = 0


for i in range(1, numero + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i

print(f"Soma dos pares: {soma_pares}")
print(f"Soma dos ímpares: {soma_impares}")