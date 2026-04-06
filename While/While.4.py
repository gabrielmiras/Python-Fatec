"""
Conversão de Temperatura: Faça um programa que converta uma temperatura de Celsius para Fahrenheit.
Continue pedindo ao usuário para inserir uma nova temperatura em Celsius até que ele digite "sair".
"""

print("Conversão de temperatura em Fahrenheit")

while True:
    temperatura=float(input("Digite a temperatura em Celsius : "))
    if temperatura==str("sair"):
        break
    fahrenheit=(temperatura*1.8)+32
    print(f"Os {temperatura}º Celsius em Fahrenheit são : {fahrenheit:.2f}ºF")
print("Conversão finalizada")
