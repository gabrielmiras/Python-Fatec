"""'
2. Contagem Personalizada

Tarefa: Peça ao usuário um número e exiba uma contagem de 1 até esse número.
"""''
import time

print("Contagem Personalizada")
end=int(input("A calculadora vai contar de 1 até o número que você colocar :"))
for contagem in range (1,end+1,+1):
    print(contagem)
    time.sleep(0.5)