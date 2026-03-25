"""
10. Fatorial de um Número

Tarefa: Solicite um número ao usuário e exiba o seu fatorial (n!).
"""

print("Fatorial de um Número")
numero=int(input("Digite o número para descobriri seu fatorial: "))

fatorial=numero

for i in range(numero-1,1,-1):
        fatorial *= int(i)
print(f"O fatorial de {numero} é {fatorial}")