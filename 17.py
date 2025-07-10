import random

def simular_dado(n):
    resultados = []
    for i in range(n):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados

rolagens = simular_dado(5)
print(rolagens)
