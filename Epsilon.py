"""
Este es el modulo Epsilon

El modulo Epsilon contiene la logica central del programa, basicamente las ordenes logicas de cada opcion del menu
"""
from Gamma import *
from Alpha import *

def menu_option_1():
    """
    Funcion que se encarga de toda la ejecucion de la opcion 1 del menu, es decir, la inicializacion de un registro vacio y la carga de sus campos correspondientes tomando como dato un archivo .txt
    :return: el registro reiniciado con el archivo de texto
    """
    # obtenemos los datos del documento
    extracted_raw_data = read()
    # formateamos los saltos de linea en una lista
    line_formatted_raw_data = lineskip_formatter(extracted_raw_data)
    # extraemos la linea timestamp
    data = timestamp_extractor(line_formatted_raw_data)
    # formateamos la linea timestamp en algo usable
    timestamp_data = timestamp_formatter(data[1])
    # checkeamos si es SC o HC
    if timestamp_data == "SC":
        registro = data_extractor_sc(data[0])
    elif timestamp_data == "HC":
        registro = data_extractor_hc(data[0])
    else:
        #como fallback asumimos que es HC
        registro = data_extractor_hc(data[0])
    return registro


def menu_option_2(registry):
    """
    Funcion que se encarga de toda la ejecucion de la opcion 2
    :param registry: un array de registros previamente dado por la función 1 O un valor de tipo "NoneType"
    :return: el array de registro con el nuevo valor adentro, asumiendo que este tenga un tipo de envío y formas de pago validas, sino retornará el array de registros original
    """
    #limpiamos la consola
    clear()
    #Si registry es None entonces es un array vacio
    if registry == None:
        registry = [ ]
    #invocamos los prints, y guardamos retorno en variable "ED" (corto para Envio Data)
    ed = menu_final_print_2()
    #nos aseguramos que no haya nonetypes
    for i in range(len(ed)):
        #si es none
        if ed[i] == None or ed[i] == "":
            #retornas con el registro que te dieron
            return registry
    #Se intenta transformar el tipo de envio en un integer
    try:
        te = int(ed[2])
    except:
        return registry
    finally:
        #Si el valor ingresado manualmente es de 0 a 6 se activara la bandera o no
        if te >= 0 and te <= 6:   
            te_verification = True
        else:
            te_verification = False
            return registry
    #Se intenta transformar la forma de envio en un integer
    try:
        fp = int(ed[3])
    except:
        return registry
    finally:
        #Si el valor ingresado manualmente es de 1 o 2 se activara la bandera o no
        if fp == 1 or fp == 2:
            fp_verification = True
        else:
            fp_verification = False
            return registry
    #Si las banderas fueron verdades se agregaran al registro
    cp = ed[0]
    dr = ed[1]
    if fp_verification and te_verification:
        registry.append(Envio(cp,dr,te,fp))
    else:
        return registry
    return registry


def menu_option_3(registry):
    """
    Funcion que se encarga de toda la ejecucion de la opcion 3
    :param registry: el array de registros
    :return: el array de registros ordenado si recibio uno valido, caso contrario retorna "NoneType"
    """
    #limpiamos la consola
    clear()
    # verificamos que el registro se haya cargado inicialmente
    if registry == None:
        # si el registro no se cargo, retornamos al menu principal
        return None
    else:
        #si el registro se cargo, ordenamos el registro. para esto usaremos el metodo de bubble sort
        sorted_registry = bubble_sorter(registry)
    user_choice = menu_final_print_3()
    #verificamos si metio un numero entero, usamos try
    try:
        #intentamos convertir el string a un entero
        user_choice = int(user_choice)
    except:
        #si tira una exception, significa que no metio un numero entero
        #seteamos manualmente a -1
        user_choice = "-1"
    finally:
        #procedemos con mostrar el registro
        if user_choice == "-1":
            n = len(sorted_registry)
        elif user_choice != "-1":
            n = int(user_choice)
        else:
            n = len(sorted_registry)
        #limpiamos la consola una vez mas, antes de mostrar todo el registro
        clear()
        mostrar__registro_completo(sorted_registry,n)
        print("se ha mostrado el registro, pulse ENTER para continuar y volver al menu")
        var1 = input()
        return sorted_registry




def menu_option_4(registry):
    """
    Funcion que se encarga de toda la ejecucion de la opcion 4
    :param registry: El array de registros
    :return: No retorna nada
    """
    #Limpiamos la consola
    clear()
    #Se ingresa manualmente la dirección
    print("=" * 59 + "\n" + "=" + " " * 11 + "OPCION 4: Buscar envio por direccion" + " " * 10 + "=" + "\n" + "=" * 59)
    print("= Ingrese su direccion:                                   =")
    print("=" * 59)
    dr = input("-->" )
    #limpiamos consola
    clear()
    #Se ingresa manualmente el tipo de envío
    print("=" * 59 + "\n" + "=" + " " * 11 + "OPCION 4: Buscar envio por direccion" + " " * 10 + "=" + "\n" + "=" * 59)
    print("= Ingrese su tipo de envío:                               =")
    print("=  Carta simple tipo 1(0)                                 =")
    print("=  Carta simple tipo 2 (1)                                =")
    print("=  Carta simple tipo 3 (2)                                =")
    print("=  Carta certificada tipo 1(3)                            =")
    print("=  Carta certificada tipo 2 (4)                           =")
    print("=  Carta expresa tipo 1 (5)                               =")
    print("=  Carta expresa tipo 2 (6)                               =")
    print("=" * 59)
    te = input("--> ")
    #una vez terminados los prints, limmpiamos consola
    clear()
    #Se evita el punto para que el ciclo for funcione correctamente
    dr = str(dr)+str(".")
    #Inicio del ciclo en el array
    for i in range(len(registry)):
        #Se busca la dirección ingresada en el array
        if dr == str(registry[i].direccion):
            #Se busca el tipo de envío ingresado en el array
            if te == str(registry[i].tipo_de_envio):
                #Se muestra en consola el código postal, la dirección, el tipo de envío y la forma de pago, llamando a la funcion correspondiente para esto.
                menu_final_print_4(registry[i])
                return
    #limpiamos consola
    clear()
    #En caso de que no coincida la dirección ni el tipo de envío se muestra éste mensaje            
    print("No se ha encontrado un valor que coincida con el criterio de busqueda solicitado")
    #Se útiliza para que el el print se mantenga en la consola
    var1 = input("presione ENTER para continuar")
    return
    
                
            

    
    
    
def menu_option_5(registry):
    """
    Funcion que se encarga de toda la ejecucion de la opcion 5
    ::param registry: El array de registros
    :return: El array del registro modificado si la solicitud es valida 
    """
    #Limpiamos la consola
    clear()
    #Se ingresa manualmente el codigo postal
    print("=" * 55 + "\n" + "=" + " " * 7 + "OPCION 5: Buscar envio por codigo postal" + " " * 6 + "=" + "\n" + "=" * 55)
    print("= Ingrese el codigo postal:                           =")
    print("=" * 55)
    cp = input("--> ")
    #Inicio del ciclo en el array
    for i in range(len(registry)):
        #Se busca el codigo postal ingresada en el array
        if cp == str(registry[i].codigo_postal):
            #Se invierte la forma de pago
            if str(registry[i].forma_de_pago) != "1":
                if str(registry[i].forma_de_pago) != "2":
                    #Se útiliza para que el el print se mantenga en la consola
                    var1 = input(" EL VALOR DE FORMA DE PAGO DE LA VARIABLE ENCOTRADA ES INVALIDO, PULSE ENTER PARA VOLVER AL MENU")
                    return registry
            if str(registry[i].forma_de_pago) == str(1):
                registry[i].forma_de_pago = 2
                #Se ordena el array
                registry = bubble_sorter(registry)
                #Se muestra el array
                mostrar__registro_completo(registry)
                #Se útiliza para que el el print se mantenga en la consola
                var1 = input("presione ENTER para continuar")
                return registry
            else:
                registry[i].forma_de_pago = 1
                #Se ordena el array
                registry = bubble_sorter(registry)
                #Se muestra el array
                mostrar__registro_completo(registry)
                #Se útiliza para que el el print se mantenga en la consola
                var1 = input("presione ENTER para continuar")
                return registry
    #En caso de que no coincida
    print("No se ha encontrado un valor que coincida con el criterio de busqueda solicitado")
    #Se útiliza para que el el print se mantenga en la consola
    var1 = input("presione ENTER para continuar")
    return registry
    


def menu_option_6(registry):
    """
    Funcion que se encarga de toda la ejecucion de la opcion 6

    :param registry: El array de registros
    :return: nada por el momento
    """
    try:
        #intentamos extraer los datos de la linea timestamp
        # obtenemos los datos del documento
        extracted_raw_data = read()
        #formateamos los saltos de linea en una lista
        line_formatted_raw_data = lineskip_formatter(extracted_raw_data)
        #extraemos la linea timestamp
        data = timestamp_extractor(line_formatted_raw_data)
        #formateamos la linea timestamp en algo usable
        tc = timestamp_formatter(data[1])
    except:
        #si tenemos error, significa que no hay documento del cual extraer, seteamos la timestamp manualmente en HC
        tc = "HC"
    if registry == None:
        #si no hay array de registros, volve
        return None
    #Primero identificamos si es HC o SC.
    #Como no nos especifican que pasara si se carga manualmente sin timestamp
    #Asumiremos que si es el caso, debe ser HC que seria lo mas realista y logico en una situacion real
    if tc == "SC":
        #tenemos que hacerlo con un vector de conteo, entonces vamos con ello.abs
        vector_de_conteo = [0,0,0,0,0,0,0]
        #declaramos un contador externo para tener estadisticas
        external_counter = 0
        #recorremos el array
        for i in range(len(registry)):
            external_counter +=1
            vector_de_conteo[int(registry[i].tipo_de_envio)] +=1
    else:
        #similar a como lo hicimos en SC, vector de conteo go brrrr
        vector_de_conteo = [0,0,0,0,0,0,0]
        #declaramos contador externo para estadisticas
        external_counter = 0
        #recorremos el array
        for i in range(len(registry)):
            #checkeamos si el valor que estoy recorriendo es valido para HC, para eso usamos element_validator()
            if element_validator(registry[i]):
                #si es un elemento valido, lo agregamos al vector de conteo y al vector estadistico
                external_counter += 1
                vector_de_conteo[int(registry[i].tipo_de_envio)] +=1
    #mostramos los resultados del analisis llamando a la funcion correspondiente
    menu_final_print_6(vector_de_conteo,external_counter,tc)
    return


def menu_option_7(registry):
    """
    Funcion que se encarga de toda la ejecucion de la opcion 7

    :param registry: El array de registros
    :return: nada por el momento
    """
    try:
        #intentamos extraer los datos de la linea timestamp
        # obtenemos los datos del documento
        extracted_raw_data = read()
        #formateamos los saltos de linea en una lista
        line_formatted_raw_data = lineskip_formatter(extracted_raw_data)
        #extraemos la linea timestamp
        data = timestamp_extractor(line_formatted_raw_data)
        #formateamos la linea timestamp en algo usable
        tc = timestamp_formatter(data[1])
    except:
        #si tenemos error, significa que no hay documento del cual extraer, seteamos la timestamp manualmente en HC
        tc = "HC"
    if registry == None:
        #si no hay array de registros, volve
        return None
    if tc == "SC":
        #tenemos que hacerlo con un vector de conteo
        vector_de_acumuladores = [0,0,0,0,0,0,0]
        #declaramos un contador externo para tener estadisticas
        external_counter = 0
        #recorremos el array
        for i in range(len(registry)):
            external_counter +=1
            vector_de_acumuladores[int(registry[i].tipo_de_envio)] += final_value_calculator(registry[i])
    else:
        #similar a como lo hicimos en SC, vector de conteo
        vector_de_acumuladores = [0,0,0,0,0,0,0]
        #declaramos contador externo para estadisticas
        external_counter = 0
        #recorremos el array
        for i in range(len(registry)):
            #checkeamos si el valor que estoy recorriendo es valido para HC, para eso usamos element_validator()
            if element_validator(registry[i]):
                #si es un elemento valido, lo agregamos al vector de conteo y al vector estadistico
                external_counter += 1
                vector_de_acumuladores[int(registry[i].tipo_de_envio)] += final_value_calculator(registry[i])
    #mostramos los resultados del analisis llamando a la funcion correspondiente
    menu_final_print_7(vector_de_acumuladores,external_counter,tc)
    

def menu_option_8(registry):
    """
    Funcion que se encarga de toda la ejecucion de la opcion 8

    :param registry: El array de registros
    :return: Nada por el moento
    """
    #por como esta echo el codigo, seria algo dificil retornar un valor que no sea el registro de vuelta al modulo main, para devolverlo aca, y no estamos seguros si las variables globales funcionan a travez de modulos, asi que simplemente ejecutaremos el core de la funcion 7.
    try:
        #intentamos extraer los datos de la linea timestamp
        # obtenemos los datos del documento
        extracted_raw_data = read()
        #formateamos los saltos de linea en una lista
        line_formatted_raw_data = lineskip_formatter(extracted_raw_data)
        #extraemos la linea timestamp
        data = timestamp_extractor(line_formatted_raw_data)
        #formateamos la linea timestamp en algo usable
        tc = timestamp_formatter(data[1])
    except:
        #si tenemos error, significa que no hay documento del cual extraer, seteamos la timestamp manualmente en HC
        tc = "HC"
    if registry == None:
        #si no hay array de registros, volve
        return None
    if tc == "SC":
        #creamos vector de conteo
        vector_de_acumuladores = [0,0,0,0,0,0,0]
        #declaramos un contador externo para tener estadisticas
        external_counter = 0
        #recorremos el array
        for i in range(len(registry)):
            external_counter +=1
            vector_de_acumuladores[int(registry[i].tipo_de_envio)] += final_value_calculator(registry[i])
    else:
        #vector de conteo otra vez
        vector_de_acumuladores = [0,0,0,0,0,0,0]
        #declaramos contador externo para estadisticas
        external_counter = 0
        #recorremos el array
        for i in range(len(registry)):
            #checkeamos si el valor que estamos recorriendo es valido para HC, para eso usamos element_validator()
            if element_validator(registry[i]):
                #si es un elemento valido, lo agregamos al vector de conteo y al vector estadistico
                external_counter += 1
                vector_de_acumuladores[int(registry[i].tipo_de_envio)] += final_value_calculator(registry[i])
    #ahora que tenemos los vectores de acumuladores llenos de informacion, obtenemos cual es el mayor.
    max_val = max(vector_de_acumuladores[0],vector_de_acumuladores[1],vector_de_acumuladores[2],vector_de_acumuladores[3],vector_de_acumuladores[4],vector_de_acumuladores[5],vector_de_acumuladores[6])
    #averiguamos cual de los 7 fue con un corto bucle for
    for i in range(len(vector_de_acumuladores)):
        if vector_de_acumuladores[i] == max_val:
            max_value_index = i
            break
    #ahora calculamos el monto acumulado total entre todos los envios:
    total_monto = vector_de_acumuladores[0] + vector_de_acumuladores[1] + vector_de_acumuladores[2] + vector_de_acumuladores[3] + vector_de_acumuladores[4] + vector_de_acumuladores[5] + vector_de_acumuladores[6]
    porcentaje = round((max_val*100) / total_monto,2)
    #y finalmente lo mostramos llamando a la funcion correspondiente
    menu_final_print_8(max_val,max_value_index,porcentaje,tc)


def menu_option_9(registry):
    """
    Funcion que se encarga de toda la ejecucion de la opcion 9

    :param registry: El array de registros
    :return: Nada por el momento
    """
    # inicializamos el acumulador
    acumulador = 0
    # inicializamos el contador
    contador = len(registry)
    # recorremos el registro
    for i in range(len(registry)):
        #agregamos al acumulador
        acumulador += final_value_calculator(registry[i])
    #sacamos el promedio
    promedio = round(acumulador / contador,2)
    #inicializamos un segundo contador
    contador2 = 0
    #recorremos el array denuevo
    for i in range(len(registry)):
        #si es menor a la media, agregamos al contador
        if final_value_calculator(registry[i]) < promedio:
            contador2 += 1
    #mostramos resultado
    menu_final_print_9(promedio,contador2)

def read():
    """
    Funcion simple que lee el documento de texto envios-tp3.txt y lo retorna como variable
    :return: Un string que contiene el archivo .txt
    """
    #simple open(), nada que ver aqui
    raw = open("envios-tp3.txt")
    return raw.read()


def lineskip_formatter(raw):
    """
    Funcion que se encarga de convertir la informacion cruda en una Lista trabajable, separandola por saltos de linea
    :param raw: Un string que contenga el archivo de texto, retornado por la funcion
    :return: una **List** que cada elemento de la list, sera un salto de linea en el docuento original
    """
    #spliteamos el documento en los saltos de linea, retorna list
    output = raw.splitlines()
    return output


def timestamp_extractor(raw):
    """
    Funcion que se encarga de extraer la linea timestamp de la lista, y la devuelve por separado junto con la lista, ahora sin timestamp
    :param raw: una lista separada usando la funcion lineskip_formatter
    :return: 1 **List** que contiene todos los envios / y 1 **String** que contiene la linea timestamp
    """
    #almacenamos la linea timestamp en una variable aparte para retornarla sola
    timestamp = raw[0]
    # sacamos la linea timestamp con un par de reverse() y un pop()
    output = raw
    output.reverse()
    output.pop()
    output.reverse()
    #retornamos
    return output , timestamp


def timestamp_formatter(string):
    """
    Funcion simple que le da formato util a la linea timestamp
    :param string: la linea timestamp de forma cruda, como la devuelve la funcion timestamp_extractor()
    :return: Un **STRING** que sera **SC** o **HC** segun corresponda
    """
    #simplemente toma la linea timestamp y vemos si es HC o SC, retornaos los strings para que sea mas "usable"
    if "HC" in string:
        return "HC"
    elif "SC" in string:
        return "SC"



def data_extractor_sc(envios_list):
    """
    Funcion que extraera los datos contenidos en cada envio de la **List** y los agregara al registro
    :param envios_list: Una **List** que contiene envios, previamente extraida la timestamp y formateados los saltos de linea con sus respectivas funciones
    :return: Un Array de Registros
    """
    # inicializamos el array de registro
    cant_envios = int(len(envios_list))
    registry = cant_envios * [None]
    # Creamos un bucle que recorra cada indice de la lista de envios
    for i in range(len(envios_list)):
        #como es sc, almacenamos datos en variable word y dejamos que la funcion constructora haga lo suyo
        word = envios_list[i]
        cp = word[0:9].lstrip(" ")
        dr = word[9:29].rstrip(" ")
        te = word[29]
        fp = word[30]
        registry[i] = Envio(cp,dr,te,fp)
    #retornamos el array lleno
    return registry

def data_extractor_hc(envios_list):
    """
        Funcion que extraera los datos contenidos en cada envio de la **List** y los agregara al registro
        :param envios_list: Una **List** que contiene envios, previamente extraida la timestamp y formateados los saltos de linea con sus respectivas funciones
        :return: Un Array de Registros
        """
    # inicializamos el array de registro
    cant_envios = int(len(envios_list))
    registry = cant_envios * [None]
    # Creamos un bucle que recorra cada indice de la lista de envios
    for i in range(len(envios_list)):
        #igual que antes, almacenamos todo en word, y separamos en 4 variables individuales
        word = envios_list[i]
        cp = word[0:9].lstrip(" ")
        dr = word[9:29].rstrip(" ")
        te = word[29]
        fp = word[30]
        #hacemos los checkeos para ver si es HC valido o no (esta cadena de comandos esta utilizada en otras partes del script, y ahi se explica como funciona, recomiendo que para la correccion se dirijan a esas otras oruccencias)
        hc_check_1_var = dr.replace(" ","")
        hc_check_1_var = hc_check_1_var.replace(".","")
        hc_check_1 = False
        hc_check_1 = hc_check_1_var.isalnum()
        flag = False
        hc_check_2 = True
        for y in dr:
            if y.isupper():
                if flag:
                    flag = False
                    hc_check_2 = False
                    break
                else:
                    flag = True
            else:
                flag = False
        hc_check_3 = False
        varx = dr.replace(".","")
        var1 = varx.split(" ")
        for x in range(len(var1)):
            if var1[x].isdecimal():
                hc_check_3 = True
                break
            else:
                hc_check_3 = False
        if  hc_check_1 and hc_check_2 and hc_check_3:
            registry[i] = Envio(cp,dr,te,fp)
        checkbuilder = (hc_check_1, hc_check_2, hc_check_3)
    noneammount = registry.count(None)
    for i in range(noneammount):
        registry.remove(None)
    #retornaos el array que ahora solo tiene adentro las entradas que sean validas por HC
    return registry