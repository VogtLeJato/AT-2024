# Exercício 06
"""
No TP-2, Alice e Bob inventaram o seguinte método para codificar mensagens:
1) Dividem a mensagem ao meio
2) A primeira metade da mensagem vai ocupar as posições pares do texto. Já a segunda metade vai ocupar as posições ímpares. Considerando que a primeira posição é a 0.

Por exemplo, a mensagem "Olá Alice." seria transformada em:

        posicao |0 1 2 3 4 5 6 7 8 9 
           pares|O # l # á #   # A #    
        ímpares |# l # i # c # e # .
         ____________________________
         
mensagem_encriptada = Olliác eA.
(Veja no moddle uma figura com esse exemplo)

A sua tarefa agora é escrever o código para ENCRIPTAR a mensagem. A mensagem a ser encriptada está definida na variável mensagem_original. Seu código deve conter comentários.
"""

mensagem_original = "Olá Alice! Resolvi mudar nossa criptografia, acredito que nossa última mensagem foi interceptada. Mas agora com esse novo método ninguém vai conseguir ler nossas mensagens."

# Acha o meio
posicao_meio = len(mensagem_original) // 2

# Primeira metade da mensagem
primeira_metade = mensagem_original[:posicao_meio]

# Segunda metade da mensagem
segunda_metade = mensagem_original[posicao_meio:]

mensagem_encriptada = ""

# Monta a mensagem, intercalando uma letra de cada metade.
i = 0
while i <= len(primeira_metade):
    if i < len(primeira_metade):
        mensagem_encriptada += primeira_metade[i]
        mensagem_encriptada += segunda_metade[i]
    i += 1

# Exibe a mensagem encriptada
print(mensagem_encriptada)

