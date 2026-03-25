print(" Sistema de Reserva de Passagens")
passagens=input("Para qual lugar você vai?(São Paulo, Rio de Janeiro, Curitiba, Salvador): ").lower()

match passagens:
    case "salvador":
        print("A passagem custa R$ 100 reais ")
    case "são paulo" | "sao paulo":
        print("A passagem custa R$120 reais")
    case "rio de janeiro":
        print("A passagem custa R$80 reais  ")
    case "curitiba":
        print("A passagem custa R$65 reais ")