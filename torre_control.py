
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return len(self.items) == 0

class TorreDeControl:
    def __init__(self):
        self.arribos = []
        self.partidas = []

    def nuevo_arribo(self, avion):
        self.arribos.append(avion)

    def nueva_partida(self, avion):
        self.partidas.append(avion)

    def ver_estado(self):
        if len(self.arribos) >= 1:
            print(f'Vuelos esperando para aterrizar: {self.arribos}')
        if len(self.partidas) >= 1:
            print(f'Vuelos esperando para despegar: {self.partidas}')
        else:
            print('No hay vuelos esperando para aterrizar o despegar')

    def esta_vacia(self):
        return len(self.arribos) == 0 and len(self.partidas) == 0

    def asignar_pista(self):
        if self.esta_vacia():
            print('No hay vuelos que deban ser asignados')
        elif len(self.arribos) >= 1:
            print(f'El vuelo {self.arribos[0]} aterrizó con éxito.')
            self.arribos.pop(0)
        elif len(self.partidas) >= 1:
            print(f'El vuelo {self.partidas[0]} despegó con éxito.')
            self.partidas.pop(0)
        else:
            raise AttributeError


