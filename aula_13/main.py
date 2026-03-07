import funcoes


print("1 - Número aleatório de 5 a 10")
print(funcoes.numero_aleatorio_5_10())

print("\n2 - Três números aleatórios")
print(funcoes.tres_numeros_aleatorios())

print("\n3 - Número aleatório entre 10 e 30")
print(funcoes.numero_aleatorio_10_30())

print("\n4 - Contagem regressiva")
funcoes.contagem_regressiva()

num = int(input("Digite um número inteiro positivo: "))

resultado = funcoes.soma_pares(num)

print("A soma dos números pares é:", resultado)

print("\n6 - Tabuada")
numero = int(input("Digite um número para ver a tabuada: "))
funcoes.tabuada(numero)

print("\n7 - Ímpares reversos")
funcoes.impares_reversos()