# Exercício 05
"""
Escreva um programa que dado o valor de N da variável abaixo calcula o valor da soma:
1 + 1/2 + 1/3 + 1/4 + ... + 1/N

Exemplo de execução:
Se N = 4,
o programa deverá calcular:
1 + 1/2 + 1/3 + 1/4 = 2.083333333333333

Saída esperada:
2.083333333333333
"""

numero = int(input("Digite um número: "))
soma = 0.0

for i in range(1, numero + 1):
    soma += 1 / i

print(soma)
