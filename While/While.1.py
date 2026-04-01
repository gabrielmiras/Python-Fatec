"""Soma de Números: Crie um programa que solicite ao usuário para inserir números e some esses números até que o usuário insira zero. Quando zero for inserido, o programa deve imprimir a soma total."""
soma = 0
numero = 1

print("Digite os números (0 para sair):")

while numero != 0:
    numero = float(input("Digite um número: "))
    soma = soma + numero

print("O total é:", soma)