# Exercício 15
"""
Faça um código para validar se um determinado cpf é válido. 
O cpf deve ser informado no formato ddd.ddd.ddd-dd (onde d é um dígito de 0 a 9). 
Para validar o cpf, você deve seguir os seguintes passos:

A validação do CPF (Cadastro de Pessoas Físicas) é um processo que verifica se um número de CPF é válido ou não. O CPF é composto por 11 dígitos e possui um algoritmo específico para validação.

O algoritmo de validação do CPF é baseado em cálculos matemáticos que envolvem os dígitos do número. Aqui está uma descrição passo a passo de como é feita a validação do CPF:

1. Primeiro, é importante remover os caracteres especiais (como pontos e traços) do número do CPF, mantendo apenas os dígitos.
2. Em seguida, é necessário separar os 9 primeiros dígitos do CPF, que são os dígitos base para o cálculo dos dígitos verificadores.
3. Para calcular o primeiro dígito verificador, multiplicamos cada um dos 9 dígitos pela sequência decrescente de números de 10 a 2. Somamos os resultados dessas multiplicações.
4. O resultado da soma é dividido por 11. O dígito verificador é o resto da divisão. Se o resto for igual a 0 ou 1, o dígito verificador é 0. Caso contrário, subtraímos o resto de 11 para obter o dígito verificador.
5. Repetimos o mesmo processo para calcular o segundo dígito verificador, mas agora utilizamos os 9 dígitos do CPF original mais o primeiro dígito verificador calculado no passo anterior multiplicando agora esses dígitos pela sequência decrescente de 11 a 2.
6. Após calcular o segundo dígito verificador, temos o CPF completo com os 11 dígitos.
7. Para validar o CPF, comparamos os dígitos verificadores calculados com os dois últimos dígitos do CPF original. Se forem iguais, o CPF é considerado válido. Caso contrário, o CPF é considerado inválido.

Veja um exemplo em: https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
"""

def validar_cpf(cpf):
    # Remove caracteres especiais
    cpf = cpf.replace('.', '').replace('-', '')
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Se todos os dígitos forem iguais, o CPF é inválido
    if cpf == cpf[0] * len(cpf):
        return False

    # Calcula o primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    # Calcula o segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    # Verifica se os dígitos verificadores são iguais aos fornecidos
    return cpf[-2:] == f'{digito1}{digito2}'

# Solicita que o usuário insira o CPF
cpf_informado = input("Informe o CPF no formato ddd.ddd.ddd-dd: ")

# Valida o CPF
if validar_cpf(cpf_informado):
    print("O CPF informado é válido.")
else:
    print("O CPF informado é inválido.")