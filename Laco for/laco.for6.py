"""
6. Soma dos Números de 1 a N

Tarefa: Solicite um número ao usuário e exiba a soma de 1 até esse número.
"""
import time
print("Sona dos números de 1 a N")

numero=int(input("Digite o número que desejar:"))

for n in range(1,numero+1):
    print(n)
    time.sleep(0.5)
