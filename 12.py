def contar_vogais(palavra):
    v = ["a", "e", "i", "o", "u"]
    cont = 0 
    for vogal in palavra:
        if vogal in v:
            cont += 1
    return cont

print(contar_vogais("tardei"))
