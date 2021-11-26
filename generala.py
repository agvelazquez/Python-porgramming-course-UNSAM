# Ejercicio 5.1
import random


def tirar(dados=5):
    tirada = [random.randint(1,6) for i in range(dados)]
    return tirada

def es_generala(tirada):
    generala = [dado == tirada[0] for dado in tirada]
    return all(generala)


#tirada = tirar()
#print(tirada)
#print(es_generala(tirada))

## simulacion

N = 100000
G = sum([es_generala(tirar()) for i in range(N)])
prob0 = G/N
print(f'Tire {N} veces, de las cuales {G} saque generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob0:.6f}.')


# Ejercicio 5.2

def prob_generala(N):
    prob = []
    for an in range(N):
        #print(an)
        tirada = tirar()
        #print(tirada)
        dados = len(tirada)
        if es_generala(tirada):
            prob.append(1)
        else:
            for i in range(2): #tengo dos chances mas luego de la primera tirada
                foo = dict.fromkeys(tirada,0)
                for e in tirada:
                    foo[e] = foo[e] + 1
                maximo = max(foo, key=foo.get)
                if foo[maximo] > 1:
                    tirada = [maximo]*foo[maximo]
                    tirada += (tirar(dados-foo[maximo]))
                    #print(i, tirada)
                else:
                    tirada = tirar()
                    #print(i, tirada)
                if es_generala(tirada):
                    prob.append(1)
                    break
                else:
                    continue
            else:
                prob.append(0)
    return sum(prob), sum(prob)/len(prob)


g, prob = prob_generala(N)

print(f'Tire {N} veces, de las cuales {g} saque generala no servida.')
print(f'Podemos estimar la probabilidad de sacar generala no servida mediante {prob:.6f}.')