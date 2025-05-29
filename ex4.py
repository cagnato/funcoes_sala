# qtd = int(input("Digite a quantidade de números a serem calculados: "))
# num = []

# def media(qtd, num):
#     mediaCalculo = num * qtd / qtd
#     print(mediaCalculo)

# media(5, 3)

def media(lista):
    return sum(lista) / len(lista)

print(media([2, 4, 6, 8]))
