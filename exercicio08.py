# Exercício 08
"""
Calcule o fatorial de um número informado pelo usuário.
O fatorial de um número n é o produto de todos os inteiros de 1 até n.

Exemplo de execução:
Digite um número: 5
O fatorial de 5 é 120
"""
numero = int(input("Digite um número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial desse número é: {fatorial}")

