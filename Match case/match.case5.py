print("Leitor de cores em inglês")
cor=input("Escolha uma cor dentre (vermelho, azul, verde, amarelo) : ").lower()

match cor:
    case "vermelho":
        print("Vermelho em inglês é Red")
    case "azul":
        print("Azul em inglês é Blue")
    case "amarelo":
        print("Amarelo em inglês é yellow")
    case "verde":
        print("Verde em inglês é green")