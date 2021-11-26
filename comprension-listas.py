import module.informe as inf
import pprint


camion = inf.camion
precio = inf.precio


#print(precio)

nums = [1,2,3,4]
cuadrados = [x*x for x in nums]
dobles = [2*x for x in nums if x > 2]
print(dobles)

costo = sum([s['cajones']*s['precio'] for s in camion])

valor = sum([s['cajones']*precio[s['nombre']] for s in camion])

mas100 = [s for s in camion if s['cajones'] > 100]

myn = [s for s in camion if s['nombre'] in ('Mandarina', 'Naranja')]

costo10k = [s for s in camion if s['cajones']*s['precio'] > 10000]

nombre_cajones = [(s['nombre'],s['cajones']) for s in camion ]

nombres = {s['nombre'] for s in camion}

stock = {nombre : 0 for nombre in nombres}

for s in camion:
    stock[s['nombre']] += s['cajones']


camion_precios = {nombre:precios[nombre] for nombre in nombres}

############################
import csv

f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)

select = ['nombre', 'cajones', 'precio']

indices = [headers.index(c) for c in select]

row = next(rows)
record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}