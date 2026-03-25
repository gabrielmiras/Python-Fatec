print("Calculadora de áreas geométricas")
forma=input("Qual forma você quer calcular?").lower()
match forma:
    case "quadrado":
        quadrado = float(input("Qual a base ou lado do quadrado em cm"))
        print(f"A área do quadrado é {quadrado*2}")
    case "triangulo" | "triângulo":
        triangulo1 = float(input("Qual a altura dele:"))
        triangulo2 = float(input("Qual a base dele:"))
        print(f"A área do triângulo é {triangulo2 * triangulo1/2 }")
    case "retangulo" | "retângulo":
        retangulo1 = float(input("Qual a base dele: "))
        retangulo2 = float(input("Qual a altura dele: "))
        print(f"A área do retângulo é {retangulo1 * retangulo2}:")