print("Tabuada Personalizada")
numero = int(input("Me dê um número para a tabuada: "))
numero2= int(input("Digite onde a tabuadad vai parar:"))


for i in range(numero, numero2+1,1):
    resultado = numero * i

    if resultado % 3 == 0:
        print(f"{numero} x {i} = Múltiplo de 3")
    else:
        print(f"{numero} x {i} = {resultado}")