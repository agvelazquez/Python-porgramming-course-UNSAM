def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] > e:
            res = bbinaria_rec(lista[:medio], e)
        elif lista[medio] == e:
            res = lista[medio] == e
        else:
            res = bbinaria_rec(lista[medio:], e)
    return res


#lista = [0,1,2,3,4,5,6,7]
#e = 12

#print(bbinaria_rec(lista, e))