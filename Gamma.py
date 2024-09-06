class Envio:
    pass


def clear():
    print("\n"*100)


def menu_content():
    #Funcion simple que contiene los prints del menu para limpiar el codigo principal
    print("=" * 52 + "\n" + "=" + " " * 18 + "MENU PRINCIPAL" + " " * 18 + "=" + "\n" + "=" * 52)
    print("= Ingrese un numero de opcion                      =")
    print("= 1) Cargar automatica                             =")
    print("= 2) Cargar manual                                 =")
    print("= 3) Mostrar Registro                              =")
    print("= 4) Buscar envio por direccion                    =")
    print("= 5) Buscar envio por codigo postal                =")
    print("= 6) Mostrar envios validos / totales              =")
    print("= 7) Mostrar importe final acumulado               =")
    print("= 8) Mostrar tipo de envio con importe final mayor =")
    print("= 9) Mostrar importe final promedio                =")
    print("=" * 52)


def menu_validator(menu_choice = None):
    #Funcion simple para validar que la opcion que se ingrese sea un numero valido, dentro del rango 1-7
    try:
        #Intentamos convertir la opcion del usuario a un Int para validar que sea un numero y no cualquier otra cosa
        menu_choice = int(menu_choice)
    except ValueError:
        #si obtenemos un error, significa que no es un numero, sino otra cosa
        return (False)
    else:
        #si lo convertimos exitosamente validamos que sea un numero dentro del rango 1-9
        if 0 < menu_choice < 10:
            return (True)
        else:
            return (False)
    finally:
        pass

