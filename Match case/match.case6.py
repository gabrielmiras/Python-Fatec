print("Simulação de agendamento telefônico")
usuario=input("Selecione uma opção de atendimento, Suporte Técnico,Financeiro,Cancelamento ou Falar com um atendente: ").lower()
match usuario:
    case "suporte técnico"| "suporte tecnico":
        print("Digite 1 para suporte")
    case "financeiro":
        print("Digite 2 para financeiro")
    case "cancelamento":
        print("Digite 3 para cancelamento")
    case "atendente":
        print("Digite 4 para atendente")