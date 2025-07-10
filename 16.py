def contar_palavras(frase):
    contador = 0
    dentro_palavra = False

    for caractere in frase:
        if caractere != ' ' and not dentro_palavra:
            contador += 1
            dentro_palavra = True
        elif caractere == ' ':
            dentro_palavra = False

    return contador

print(contar_palavras("Eu gosto de chocolate")) 

