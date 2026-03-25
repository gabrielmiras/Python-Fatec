login_digitado = input("Digite o usuário: ")
senha_digitada = input("Digite sua senha: ")

logincerto = "Admin"
senhacerta = "123"

if login_digitado == logincerto and senha_digitada == senhacerta:
    print(" Logado com sucesso!")
else:
    if login_digitado != logincerto:
        print(" Erro: Usuário não encontrado.")
    else:
        print(" Erro: Senha incorreta.")