import random
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    comp = 0

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p, comparaciones = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1
        comp = comp + comparaciones

    return comp


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    comparaciones = 0
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
        comparaciones += 1
    return pos_max, comparaciones


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comp = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        comparaciones = 1
        if lista[i + 1] < lista[i]:
            comparaciones += reubicar(lista, i + 1)

        comp = comparaciones + comp

    return comp

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    comparaciones = 0
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        comparaciones += 1

    lista[j] = v
    return comparaciones

def ord_burbujeo(lista):
    n = 1
    comparaciones = 0
    while n < len(lista):
        for i in range(len(lista)-n):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                comparaciones += 1
        n = n + 1
    return comparaciones


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        comp = 0
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, comp = merge_sort(lista[:medio])
        der, comp = merge_sort(lista[medio:])
        lista_nueva, comp = merge(izq, der, comp)
    return lista_nueva, comp

def merge(lista1, lista2, comp):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        comp +=1
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comp

def generar_lista(N):
    rand_list = random.sample(range(1,1000),N)
    return rand_list

def experimento(n: int = 10, k:int = 100) -> tuple:
    bur, ins, sel = 0, 0, 0
    for i in range(k):
        lista = generar_lista(n)
        sel += ord_seleccion(lista.copy())
        ins += ord_insercion(lista.copy())
        bur += ord_burbujeo(lista.copy())

    res = (sel/k, ins/k, bur/k)
    return res

def experimento_vectores(Nmax:int) -> list:
    comparaciones_seleccion, \
    comparaciones_insercion, \
    comparaciones_burbujeo,\
    comparaciones_merge_sort    = [], [], [], []
    for n in range(Nmax):
        lista = generar_lista(n)
        comparaciones_seleccion.append(ord_seleccion(lista.copy()))
        comparaciones_insercion.append(ord_insercion(lista.copy()))
        comparaciones_burbujeo.append(ord_burbujeo(lista.copy()))
        comparaciones_merge_sort.append(merge_sort(lista.copy())[1])
    return comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge_sort

if __name__ == '__main__':
    n = 500
    comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge_sort \
        = experimento_vectores(n)
    plt.plot(comparaciones_seleccion, 'b', label='selection')
    plt.plot(comparaciones_insercion, 'orange', label='insercion')
    plt.plot(comparaciones_burbujeo, 'g',  label='burbujeo')
    plt.plot(comparaciones_merge_sort, 'r', label='merg_sort')
    plt.xlabel('Numero de comparaciones')
    plt.ylabel('Tamaño de lista')
    plt.legend()
    plt.show()




