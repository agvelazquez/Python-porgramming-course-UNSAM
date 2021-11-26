# Ejercicio 5.10
import random
import numpy as np
import matplotlib.pyplot as plt


def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=int)
    return album

def album_incompleto(A):
    return np.any(A == 0)

def comprar_figu(figus_total):
    return random.choice(range(figus_total))

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu] += 1
    return album.sum()


def experimento_figus(n_repeticiones, figus_total):
    total_figus = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    return np.mean(total_figus)

def comprar_paquete(figus_total, figus_paquete=5):
    paquete = random.choices(range(figus_total), k=5)
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total,figus_paquete)
        for figu in paquete:
            album[figu] += 1
    return album.sum()

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas

n_repeticiones=10000
figus_total = 670
figus_paquete = 5

#experimento = experimento_figus(n_repeticiones, figus_total)
#print(experimento)

album = crear_album(figus_total)
while album_incompleto(album):
    paquete = random.choices(range(figus_total), k=5)
    for figu in paquete:
        album[figu] += 1

n_paquetes = (album.sum()) / figus_paquete
print('Numero de figus', album.sum())
print('Numero de figus', n_paquetes)

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

##Numero de figus 4285
#Numero de figus 857.0