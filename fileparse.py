import csv
import gzip

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    filas = csv.reader(nombre_archivo)

    if select and has_headers == False:
        raise RuntimeError('Para seleccionar, necesito encabezados.')

    # Lee los encabezados del archivo
    if has_headers:
        encabezados = next(filas)

    # Si se indicó un selector de columnas,
    #    buscar los índices de las columnas especificadas.
    # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

    registros = []
    for i, fila in enumerate(filas):
        try:
            if has_headers:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]

                if types:
                    fila = [func(val) for func, val in zip(types, fila)]

            else:
                if types:
                    fila = tuple(func(val) for func, val in zip(types, fila))
                else:
                    fila = tuple(fila)

            if has_headers:
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            else:
                registros.append(fila)
        except ValueError as e:
            if silence_errors:
                continue
            else:
                print(f'Fila {i}: No pude convertir {fila}')
                print(f'Fila {i}: Motivo: {e}')
                continue

    return registros


if __name__ == "__main__":
    with open('../Data/missing.csv', 'rt') as file:
        #camion = parse_csv(file, types=[str, int, float])
        #camion = parse_csv(file, select = ['nombre','precio'], has_headers = False)
        camion = parse_csv(file, types=[str, int, float], silence_errors=True)
    #lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
    #camion = parse_csv(lines, types=[str, int, float], has_headers=True)
    print(camion)
