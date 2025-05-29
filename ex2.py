# def maior_num(x, y, z):
#     maior = x
#     for i in range(3):
#         if maior < y:
#             maior = y
#         if maior < z:
#             maior = z
#     print(f"O maior número é {maior}")

# maior_num(-100000000, -9, 100)

def maior(valor1, valor2, valor3):
    return max(valor1, valor2, valor3)

numero_maior = maior(3, -7, 4)
numero_maior2 = maior(5, 37, 9)
numero_maior3 = maior(11, -98, -5)

print(numero_maior, numero_maior2, numero_maior3)