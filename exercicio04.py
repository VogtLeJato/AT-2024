# Exercício 04
"""
Escreva um código que peça um número para o usuário e responda se ele é primo ou não.
Lembrando que um número primo é um número maior que 1 que só pode ser dividido por 1 e por ele mesmo.
Seu código deve conter comentários.
"""

def numero_e_primo(num):
    # se numero for menor ou igual a 1, não é primo
    if num <= 1:
        return False
    # Verifica se o número é divisível por qualquer número de 2 até a raiz quadrada do número
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:  # Se for divisível, não é primo
            return False
    return True  # Se não for divisível por nenhum, é primo

# Pede um número para o usuário
numero = int(input("Digite um número: "))

# Chama a função e verifica se o número é primo
if numero_e_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
