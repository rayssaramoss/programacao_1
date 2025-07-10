def analisa_lista(lista):
    maior = lista[0]
    menor = lista[0]
    soma = 0
    
    for numero in lista:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        soma += numero

    media = soma / len(lista)

    return maior, menor, media

valores = [10, 5, 20, 7]
maior, menor, media = analisa_lista(valores)

print("Maior:", maior)
print("Menor:", menor)
print("Média:", media)