# main.py
print("Santhago RPG")
print("Versión super-ultra-pre-alpha 0.1")
print("Parece que esta noche va a ser fría...")

def saludar_jugador(nombre):
    print(f"Despierta, {nombre}! La rueda del destino está girando.")

# Llamada de prueba a la función
saludar_jugador("Rob")


# ============================================== VARIABLES ==============================================
jugando = True

mapa = {
        "callejon":{
            "descripcion":
            """
            Te encuentras en un callejón oscuro, sientes una mezcla de olores entre el basurero frente tuyo y la orina
            seca de las murallas a tu espalda.
            Puedes escuchar el ruido de la ciudad: el ajetreo, los automóviles y algunos perros ladrando en la lejanía.
            Al final del callejón hay una puerta semi-abierta, parece la entrada trasera de un antiguo recinto industrial,
            en su interior puedes escuchar lo que parece ser música... parece que alguien está teniendo una fiesta.
            """,
            "salidas":{
                "norte":"plaza",
                "sur":"recinto industrial",
                }
        },
        "plaza":{
            "descripcion":
            """
            Es una plaza como las que hay en todas las comunas de la ciudad, construidas por la municipalidad con los impues-
            tos de las personas. En el centro hay unos juegos para niños. Notas que bajo la sombra de lo que parece ser uno 
            los árboles más antiguos del lugar, hay una carpa con algunas pertenencias de algún indigente.
            """,
            "salidas":{
                "norte":"plaza",
                "sur":"callejon",
                "este":"construccion",
                "oeste":"condominio"
                }
        },
        "construccion":{
            "descripcion":
            """
            Estás en un recinto cerrado donde se está construyendo un edificio, no lleva muchos pisos, pero ya
            terminaron el estacionamiento subterráneo. Puedes ver algunas de las maquinarias que fueron usadas durante el
            día. Al este del recinto, puedes observar unas oficinas container con el logo de la empresa constructora:
                                                        "NEBCO"
            """,
            "salidas":{
                "norte":"avenida",
                "sur":"recinto industrial",
                "este":"oficinas",
                "oeste":"plaza"
                }
        }    
    }

ubicacion_actual = "callejon"

turno = 1

# ============================================== FUNCIONES ==============================================

def mostrar_ubicacion():
    print(mapa[ubicacion_actual]["descripcion"])
    return

def mover(direccion):
    global ubicacion_actual
    if mapa[ubicacion_actual]["salidas"][direccion]:
        ubicacion_actual = mapa[ubicacion_actual]["salidas"][direccion]
        print(f"Te has movido al {direccion}")
        return mostrar_ubicacion()
    print("No puedes ir en esa dirección desde aquí...")

while jugando == True:
    print(f"Turno: {turno}")
    if turno==1:
        mostrar_ubicacion()
    turno += 1
    accion = input("¿Qué quieres hacer?\n").strip().lower()
    if accion=="norte":
        mover(accion)
    elif accion=="sur":
        mover(accion)