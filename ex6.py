matriz_fora = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

# def imprimir_diagonal(matriz):
#     for linha in range(len(matriz[0])):
#         for coluna in range(len(matriz[0])):
#             if linha == coluna:
#                 print(matriz[linha][coluna])

# imprimir_diagonal(matriz_fora)

def imprimir_diagonal(matriz):
    for i in range(len(matriz[0])):
        print(matriz[i][i])

imprimir_diagonal(matriz_fora)