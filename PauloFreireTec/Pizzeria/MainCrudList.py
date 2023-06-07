nombres = []

# Mostrar datos de la lista


def MostrarDatos():
    for dato in nombres:
        print(end='' + dato + ', ')

# Insertar datos en la lista


def InsertarDatos():
    cantDatos = int(input('¿Cuántos datos desea ingresar? '))
    for i in range(cantDatos):
        dato = input('Ingrese el nombre en la posicion: ')
        upperDato = dato.upper()
        nombres.append(upperDato)
    print('Datos ingresados con éxito!!')
    print('Los datos ingresados son: ')
    MostrarDatos()
    EliminarDatos()

# Eliminar datos de la lista


def EliminarDatos():
    dato = input('¿Qué dato desea eliminar? ')
    upperDato = dato.upper()
    nombres.remove(upperDato)
    print('Datos eliminados con éxito!!')
    print('La nueva lista queda así: ')
    MostrarDatos()
    ActualizarDatos()

# Actualizar datos de la lista


def ActualizarDatos():
    dato = input('¿Qué dato desea actualizar? ')
    upperDato = dato.upper()
    nuevoDato = input('Ingrese el nuevo dato: ')
    upperNuevoDato = nuevoDato.upper()
    nombres[nombres.index(upperDato)] = upperNuevoDato
    MostrarDatos()


# Entry point
if __name__ == '__main__':
    InsertarDatos()
