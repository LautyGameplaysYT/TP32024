from Gamma import *

def menu_option_1():
    """
    Funcion que se encarga de toda la ejecucion de la opcion 1
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


def menu_option_2():
    """
    Funcion que se encarga de toda la ejecucion de la opcion 2
    :return:
    """


def menu_option_3():
    """
    Funcion que se encarga de toda la ejecucion de la opcion 3
    :return:
    """


def menu_option_4():
    """
    Funcion que se encarga de toda la ejecucion de la opcion 4
    :return:
    """


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
