def primeros_auxilios():
    """
    Función que simula una aplicación interactiva de primeros auxilios.
    """

    # Inicio de la aplicación
    print("**Aplicación de primeros auxilios**")

    # Preguntar si la víctima está estimulada
    estimulada = input("¿La víctima responde a estímulos? (Sí/No): ")

    # si estimulada es positivo:
    if estimulada.lower() == "si":||
        print("Llevarlo al hospital más cercano")
    else:
        # Si la víctima no está estimulada, abrir la vía aérea
        print("**Abrir la vía aérea**")

        # Preguntar si la víctima respira
        respira = input("¿La víctima respira? (Sí/No): ")

        # Si la víctima respira, pero no de manera suficiente, administrar respiraciones de rescate
        if respira.lower() == "si":
            print("Permitirle posición de suficiente ventilación")
            
        else:
            # Si la víctima no respira, iniciar la reanimación cardiopulmonar (RCP)
            print("**Administrar 5 compresiones y llamar a ambulancia**")

            # Inicializar signos_vida antes del bucle
            llego_ambulancia = ""

            while llego_ambulancia != 'si':
                # Preguntar si la víctima tiene signos de vida
                signos_vida = input("¿La víctima tiene signos de vida? (Sí/No): ")

                # Si la víctima tiene signos de vida, llamar a una ambulancia
                if signos_vida.lower() == "si":
                    print("**Reevaluar a la espera de la ambulancia**")
                    llego_ambulancia = input("¿Llegó la ambulancia? (Sí/No): ")
                # Si la víctima no tiene signos de vida, continuar con la RCP
                elif signos_vida.lower() == "no":
                    print("**Administrar compresiones hasta que llegue la ambulancia**")
                    llego_ambulancia = input("¿Llegó la ambulancia? (Sí/No): ")

primeros_auxilios()