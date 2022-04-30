from random import randint

max_vetor = None
max_n = None
max_l = None
maxi_l = None
matriz = []

indices = []
for linha in range(10):
    linha = []

    for coluna in range(10):
        linha.append(randint(0, 1000))

    matriz.append(linha)

for linha_matriz in matriz:
    print(linha_matriz)

for indice, numero in enumerate(matriz):

    if (max_vetor is None or numero > max_vetor):
        max_vetor = numero
        max_n = indice

for k, numero in enumerate(max_vetor):
    if (max_l is None or numero > max_l):
        max_l = numero
        maxi_l = k

print("#" * 100)
print("Maior vetor com os maiores numeros :", max_vetor)
print("Localização do maior vetor esta localizado na linha :", max_n)
print(f"O maior numero do vetor é : {max_l} e esta localizado no indice : {maxi_l}")