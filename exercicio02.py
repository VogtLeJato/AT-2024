# Exercício 02
"""
Crie uma lista com números que o usuário informar até que ele digite 'q'.
Exiba a soma dos números informados, a média e o desvio-padrão.
Não utilize bibliotecas ou funções para o cálculo da soma, média e desvio padrão.

Exemplo de execução:
Digite um número (q para sair): 5
Digite um número (q para sair): 10
Digite um número (q para sair): -3
Digite um número (q para sair): q
A soma dos números informados é: 12
A média dos números informados é: 4
O desvio-padrão dos números informados é: 6.5574

No moodle, é possível ver a fórmula para cálculo do desvio padrão.
Veja um exemplo em: https://pt.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/a/population-and-sample-standard-deviation-review


"""
saiu = False
numeros = []
print("Digite mais de 1 número, para parar de digitar números, digite 'q'")

while not saiu:
    entrada = input("Digite um número (q para sair): ")
    if entrada == 'q':
        saiu = True
    else:
        numeros.append(float(entrada))

soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)

soma_quadrados = 0
for numero in numeros:
    soma_quadrados += (numero - media) ** 2

desvio_padrao = (soma_quadrados / len(numeros)) ** 0.5

print(f"Soma é: {soma}")
print(f"Média é: {media}")
print(f"Desvio-padrao é: {desvio_padrao}")

    