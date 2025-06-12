mapa = {
    "callejon": {
        "descripcion":
        """
        Te encuentras en un callejón estrecho y sombrío, donde la luz de la luna apenas se atreve a penetrar.
        Una punzante fetidez a basura fermentada y orina rancia se adhiere al aire frío y húmedo, una clara evidencia
        del basurero desbordado a tu izquierda y las murallas graffiteadas a tu espalda.
        El ruido de la ciudad es un murmullo constante y ahogado: el ajetreo lejano de los autos, el ocasional claxon
        y el lamento agudo de perros callejeros que resuena desde la lejanía.
        Al final del callejón, una puerta de metal oxidado se entreabre ligeramente, revelando un halo de luz tenue
        y el pulso rítmico de música electrónica. Parece ser la entrada trasera de un antiguo recinto industrial,
        y algo dentro sugiere una fiesta clandestina, atrayéndote con su enigmática promesa.
        """,
        "salidas": {
            "norte": "plaza",
            "sur": "recinto industrial",
        }
    },
    "plaza": {
        "descripcion":
        """
        Te encuentras en una plaza típica de barrio, un oasis de cemento y verdor financiado por el sudor de los contribuyentes.
        El aire aquí es sorprendentemente más fresco, con un tenue aroma a tierra húmeda y el dulzor de flores marchitas.
        En el centro, los juegos infantiles, oxidados y silenciosos en la penumbra, parecen melancólicos.
        Bajo la sombra imponente de un viejo plátano oriental, cuyas ramas nudosa se extienden como brazos de un coloso,
        una carpa descolorida se alza precariamente, sugiriendo la residencia temporal de un alma errante.
        Se escucha el chirrido distante de un columpio movido por el viento, un recordatorio solitario de risas pasadas.
        """,
        "salidas": {
            "norte": "avenida", # Asumiendo que la plaza también tiene salida a la avenida como en el dibujo
            "sur": "callejon",
            "este": "construccion",
            "oeste": "condominio"
        }
    },
    "construccion": {
        "descripcion":
        """
        Estás dentro de un recinto de construcción vallado, donde el esqueleto de un edificio de hormigón se alza
        contra el cielo nocturno, prometiendo una nueva torre. Apenas lleva unos pisos levantados, pero el vasto
        estacionamiento subterráneo ya está terminado, un abismo oscuro bajo tus pies.
        El aire huele a cemento fresco y metal, y el silencio de la noche es roto solo por el crujido ocasional
        de las lonas movidas por el viento. Algunas maquinarias pesadas, imponentes y silenciosas,
        duermen bajo la luna, sus sombras proyectándose como monstruos dormidos.
        Al este, un grupo de containers de obra, limpios y ordenados, llevan impreso el logo de la empresa constructora:
                                                        "NEBCO"
        Un nombre que resuena con un eco industrial en la calma de la noche.
        """,
        "salidas": {
            "norte": "avenida", # Asumiendo que la construcción también tiene salida a la avenida
            "este": "oficinas container",
            "oeste": "plaza"
        }
    },
    "oficinas container": {
        "descripcion":
        """
        Te encuentras entre tres containers de obra, acondicionados para la vida de oficina en medio del polvo y el ruido.
        El metal corrugado exuda el calor residual del día y un ligero olor a café rancio y papel se filtra en el aire.
        Cada uno tiene un propósito claro, indicado por rudimentarios carteles: uno para "ALTOS MANDOS", otro para "OFICINA TÉCNICA"
        y un tercero, más pequeño, para "CAMARÍN OBREROS".
        La mayoría de los containers tienen sus puertas cerradas con candados robustos, pero la del camarín está abierta,
        invitando a la curiosidad con un eco hueco. Una luz parpadeante se filtra por una de las rendijas del camarín,
        sugiriendo que no está completamente deshabitado.
        """,
        "salidas": {
            "sur": "maquinaria pesada", # Asumiendo este es un lugar exploratorio dentro de la construcción
            "oeste": "construccion"
        }
    },
    "condominio": {
        "descripcion":
        """
        Frente a ti se alza el Condominio "Los Robles", un edificio residencial de cinco pisos cuya fachada,
        aunque moderna, parece guardar un secreto de poca vida. Fue construido hace años, pero nunca se llenó por completo.
        Las ventanas, como ojos oscuros, revelan solo algunas luces encendidas, puntos dispersos de vida en un mar de penumbra.
        Una música tenue y con un bajo rítmico se filtra desde el quinto piso, imposible de precisar la ventana exacta,
        generando una atmósfera de misterio.
        No hay recepción a la vista ni un guardia en la entrada principal, que se presenta sorprendentemente desatendida.
        Un instinto te dice que debe haber una escalera de emergencia en algún lugar, una ruta discreta a los pisos superiores.
        """,
        "salidas": {
            "norte": "avenida", # Asumiendo que el condominio también tiene salida a la avenida
            "sur": "escaleras de emergencia", # Asumiendo que esto es un punto de interés secundario en el condominio
            "este": "plaza",
            "oeste": "entrada principal" # Asumiendo que esto es la entrada principal y puede llevar a otro lugar o ser solo una referencia
        }
    }
}