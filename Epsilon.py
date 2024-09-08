from Gamma import *

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
    clear()
    if registry == None:
        registry = [ ]
    print("Ingrese el codigo postal: ")
    cp = input("--> ")
    print("Ingrese su direccion: ")
    dr = input("-->" )
    print(f"Ingrese su tipo de envio: \n carta simple (0) \n carta simple_v2 (1) \n carta simple_v3 (2) \n carta certificada (3) \n carta certificada_v2 (4) \n carta expresa (5) \n carta expresa_v2 (6)")
    te = input("--> ")
    print("Ingrese su forma de pago. \n Efectivo: 1 \n Tarjeta crédito: 2")
    fp = input("--> ") 
    try:
        te = int(te)
    except:
        return registry
    finally:
        if te >= 0 and te <= 6:   
            te_verification = True
        else:
            te_verification = False
            return registry
    try:
        fp = int(fp)
    except:
        return registry
    finally:
        if fp == 1 or fp == 2:
            fp_verification = True
        else:
            fp_verification = False
            return registry
    if fp_verification and te_verification:
        registry.append(Envio(cp,dr,te,fp))
    else:
        return registry
    return registry




    

def menu_option_3(registry):
    """
    Funcion que se encarga de toda la ejecucion de la opcion 3
    :param registry: el array de registros a recorrer
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
    #le preguntamos al usuario si quiere mostrar todo, o solamente algunos
    print("Cuantos elementos desea mostrar en el arreglo?")
    print("Ingrese un numero entero para indicar cuantos elementos desea mostrar")
    print("Ingrese cualquier otra cosa para mostrar todos los elementos del arreglo")
    user_choice = input("-->")
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
        #
        if user_choice == "-1":
            n = len(sorted_registry)
        elif user_choice != "-1":
            n = int(user_choice)
        else:
            n = len(sorted_registry)
        #limpiamos la consola una vez mas, antes de mostrar todo el registro
        clear()
        for i in range(n):
            print("envio n°: "+str(i)+"  |  "+" Codigo postal: "+str(sorted_registry[i].codigo_postal)+"  |  "+" Tipo de envio: "+str(sorted_registry[i].tipo_de_envio)+"  |  "+" Direccion de destino: "+str(sorted_registry[i].direccion)+"  |  "+" Forma de pago: "+str(sorted_registry[i].forma_de_pago))
        print("se ha mostrado el registro, pulse ENTER para continuar y volver al menu")
        var1 = input()
        return sorted_registry




def menu_option_4(registry):
    """
    Funcion que se encarga de toda la ejecucion de la opcion 4
    :return:
    """
    clear()
    print("Ingrese su direccion: ")
    dr = input("-->" )
    print(f"Ingrese su tipo de envio: \n carta simple (0) \n carta simple_v2 (1) \n carta simple_v3 (2) \n carta certificada (3) \n carta certificada_v2 (4) \n carta expresa (5) \n carta expresa_v2 (6)")
    te = input("--> ")
    

    
    
    
def menu_option_5():
    """
    Funcion que se encarga de toda la ejecucion de la opcion 5
    :return:
    """


def menu_option_6():
    """
    Funcion que se encarga de toda la ejecucion de la opcion 6
    :return:
    """


def menu_option_7():
    """
    Funcion que se encarga de toda la ejecucion de la opcion 7
    :return:
    """


def menu_option_8():
    """
    Funcion que se encarga de toda la ejecucion de la opcion 8
    :return:
    """


def menu_option_9():
    """
    Funcion que se encarga de toda la ejecucion de la opcion 9
    :return:
    """

def read():
    """
    Funcion simple que lee el documento de texto envios-tp3.txt y lo retorna como variable
    :return: Un string que contiene el archivo .txt
    """
    raw = open("envios-tp3.txt")
    return raw.read()


def lineskip_formatter(raw):
    """
    Funcion que se encarga de convertir la informacion cruda en una Lista trabajable, separandola por saltos de linea
    :param raw: Un string que contenga el archivo de texto, retornado por la funcion
    :return: una **List** que cada elemento de la list, sera un salto de linea en el docuento original
    """
    output = raw.splitlines()
    return output


def timestamp_extractor(raw):
    """
    Funcion que se encarga de extraer la linea timestamp de la lista, y la devuelve por separado junto con la lista, ahora sin timestamp
    :param raw: una lista separada usando la funcion lineskip_formatter
    :return: 1 **List** que contiene todos los envios / y 1 **String** que contiene la linea timestamp
    """
    timestamp = raw[0]
    output = raw
    output.reverse()
    output.pop()
    output.reverse()
    return output , timestamp


def timestamp_formatter(string):
    """
    Funcion simple que le da formato util a la linea timestamp
    :param string: la linea timestamp de forma cruda, como la devuelve la funcion timestamp_extractor()
    :return: Un **STRING** que sera **SC** o **HC** segun corresponda
    """
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
        word = envios_list[0]
        cp = word[0:9].lstrip(" ")
        dr = word[9:29].rstrip(" ")
        te = word[29]
        fp = word[30]
        registry[i] = Envio(cp,dr,te,fp)
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
        word = envios_list[i]
        cp = word[0:9].lstrip(" ")
        dr = word[9:29].rstrip(" ")
        te = word[29]
        fp = word[30]
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
        var1 = cp.split(" ")
        for x in range(len(var1)):
            if var1[x].isdecimal():
                hc_check_3 = True
                break
            else:
                hc_check_3 = False
        if  hc_check_1 and hc_check_2 and hc_check_3:
            registry[i] = Envio(cp,dr,te,fp)
    noneammount = registry.count(None)
    for i in range(noneammount):
        registry.remove(None)
    return registry


def bubble_sorter(registry = None):
    """
    Funcion que se encarga de ordenar el array de registros, usando el bubble sort como algoritmo
    :param registry: el array de registros sin ordenar
    :return: el array ordenado
    """
    if registry == None:
        return None
    try:
        n = len(registry)
    except:
        return None
    finally:
        pass
    for i in range(n):
        for j in range(0, n-i-1):
            if int(registry[j].codigo_postal) > int(registry[j+1].codigo_postal):
                registry[j], registry[j+1] = registry[j+1], registry[j]
    return registry