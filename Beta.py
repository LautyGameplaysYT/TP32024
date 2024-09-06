from Epsilon import *


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
    Funcion simple para validar que la opcion que se ingrese sea un numero valido, dentro del rango 1-9
    :param menu_choice: Default a **None** debe contener un string de la opcion que cargo el usuario
    :return: **True** :  si la opcion ingresada en el menu es un numero y esta dentro del rango 1-9 / **False** : si la opcion ingresada es cualquier otra cosa
    """
    try:
        #Intentamos convertir la opcion del usuario a un Int para validar que sea un numero y no cualquier otra cosa
        menu_choice = int(menu_choice)
    except ValueError:
        #si obtenemos un error, significa que no es un numero, sino otra cosa
        return False
    else:
        #si lo convertimos exitosamente validamos que sea un numero dentro del rango 1-9
        if 0 < menu_choice < 10:
            return True
        else:
            return False
    finally:
        pass


def menu_choice_1():
    """
    Funcion que se encarga de manejar la ejecucion de los prints de la opcion 1

    (SOLO LOS PRINTS)

    :return: solo retornara -1 si se debe re-ejecutar el menu principal
    """
    print("=" * 80 + "\n" + "=" + " " * 32 + "MENU PRINCIPAL" + " " * 32 + "=" + "\n" + "=" * 80)
    print("= Esta opcion intentara generar el arreglo principal usando un archivo de .txt =")
    print("= Esto tomara los datos de un archivo llamado *envios-tp3.txt* y no otro       =")
    print("= Ademas esto destruira el arreglo anterior (si existiera) y creara uno nuevo  =")
    print("= Esta seguro que desea continuar?                                             =")
    print("= Ingrese 1 para continuar y 2 para volver                                     =")
    print("="*80)
    choice_confirm = input("--> ")
    if choice_confirm == "1":
        registry = menu_option_1()
        return registry
    elif choice_confirm == "2":
        return -1
    else:
        menu_choice_1()


def menu_choice_2():
    """
    Funcion que se encarga de manejar la ejecucion de los prints de la opcion 2

    (SOLO LOS PRINTS)

    :return: No tiene Retorno
    """
    print("=" * 80 + "\n" + "=" + " " * 32 + "MENU PRINCIPAL" + " " * 32 + "=" + "\n" + "=" * 80)
    print("= Esta opcion le permitira cargar por teclado un valor nuevo envio             =")
    print("= Dicho envio sera almacenado en el registro existente                         =")
    print("= Y si el registro no existiera, uno vacio sera creado                         =")
    print("= Esta seguro que desea continuar?                                             =")
    print("= Ingrese 1 para continuar y 2 para volver                                     =")
    print("=" * 80)
    choice_confirm = input("--> ")
    if choice_confirm == "1":
        menu_option_2()
    elif choice_confirm == "2":
        return -1
    else:
        menu_choice_2()


def menu_choice_3():
    """
    Funcion que se encarga de manejar la ejecucion de los prints de la opcion 3

    (SOLO LOS PRINTS)

    :return: No tiene Retorno
    """
    print("=" * 80 + "\n" + "=" + " " * 32 + "MENU PRINCIPAL" + " " * 32 + "=" + "\n" + "=" * 80)
    print("= Esta opcion le permitira visualizar por consola el registro                  =")
    print("= Este sera mostrado por la consola                                            =")
    print("= Ademas tendra la opcion de ajustar cuantas entradas desea visualizar         =")
    print("= Esta seguro que desea continuar?                                             =")
    print("= Ingrese 1 para continuar y 2 para volver                                     =")
    print("=" * 80)
    choice_confirm = input("--> ")
    if choice_confirm == "1":
        menu_option_3()
    elif choice_confirm == "2":
        return -1
    else:
        menu_choice_3()


def menu_choice_4():
    """
    Funcion que se encarga de manejar la ejecucion de los prints de la opcion 4

    (SOLO LOS PRINTS)

    :return: No tiene Retorno
    """
    print("=" * 80 + "\n" + "=" + " " * 32 + "MENU PRINCIPAL" + " " * 32 + "=" + "\n" + "=" * 80)
    print("= Esta opcion le permitira buscar un envio especifico dentro del registro      =")
    print("= Este sera buscado utilizando su direccion como criterio de busqueda          =")
    print("= Este solo mostrara el primer resultado que coincida con el criterio          =")
    print("= Esta seguro que desea continuar?                                             =")
    print("= Ingrese 1 para continuar y 2 para volver                                     =")
    print("=" * 80)
    choice_confirm = input("--> ")
    if choice_confirm == "1":
        menu_option_4()
    elif choice_confirm == "2":
        return -1
    else:
        menu_choice_4()


def menu_choice_5():
    """
    Funcion que se encarga de manejar la ejecucion de los prints de la opcion 5

    (SOLO LOS PRINTS)

    :return: No tiene Retorno
    """
    print("=" * 80 + "\n" + "=" + " " * 32 + "MENU PRINCIPAL" + " " * 32 + "=" + "\n" + "=" * 80)
    print("= Esta opcion le permitira buscar un envio especifico dentro del registro      =")
    print("= Este sera buscado utilizando su codigo postal como criterio de busqueda      =")
    print("= Este solo mostrara el primer resultado que coincida con el criterio          =")
    print("= Ademas cuando encuentre una opcion que coincida con el criterio solicitado   =")
    print("= Se le dara la opcion de alterar su forma de pago                             =")
    print("= Luego se le mostrara el registro completo reflejando el cambio efectuado     =")
    print("= Esta seguro que desea continuar?                                             =")
    print("= Ingrese 1 para continuar y 2 para volver                                     =")
    print("=" * 80)
    choice_confirm = input("--> ")
    if choice_confirm == "1":
        menu_option_5()
    elif choice_confirm == "2":
        return -1
    else:
        menu_choice_5()


def menu_choice_6():
    """
    Funcion que se encarga de manejar la ejecucion de los prints de la opcion 6

    (SOLO LOS PRINTS)

    :return: No tiene Retorno
    """
    print("=" * 80 + "\n" + "=" + " " * 32 + "MENU PRINCIPAL" + " " * 32 + "=" + "\n" + "=" * 80)
    print("= Esta opcion le mostrara la cantidad de envios, categorizados por tipo        =")
    print("= Si el tipo de control es SC, mostrara la cantidad de envios totales          =")
    print("= Si el tipo de control es HC, mostrara la cantidad de envios validos          =")
    print("= Esta seguro que desea continuar?                                             =")
    print("= Ingrese 1 para continuar y 2 para volver                                     =")
    print("=" * 80)
    choice_confirm = input("--> ")
    if choice_confirm == "1":
        menu_option_6()
    elif choice_confirm == "2":
        return -1
    else:
        menu_choice_6()


def menu_choice_7():
    """
    Funcion que se encarga de manejar la ejecucion de los prints de la opcion 7

    (SOLO LOS PRINTS)

    :return: No tiene Retorno
    """
    print("=" * 80 + "\n" + "=" + " " * 32 + "MENU PRINCIPAL" + " " * 32 + "=" + "\n" + "=" * 80)
    print("= Esta opcion le mostrara el importe final acumulado, categorizados por tipo   =")
    print("= Si el tipo de control es SC, mostrara el importe final de todos los envios   =")
    print("= Si el tipo de control es HC, mostrara el importe final de los envios validos =")
    print("= Esta seguro que desea continuar?                                             =")
    print("= Ingrese 1 para continuar y 2 para volver                                     =")
    print("=" * 80)
    choice_confirm = input("--> ")
    if choice_confirm == "1":
        menu_option_7()
    elif choice_confirm == "2":
        return -1
    else:
        menu_choice_7()


def menu_choice_8():
    """
    Funcion que se encarga de manejar la ejecucion de los prints de la opcion 8

    (SOLO LOS PRINTS)

    :return: No tiene Retorno
    """
    print("=" * 80 + "\n" + "=" + " " * 32 + "MENU PRINCIPAL" + " " * 32 + "=" + "\n" + "=" * 80)
    print("= Esta opcion le mostrara cual fue el tipo de envio con importe final mayor    =")
    print("= Solo se podra ejecutar esta opcion si se ejecuto la opcion 7 previamente     =")
    print("= Esto debido a que se requiere de los datos de la opcion 7 para la opcion 8   =")
    print("= Esta seguro que desea continuar?                                             =")
    print("= Ingrese 1 para continuar y 2 para volver                                     =")
    print("=" * 80)
    choice_confirm = input("--> ")
    if choice_confirm == "1":
        menu_option_8()
    elif choice_confirm == "2":
        return -1
    else:
        menu_choice_8()


def menu_choice_9():
    """
    Funcion que se encarga de manejar la ejecucion de los prints de la opcion 9

    (SOLO LOS PRINTS)

    :return: No tiene Retorno
    """
    print("=" * 80 + "\n" + "=" + " " * 32 + "MENU PRINCIPAL" + " " * 32 + "=" + "\n" + "=" * 80)
    print("= Esta opcion le mostrara el importe final promedio entre todos los envios     =")
    print("= Ademas le informara de cuantos envios fueron menores al promedio             =")
    print("= Esta seguro que desea continuar?                                             =")
    print("= Ingrese 1 para continuar y 2 para volver                                     =")
    print("=" * 80)
    choice_confirm = input("--> ")
    if choice_confirm == "1":
        menu_option_9()
    elif choice_confirm == "2":
        return -1
    else:
        menu_choice_9()


def menu_choice_caller(menu_choice):
    """
    Funcion simple que se encarga de llamar a la opcion del menu que selecciono el usuario
    :param menu_choice: La opcion que eligio el usuario, previamente validada por la funcion menu_validator()
    :return: Retornara lo que retorne la funcion a la que llamo
    """
    menu_choice = int(menu_choice)
    if menu_choice == 1:
        f1 = menu_choice_1()
        return f1
    elif menu_choice == 2:
        f2 = menu_choice_2()
        return f2
    elif menu_choice == 3:
        f3 = menu_choice_3()
        return f3
    elif menu_choice == 4:
        f4 = menu_choice_4()
        return f4
    elif menu_choice == 5:
        f5 = menu_choice_5()
        return f5
    elif menu_choice == 6:
        f6 = menu_choice_6()
        return f6
    elif menu_choice == 7:
        f7 = menu_choice_7()
        return f7
    elif menu_choice == 8:
        f8 = menu_choice_8()
        return f8
    elif menu_choice == 9:
        f9 = menu_choice_9()
        return f9