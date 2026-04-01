"""Encontrar o Máximo: Crie um programa que peça ao usuário para inserir
números e encontre o maior número inserido.
 O programa deve continuar pedindo números até que o usuário digite "sair"."
"""
print("Digite números para podermos ver o maior (digite 'sair' para parar)")
compare=-9999999999999999999999999999999999999
while True:
    numero= input("Digite o número:")
    if numero =="sair":
        break
    elif float (numero)>(compare):
        compare=float(numero)
    print(f"O maior número é o {compare}")
print("Acabou mano")
