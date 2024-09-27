# Exercício 14
"""
    Crie um jogo onde o computador escolhe um número aleatório entre 1 e 100 e o usuário tenta adivinhá-lo.
    O programa deve informar se o palpite do usuário é maior ou menor que o número escolhido.

    Exemplo de execução (supondo que o computador escolheu o número 42):

    Computador escolhe um número secreto
    Usuário faz o palpite: 50
    Saída: "Seu palpite é maior que o número escolhido."

    Usuário faz o palpite: 30
    Saída: "Seu palpite é menor que o número escolhido."

    Usuário faz o palpite: 42
    Saída: "Parabéns! Você adivinhou o número!"
"""

import random

numero_secreto = random.randint(1, 100)

print("Computador escolhe um número secreto entre 1 e 100.")
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Usuário faz o palpite: "))
    
    if tentativa < numero_secreto:
        print("Seu palpite é menor que o número escolhido.")
    elif tentativa > numero_secreto:
        print("Seu palpite é maior que o número escolhido.")
    else:
        print("Parabéns! Você adivinhou o número!")