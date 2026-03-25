# Solicita a idade ao usuário
# O input sempre retorna uma string, por isso usamos int() para converter em número
idade = int(input("Digite a sua idade: "))

# Verifica a condição
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")