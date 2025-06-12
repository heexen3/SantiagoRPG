from mapa import mapa


# ============================================== FUNCIONES ==============================================


def mostrar_ubicacion(ubicacion):
    print(mapa[ubicacion]["descripcion"])
    return

def mostrar_salidas(ubicacion):
    salidas_disponibles = mapa[ubicacion]["salidas"]
    print("Puedes 'avanzar' hacia:")
    print(", ".join(salidas_disponibles))

def mover(ubicacion_actual, direccion):
    try:
        ubicacion_nueva = mapa[ubicacion_actual]["salidas"][direccion]
        print(f"Te has movido hacia: {ubicacion_nueva}")
        mostrar_ubicacion(ubicacion_nueva)
        return ubicacion_nueva
    except KeyError:
        print("Esa dirección no parece llevar hacia ningún lado.")
        return ubicacion_actual

def saludar_jugador(nombre):
    print(f"Despierta, {nombre}! La rueda del destino está girando.")


