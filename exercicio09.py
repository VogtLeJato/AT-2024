# Exercício 09
"""
Adrian, Bruno e Goran queriam se juntar ao clube dos amantes de pássaros. No entanto, eles não sabiam que todos os candidatos devem passar por um exame de admissão. O exame consiste em perguntas, cada uma com três possíveis respostas: A, B e C.

Infelizmente, eles não conseguiam distinguir um pássaro de uma baleia, então estão tentando adivinhar as respostas corretas. Cada um dos três garotos tem uma teoria sobre qual conjunto de respostas funcionará melhor:

Adrian afirma que a melhor sequência é: A B C A B C A B C A B C ...

Bruno está convencido de que esta é melhor: B A B C B A B C B A B C B ...

Goran ri deles e usará esta sequência: C C A A B B C C A A B B C C ...

O gabarito do exercício é dado na variável gabarito. 

Escreva um código que diga quanto cada questão cada um dos garotos acertou. Seu código deve conter comentários.
"""

gabarito = "BBCBCBBCAACABBACCCBCBCABBACBCACBCCBACACCCCABBCCCCABACAABBCAACACBABBACACBBBCABBABCAABCCCBABAAAAABBCBBCABABAAABCCCCACBBBCAABCBCBABCBCBABAACBCCCACAAABCCCCCABBAABACAACCABCBABACBBACCCCCAACBBBCBAACACCACAAAC"

# Função que monta um gabarito a partir da sequencia de carateres passada que será repetida até o tamanho do garito correto
def monta_gabarito(sequencia):
    gabarito_aluno = ""
    while len(gabarito_aluno) != len(gabarito):
        for i in range(0, len(sequencia)):
            gabarito_aluno += sequencia[i]
            if len(gabarito_aluno) == len(gabarito):
                return gabarito_aluno
    return gabarito_aluno

# Define as sequencias repetidas de cada aluno
sequencia_adrian = "ABC"
sequencia_bruno = "BABC"
sequencia_goran = "CCAABB"

# Obtém os gabaritos de cada um
gabarito_adrian = monta_gabarito(sequencia_adrian)
gabarito_bruno = monta_gabarito(sequencia_bruno)
gabarito_goran = monta_gabarito(sequencia_goran)

acertos_adrian = 0
acertos_bruno = 0
acertos_goran = 0

# Compara cada letra do gabarito com os gabaritos dos alunos
for i in range(len(gabarito)):
    if gabarito[i] == gabarito_adrian[i]:
        acertos_adrian += 1
    if gabarito[i] == gabarito_bruno[i]:
        acertos_bruno += 1
    if gabarito[i] == gabarito_goran[i]:
        acertos_goran += 1

# Printa os resultados
print(f"Adrian acertou {acertos_adrian}.")
print(f"Bruno acertou {acertos_bruno}.")
print(f"Goran acertou {acertos_goran}.")
