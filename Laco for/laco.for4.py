"""
4. Contagem com Passo Personalizado

Tarefa: Peça ao usuário três números: início, fim e passo e exiba a sequência correspondente.
"""

print("Contagem com Passo Personalizado")
ini=int(input("inicio: "))
fim=int(input("fim: "))
passo=int(input("passo: "))
print(f"\n Sequência de {ini} até {fim} com passo {passo}=")
for c in range (ini,fim+1,passo):
    print(c)