def palindromo(palavra):
    invertida = ""
    for letra in palavra:
        invertida = letra + invertida
    return palavra == invertida

print(palindromo("arara"))   
print(palindromo("carro"))   