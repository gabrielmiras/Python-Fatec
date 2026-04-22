"""Simulação de Dados de Sensor: Crie um programa que simule a leitura de dados de um sensor e continue
capturando dados até que um valor fora do intervalo de operação seja detectado (por exemplo, fora de 0 a 100).
"""

print("Simulação de Análise de Dados" )
contador = 0
while True:
    leitorddados=int(input("Digite os dados a serem analisados ao máximo de 100:"))
    contador   +=  leitorddados

    if leitorddados >=0 and leitorddados <=100:
     print(f"Dados analisados e armazenados , quantidade de dados armazenado: {contador}")
    elif leitorddados < 0 or leitorddados > 100:
        print("Dados fora do limite , digite dados de 0 a 100")
        break

