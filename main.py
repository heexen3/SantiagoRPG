import funciones as fun
from mapa import mapa
# main.py

print("Santhago RPG")
print("Versión super-ultra-pre-alpha 0.1")
print("Parece que esta noche va a ser fría...")

# Llamada de prueba a la función
fun.saludar_jugador("Rob")


# ============================================== VARIABLES ==============================================
jugando = True

ubicacion_actual = "callejon"

turno = 1


# ============================================== LOOP DE JUEGO ==============================================

while jugando == True:
    print(f"Turno: {turno}")
    if turno==1:
        fun.mostrar_ubicacion(ubicacion_actual)
    accion = input("¿Qué quieres hacer?\n").strip().lower()

    # --- Lógica de parseo de comandos ---

    partes_accion = accion.split(' ', 1)
    verbo = partes_accion[0]
    complemento = partes_accion[1] if len(partes_accion)>1 else ""

    if verbo == "avanzar":
        if complemento == "":
            print(f"Avanzar... ¿pero hacia dónde...?")
        else:
            ubicacion_actual = fun.mover(ubicacion_actual, complemento)
            turno += 1
    elif verbo == "mirar":
        if complemento == "salidas":
            fun.mostrar_salidas(ubicacion_actual)
            turno += 1
        else:
            fun.mostrar_ubicacion(ubicacion_actual)
    elif verbo == "salir":
        jugando = False
        print("Gracias por jugar a Santhago RPG.")
    else:
        print(f"'{accion}' no es una acción válida, intenta nuevamente...")