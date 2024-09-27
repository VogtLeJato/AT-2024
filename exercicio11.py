# Exercício 11
"""
Dado as duas listas de números inteiros abaixo, crie uma nova lista de mesmo tamanho onde cada elemento é a soma dos elementos correspondentes das listas originais.
Imprima o valor das listas originais e da lista resultante.

Exemplo de execução:
lista0: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista_resultante: [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
"""

import random

lista0 = random.sample(range(1, 100), 10)
lista1 = random.sample(range(1, 100), 10)

lista_somada = []
for i in range(0, 10):
    lista_somada.append(lista0[i] + lista1[i])

print(f"Lista original 0: {lista0}")
print(f"Lista original 1: {lista1}")
print(f"Lista somada: {lista_somada}")