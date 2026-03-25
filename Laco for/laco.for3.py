"""
3. Contagem Regressiva

Tarefa: Exiba uma contagem regressiva de 10 até 1 e, ao final, exiba "Fogo!".
"""

import time


for i in range(10, 0, -1):
    print(i)
    time.sleep(0.4  )

print("Fogo!")
