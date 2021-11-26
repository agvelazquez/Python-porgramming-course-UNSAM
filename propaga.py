# Ejercicio 4.6: Propagación
# Hecho con Rocio Gonzalez

def propagar(vector):
    nuevo= [0]*len(vector)
    for i,v in enumerate(vector):
        if i == 0:
            nuevo[i] = v
        if v == 0:
            if nuevo[i-1] == 1:
                nuevo[i] = 1
            else:    
                nuevo[i] = v
        else:
            nuevo[i] = v
    for e in range(len(nuevo)-1,-1,-1):
    #print(e, nuevo[e])
        if nuevo[e] == 0:
            if nuevo[e+1] == 1:
                nuevo[e] = 1
    return nuevo
        
test=propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
print(test)