


lista_1 = [1, 2, -3, 8, 1, 5]
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]


def ord_burbujeo(lista):
    n = 1
    while n < len(lista):
        for i in range(len(lista)-n):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
        n = n + 1
    return lista


l_ord = ord_burbujeo(lista_5)

print(l_ord)