# Exercício 01
"""
Calcule a soma de todos os números pares de 1 a N, onde N é um número informado pelo usuário.

Exemplo de execução:
Digite um número: 10
A soma dos números pares de 1 a 10 é: 30
"""
contador = 1
soma = 0
numero = int(input("Digite um número inteiro: "))
while contador < numero:
  if contador%2 == 0:
    soma += contador

  contador+=1

print(soma)