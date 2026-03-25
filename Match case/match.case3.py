print("Sistema de login")
usuario=input("Qual o seu usuário?").lower()
match usuario:
    case "admin":
        print(f"Você tem acesso total")
    case "professor":
        print(f"Você tem acesso ao ambiente acadêmico")
    case "Aluno":
        print("Você tem acesso ao ambiente de estudos ")

