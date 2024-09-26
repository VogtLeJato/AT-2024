# Exercício 03
"""
Escreva um programa que recebe uma lista de números inteiros do usuário.
O programa deve criar uma nova lista contendo apenas os números pares da lista original e imprimi-la.

Exemplo de execução:
Entre com os números separados por espaço: 1 2 3 4 5 6
Números pares: [2, 4, 6]
"""

entrada = input("Digite numeros separados por espaço: ")

numeros = []
for num in entrada.split():
    numeros.append(int(num))

numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print("Números pares:", numeros_pares)
