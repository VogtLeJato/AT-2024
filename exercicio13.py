# Exercício 13
"""
Escreva um programa que dado as variaveis lista0 e lista1, crie uma nova lista na variável lista_intersecao contendo apenas os elementos que estão presentes em ambas as listas.
"""

lista0 = [7, 15, "a", "r", "o", "c", 17, 7, "w", "b"]
lista1 = ["b", "o", 7, 3, 2, "x", "d", 6, "w", "n"]


lista_intersecao = None

lista_intersecao = list(set(lista0) & set(lista1))

print(lista_intersecao)
