# Exercício 10
"""
Peça ao usuário para informar um número e exiba a tabuada de multiplicação desse número de 1 a 10.

Exemplo de execução:
Informe um número: 5
A tabuada de 5 é:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""

def monta_tabuada(numero_tabuada):
    print(f"A tabuada de {numero_tabuada} é: ")
    for i in range(1, 10 + 1):
        print(f"{numero_tabuada} x {i} = {numero_tabuada * i}")

numero = int(input("Informe um número para apresentar a tabuada: "))
monta_tabuada(numero)
