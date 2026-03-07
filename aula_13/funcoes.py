# 1 - Número aleatório entre 5 e 10

import random

def numero_aleatorio_5_10():
    numero = random.randint(5, 10)
    return numero

# 2 - Criar 3 números aleatórios
def tres_numeros_aleatorios():
    lista = []

    for i in range(3):
        num = random.randint(1, 100)
        lista.append(num)

    return lista


# 3 - Número aleatório entre 10 e 30 usando range
def numero_aleatorio_10_30():
    numeros = list(range(10, 31))
    num = random.choice(numeros)
    return num

# 4 - Contagem regressiva
def contagem_regressiva():
    for i in range(10, 0, -1):
        print(i)

    print("Fogo!")


# 5 - Soma de números pares
def soma_pares(numero):
    soma = 0

    for i in range(2, numero + 1):
        if i % 2 == 0:
            soma = soma + i

    return soma

# 6 - Tabuada
def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)


# 7 - Números ímpares reversos
def impares_reversos():
    for i in range(99, 0, -1):
        if i % 2 != 0:
            print(i)
