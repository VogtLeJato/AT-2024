# Exercício 12
"""
Quando eu como meus Skittles, sempre como os vermelhos por último. Eu os separo em grupos de cores e começo comendo os laranjas, depois os azuis, verdes, amarelos, rosas, violetas, marrons e, finalmente, os vermelhos. Os vermelhos são os melhores, então eu os como devagar, um de cada vez. As outras cores eu como rapidamente aos punhados (minha mão pode segurar no máximo 7 Skittles). Eu sempre termino todos os Skittles de uma cor antes de passar para a próxima, então às vezes o último punhado de uma cor não está completamente cheio. Mas espere, tem mais! Eu transformei meu hábito de comer Skittles em uma ciência. Eu sei que sempre levo exatamente 13 segundos para comer um punhado de Skittles que não são vermelhos e ajusto minha taxa de mastigação para que eu sempre leve 13 segundos, mesmo que minha mão não esteja completamente cheia. Quando como os Skittles vermelhos, gosto de levar meu tempo, então levo exatamente 16 segundos para comer cada um. Eu tenho uma grande caixa de Skittles. Depois de terminar de separar as cores, quanto tempo levará para comê-los? 

 Abaixo está uma lista de cores de Skittles em minha caixa. Cada cor é representada por uma string.
"""

saco_de_skittles = [
    "vermelho",
    "marrom",
    "marrom",
    "violeta",
    "azul",
    "rosa",
    "azul",
    "azul",
    "rosa",
    "marrom",
    "amarelo",
    "marrom",
    "rosa",
    "violeta",
    "verde",
    "amarelo",
    "vermelho",
    "laranja",
    "laranja",
    "azul",
    "marrom",
    "rosa",
    "vermelho",
    "vermelho",
    "vermelho",
    "marrom",
    "laranja",
    "laranja",
    "verde",
    "vermelho",
    "laranja",
    "violeta",
    "azul",
    "rosa",
    "amarelo",
    "rosa",
    "marrom",
    "laranja",
    "verde",
    "vermelho",
    "azul",
    "amarelo",
    "verde",
    "laranja",
    "marrom",
    "laranja",
    "rosa",
    "violeta",
    "marrom",
    "vermelho",
]

print(set(saco_de_skittles))
cores_skittles = set(saco_de_skittles)
cores_skittles.remove("vermelho")
print(cores_skittles)

quantidade_de_segundos = 0
for cor in cores_skittles:
    quantidade_de_skitttles_da_cor = saco_de_skittles.count(cor)
    print((quantidade_de_skitttles_da_cor // 7) + 1)
    quantidade_de_segundos += ((quantidade_de_skitttles_da_cor // 7) + 1) * 13

quantidade_de_skitttles_vermelhos = saco_de_skittles.count("vermelho")
quantidade_de_segundos += quantidade_de_skitttles_vermelhos * 16

print(quantidade_de_segundos)
