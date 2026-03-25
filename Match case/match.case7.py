print("CALCULADORA SIMPLES ")


num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))


match operacao:
    case "+":
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    case "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Erro: Não é possível dividir por zero!")
    case _:
        print("Operação inválida!")