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
            los árboles más antiguos del lugar, hay una carpa con las pertenencias de algún indigente.
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
            Estás en un recinto cerrado donde se está construyendo un edificio, no lleva muchos pisos, pero ya terminaron 
            el estacionamiento subterráneo. Puedes ver algunas de las maquinarias que fueron usadas durante el día.
            Al este del recinto, puedes observar unas oficinas container con el logo de la empresa constructora:
                                                        "NEBCO"
            """,
            "salidas":{
                "norte":"avenida",
                "este":"oficinas container",
                "oeste":"plaza"
                }
        },
        "oficinas container":{
            "descripcion":
            """
            Dentro de la construcción hay tres containers acondicionados para ser usados por los trabajadores. Al parecer
            cada uno tiene asignado un uso específico: 
                Uno para los altos mandos, uno para oficina técnica y otro para ser usado como camarín por los obreros.
            El único que parece estar abierto es el camarín, los demás están cerrados con llave.
            """,
            "salidas":{
                "sur":"maquinaria pesada",
                "oeste":"construccion"
                }
        },
        "condominio":{
            "descripcion":
            """
            Te encuentras en frente del condominio "Los Robles", este edificio residencial de 5 pisos lleva unos años aquí 
            pero nunca terminó de llenarse. Al mirar las ventanas, observas que solo algunos departamentos tienen luces
            encendida. Puedes escuchar música provenir desde el quinto piso, no estás seguro del departamento exacto.
            Notas que no hay una recepción ni tampoco un guardia cuidando la entrada principal. Debe haber una escalera de em-
            ergencia en algún lado.
            """,
            "salidas":{
                "norte":"avenida",
                "sur":"escaleras de emergencia",
                "este":"plaza",
                "oeste":"entrada pricipal"
                }
        }
        }