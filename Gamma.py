class Envio:
    """
    Clase Envio, registro vacio por ahora
    """
    pass


def clear():
    """
    Funcion sin retorno que ingresa 100 saltos de linea

    Esto lo hacemos para limpiar la output de consola obteniendo una ejecucion mas limpia
    Ya que no podemos hacer interfaces de usuario.
    """
    print("\n"*100)


def menu_content():
    """
    Funcion simple que contiene los prints del menu
    :return: No tiene **retorno** ni **parametros**
    """
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
    """
    Funcion simple para validar que la opcion que se ingrese sea un numero valido, dentro del rango 1-7
    :param menu_choice: Default a **None** debe contener un string de la opcion que cargo el usuario
    :return: **True** :  si la opcion ingresada en el menu es un numero y esta dentro del rango 1-7 / **False** : si la opcion ingresada es cualquier otra cosa
    """
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


def menu_choice_1():
    print("op1")


def menu_choice_2():
    print("op2")


def menu_choice_3():
    print("op3")


def menu_choice_4():
    print("op4")


def menu_choice_5():
    pass


def menu_choice_6():
    pass


def menu_choice_7():
    pass


def menu_choice_8():
    pass


def menu_choice_9():
    pass


menu_choice_opciones = {
    # Diccionario que contiene las opciones de menu para callearlas
    "1": menu_choice_1,
    "2": menu_choice_2,
    "3": menu_choice_3,
    "4": menu_choice_4,
    "5": menu_choice_5,
    "6": menu_choice_6,
    "7": menu_choice_7,
    "8": menu_choice_8,
    "9": menu_choice_9
}


