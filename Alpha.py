"""
Este es el modulo Alpha

El modulo Alpha contiene los prints de output de cada opcion del menu
"""
from Gamma import *


def menu_final_print_2():
    """
    Función que se encarga de los prints de diseño de la opcion 2

    Ademas esta función tiene las inputs del usuario

    :return: las 4 inputs del usuario
    """
    print("=" * 52 + "\n" + "=" + " " * 14 + "OPCIÓN 2: CARGA MANUAL" + " " * 14 + "=" + "\n" + "=" * 52)
    print("= Ingrese el código postal:                        =")
    cp = input("= --> ")
    print("=" * 52)
    print("= Ingrese su dirección:                            =")
    dr = input("= -->" )
    print("=" * 52)
    print("= Ingrese su tipo de envío:                        =")
    print("=  Carta simple tipo 1(0)                          =")
    print("=  Carta simple tipo 2 (1)                         =")
    print("=  Carta simple tipo 3 (2)                         =")
    print("=  Carta certificada tipo 1(3)                     =")
    print("=  Carta certificada tipo 2 (4)                    =")
    print("=  Carta expresa tipo 1 (5)                        =")
    print("=  Carta expresa tipo 2 (6)                        =")
    te = input("= --> ")
    print("=" * 52)
    print("= Ingrese su forma de pago:                        =")
    print("=  Efectivo: 1                                     =")
    print("=  Tarjeta crédito: 2                              =")
    fp = input("= --> ") 
    return cp,dr,te,fp


def menu_final_print_3():
    """
    Función que se encarga de los prints de diseño de la opcion 3

    :return: La input del usuario
    """
    print("=" * 76 + "\n" + "=" + " " * 24 + "OPCIÓN 3: Mostrar Registro" + " " * 24 + "=" + "\n" + "=" * 76)
    print("= ¿Cuántos elementos desea mostrar en el arreglo?                          =")
    print("= Ingrese un número entero para indicar cuántos elementos desea mostrar    =")
    print("= Ingrese cualquier otra cosa para mostrar todos los elementos del arreglo =")
    print("=" * 76)
    user_choice = input("-->")
    return user_choice


def menu_final_print_4(element):
    """
    Función que se encarga de los prints de diseño de la opcion 4

    :param element: Una variable de tipo registro (Envio)

    :return: Nada
    """
    print("=" * 59 + "\n" + "=" + " " * 11 + "OPCIÓN 4: Buscar envio por direccion" + " " * 10 + "=" + "\n" + "=" * 59)
    print(f"= valor encontrado:                                       =")
    print(f"= Código postal: {element.codigo_postal}                      ")
    print(f"= La dirección del envío es: {element.direccion}          ")
    print(f"= Tipos de envío: {element.tipo_de_envio}                     ")
    print(f"= La forma de pago es: {element.forma_de_pago}                ")
    print("=" * 59)
    var1 = input("presione ENTER para continuar")


def menu_final_print_6(vector_de_conteo,external_counter,tc):
    """
    Función que se encarga de los prints de diseño de la opcion 6

    :param vector_de_conteo: El vector de conteo
    :param external_counter: El contador de la cantidad de elementos analizados
    :param tc: El tipo de control en un string

    :return: Nada
    """
    print("=" * 50 + "\n" + "=" + " " * 4 + "OPCIÓN 6: Buscar envio por codigo postal" + " " * 4 + "=" + "\n" + "=" * 50)
    print("= Resultados del analisis:                       =")
    print("= Tipo de array analizado: "+str(tc)+"\n=                                                =")
    print("= Cantidad de elementos analizados: "+str(external_counter)+"\n=                                                =")
    print("= Cantidad envíos carta simple tipo 1: "+str(vector_de_conteo[0])+"\n=                                                =")
    print("= Cantidad envíos carta simple tipo 2: "+str(vector_de_conteo[1])+"\n=                                                =")
    print("= Cantidad envíos carta simple tipo 3: "+str(vector_de_conteo[2])+"\n=                                                =")
    print("= Cantidad envíos carta certificada tipo 1: "+str(vector_de_conteo[3])+"\n=                                                =")
    print("= Cantidad envíos carta certificada tipo 2: "+str(vector_de_conteo[4])+"\n=                                                =")
    print("= Cantidad envíos carta expresa tipo 1: "+str(vector_de_conteo[5])+"\n=                                                =")
    print("= Cantidad envíos carta expresa tipo 2: "+str(vector_de_conteo[6])+"\n=                                                =")
    print("=" * 50)
    var1 = input("Pulse ENTER para volver al menu")


def menu_final_print_7(vector_de_acumuladores,external_counter,tc):
    """
    Función que se encarga de los prints de diseño de la opcion 7

    :param vector_de_acumuladores: El vector de acumuladores
    :param external_counter: El contador de la cantidad de elementos analizados
    :param tc: El tipo de control en un string

    :return: Nada
    """
    clear()
    print("=" * 80 + "\n" + "=" + " " * 18 + "OPCIÓN 7: Mostrar importe final acumulado" + " " * 19 + "=" + "\n" + "=" * 80)
    print("= Resultados del analisis:                                                     =")
    print("= Tipo de array analizado: "+str(tc)+"\n=                                                                              =")
    print("= Cantidad de elementos analizados: "+str(external_counter)+"\n=                                                                              =")
    print("= Importe final acumulado para envíos de carta simple tipo 1: "+str(vector_de_acumuladores[0])+"\n=                                                                              =")
    print("= Importe final acumulado para envíos de simple tipo 2: "+str(vector_de_acumuladores[1])+"\n=                                                                              =")
    print("= Importe final acumulado para envíos de simple tipo 3: "+str(vector_de_acumuladores[2])+"\n=                                                                              =")
    print("= Importe final acumulado para envíos de carta certificada tipo 1: "+str(vector_de_acumuladores[3])+"\n=                                                                              =")
    print("= Importe final acumulado para envíos de carta certificada tipo 2: "+str(vector_de_acumuladores[4])+"\n=                                                                              =")
    print("= Importe final acumulado para envíos de carta expresa tipo 1: "+str(vector_de_acumuladores[5])+"\n=                                                                              =")
    print("= Importe final acumulado para envíos de carta expresa tipo 2: "+str(vector_de_acumuladores[6])+"\n=                                                                              =")
    print("=" * 80)
    var1 = input("Pulse ENTER para volver al menu")


def menu_final_print_8(max_val,max_value_index,porcentaje,tc):
    """
    Función que se encarga de los prints de diseño de la opcion 8

    :param max_val: El valor final acuumlado de todos los Envíos de X tipo.
    :param max_value_index: El índice de a que tipo de envío representa
    :param porcentaje: El porcentaje que representa sobre el total
    :param tc: El tipo de control en un string

    :return: Nada
    """
    print("=" * 70 + "\n" + "=" + " " * 6 + "OPCIÓN 8: Mostrar tipo de envío con importe final mayor" + " " * 7 + "=" + "\n" + "=" * 70)
    print("= Resultados del análisis:                                           =")
    print("= Tipo de array analizado: "+str(tc)+"\n=                                                                    =")
    print("= Tipo de envío con mayor importe acumulado: "+str(max_value_index)+"\n=                                                                    =")
    print("= Importe final acumulado por el tipo de envío mayor: "+str(max_val)+"\n=                                                                    =")
    print("= Porcentaje que representa ese valor sobre el monto total: "+str(porcentaje)+"%"+"\n=                                                                    =")
    print("=" * 70)
    var1 = input("Pulse ENTER para volver al menu")


def menu_final_print_9(promedio, contador2):
    """
    Función que se encarga de los prints de diseño de la opcion 8

    :param promedio: El valor final promedio de todos los envíos del array
    :param contador2: Un contador que contiene la cantidad de envíos con valor final menor al promedio

    :return: Nada
    """
    clear()
    print("=" * 80 + "\n" + "=" + " " * 19 + "OPCIÓN 9: Mostrar importe final promedio" + " " * 19 + "=" + "\n" + "=" * 80)
    print("= Resultados del análisis:                                                     =")
    print("= Importe final promedio de todo el array: "+str(promedio)+"\n=                                                                              =")
    print("= Cantidad de envíos que tuvieron importe menor a ese promedio: "+str(contador2)+"\n=                                                                              =")
    print("=" * 80)
    var1 = input("Pulse ENTER para volver al menu")