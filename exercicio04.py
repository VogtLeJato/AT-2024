# Exercício 04
"""
Escreva um código que peça um número para o usuário e responda se ele é primo ou não.
Lembrando que um número primo é um número maior que 1 que só pode ser dividido por 1 e por ele mesmo.
Seu código deve conter comentários.
"""

numero_e_primo = True

# Pede um número para o usuário
numero = int(input("Digite um número: "))

# se numero for menor ou igual a 1, não é primo
if numero <= 1:
    numero_e_primo = False

# Verifica se é divisível por algum número entre 2 e ele mesmo
for i in range(2, numero - 1):
    if numero % i == 0:
        numero_e_primo = False

# Printa o resultado
if numero_e_primo:
    print("É um número primo.")
else:
    print("Não é um número primo.")
