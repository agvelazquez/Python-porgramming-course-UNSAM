
def buscar_u_elemento(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            continue    # y salimos del ciclo
    return pos



def maximo(lista):
    '''Devuelve el máximo de una lista,
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista.
    m = float('-inf') # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

def buscar_n_elemento(lista, e):
    '''Devuelve la cantidad de veces que aparece el elemento e
    '''
    count = 0
    for i, z in enumerate(lista):
        if z == e:
            count += 1
            continue
    return count

print(maximo([1,2,7,2,3,4]))

buscar_n_elemento([1,2,7,2,3,4,7,7,7,7],7) #resultado = 5