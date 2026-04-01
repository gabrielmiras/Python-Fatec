"""Quantidade de valores: Conte quantos valores positivos, negativos
e zeros foram digitados."""
negativos=0
positivos=0
zeros=0
print("Contadores de valores positivos,negativos e zero")


while True:
    numero=input("Digite os números:")
    if numero=="sair":
        break
    elif float(numero)<0:
        negativos+=1
    elif float(numero)==0:
        zeros+=1
    elif float(numero)>0:
        positivos+=1
print(f"{positivos} foram positivos, {negativos} foram negativos e {zeros} foram zero")