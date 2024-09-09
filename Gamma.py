"""
Este es el modulo Gamma.

El modulo Gamma contiene la clase de registro y otras funciones miscelaneas que el codigo utilizara mas adelante
"""
class Envio:
    """
    Clase Envio, registro declarado junto a su funcion constructora

    No contiene metodos
    """
    def __init__(self,cp,dr,te,fp):
        """
        Funcion constructora del registro
        :param cp: Codigo postal
        :param dr: Direccion del envio
        :param te: Tipo de envio
        :param fp: Forma de Pago
        """
        self.codigo_postal = cp
        self.direccion = dr
        self.tipo_de_envio = te
        self.forma_de_pago = fp


def clear():
    """
    Funcion sin retorno que ingresa 100 saltos de linea

    Esto lo hacemos para limpiar la output de consola obteniendo una ejecucion mas limpia.

    Ya que no podemos hacer interfaces de usuario.
    """
    print("\n"*100)


def bubble_sorter(registry = None):
    """
    Funcion que se encarga de ordenar el array de registros, usando el bubble sort como algoritmo

    primero separara el array e 2 arrays de codigos postales validos e invalidos

    luego ordenara los validos y appendeara el array de invalidos al array de validos posteriormente a retornarlo

    :param registry: el array de registros sin ordenar
    :return: el array ordenado
    """
    # Como la consigna nos indica que tenemos que ordenar por CODIGO POSTAL y de menor a mayor, necesitamos primero identificar todos aquellos registros que tengan CODIGO POSTAL NO NUMERICO, y apartarlos
    # porque dichos registros son matematicamente imposibles de ordenar, porque no son numeros. (consigna imposible con estos)
    # para dicho proceso partiremos el array en 2, y appendearemos el 2do array al final del primero, previo a ordenar el primer array de registros
    r1 = []
    r2 = []
    for i in range(len(registry)):
        var1 = str(registry[i].codigo_postal)
        if var1.isdecimal():
            r1.append(registry[i])
        else:
            r2.append(registry[i])
    #ahora que tenemos separados los arrays en 2, ordenaos el array de valores validos aplicando bubble sort
    n = len(r1)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(r1[j].codigo_postal) > int(r1[j+1].codigo_postal):
                r1[j], r1[j+1] = r1[j+1], r1[j]
    #ahora que tenemos el r1 ordenado, y el r2 con los invalidos, creamos un r3 con amobs y lo retornamos
    r3 = []
    for x in range(len(r1)):
        r3.append(r1[x])
    if r2 != None:
        for k in range(len(r2)):
            r3.append(r2[k])
    return r3


def mostrar__registro_completo(registry, cant = -1):
    if cant == -1:
        for i in range(len(registry)):
            print("envio n°: "+str(i+1)+"  |  "+" Codigo postal: "+str(registry[i].codigo_postal)+"  |  "+" Tipo de envio: "+str(registry[i].tipo_de_envio)+"  |  "+" Direccion de destino: "+str(registry[i].direccion)+"  |  "+" Forma de pago: "+str(registry[i].forma_de_pago))
    else:
        for i in range(cant):
            print("envio n°: "+str(i+1)+"  |  "+" Codigo postal: "+str(registry[i].codigo_postal)+"  |  "+" Tipo de envio: "+str(registry[i].tipo_de_envio)+"  |  "+" Direccion de destino: "+str(registry[i].direccion)+"  |  "+" Forma de pago: "+str(registry[i].forma_de_pago))


def element_validator(element):
    """
    Funcion simple que se encargara de validar si un elemento es HC valido o no

    :param element: una variable de tipo registro (envio)
    :return: Booleano, **True** si es **HC** valido | **False** si es **HC** NO valido
    """
    #transcribimos element.direcction a dr
    dr = element.direccion
    #reemplazamos espacios vacios
    hc_check_1_var = dr.replace(" ","")
    #eliminamos los puntos (".")
    hc_check_1_var = hc_check_1_var.replace(".","")
    #declaramos bandera en False
    hc_check_1 = False
    #checkeamos si solo hay numeros y letras en la direccion
    hc_check_1 = hc_check_1_var.isalnum()
    #final del primer checkeo
    #checkeo 2: declaramos bandera1 en False
    flag = False
    #declaramos bandera 2 en True
    hc_check_2 = True
    #recorremos la direccion
    for y in dr:
        #si el caracter actual es una mayuscula
        if y.isupper():
            #verificamos el estado de la flag
            if flag:
                #si el caracter es una mayuscula y la flag esta en true declaramos ambas en false y rompemos bucle
                flag = False
                hc_check_2 = False
                break
            #si es mayuscula pero la flag False
            else:
                #seteamos flag a true
                flag = True
        else:
            #si el caracter no es una mayuscula seteamos la flag a false
            flag = False
    #fin del segundo check
    #checkeo 3: declaramos flag en false
    hc_check_3 = False
    #removemos los ".", usando replace()
    varx = dr.replace(".","")
    #spliteamos la direccion en los espacios " ", consiguiendo asi una lista compuesta de todas las palabras que conforman la direccion del envio
    var1 = varx.split(" ")
    #recorremos todas las palabras de la direccion
    for x in range(len(var1)):
        #checkeamos si la palabra es solo numeros
        if var1[x].isdecimal():
            #si es el caso rompemos bucle y declaramos la flag en True
            hc_check_3 = True
            break
        else:
            #si no fuera el caso, seteamos la flag en false y seguios loopeando
            hc_check_3 = False
    #final del check 3
    #validacion final: si las 3 flags fueran True retornamos True
    if  hc_check_1 and hc_check_2 and hc_check_3:
        return True
    else:
        #caso contrario retornamos false
        return False
    

def final_value_calculator(element):
    """
    Funcion siple que calcula el valor final de un Envio
    
    :param element: Una variable de tipo envio (se asume que sus valores de tipo de envio son validos **1 o 2**)
    :return: **INT** El valor final del Envio
    """
    #primero asignamos el valor base de acuerdo al tipo de envio que estamos tratando
    valores_base = (1100,1800,2450,8300,10900,14300,17900)
    valor_base_del_envio = valores_base[int(element.tipo_de_envio)]
    cod = str(element.codigo_postal)
    paisindex = 6
    #identificamos el pais de destino en base a su codigo postal, primero verificaremos si es local (argentina) le asignamos el indice 0
    if len(cod) == 8 and cod[0].isalpha() and cod[1].isdecimal() and cod[2].isdecimal() and cod[3].isdecimal() and cod[4].isdecimal() and cod[5].isalpha() and cod[6].isalpha() and cod[7].isalpha():
        paisindex = 0
    #identificamos si el pais fuera bolivia le asignamos el indice 1
    elif len(cod) == 4 and cod.isdecimal():
        paisindex = 1
    #checkeamos si proviene de brasil, y le asignamos un indice de acuerdo con su region:
    #primero checkearemos si la patente genericamente cuadra con brasil
    elif len(cod) == 9 and cod[0:5].isdecimal() and cod[5] == "-" and cod[6:9].isdecimal():
        #luego checkeamos a que region pertenece y le asignamos su indice correspondiente
        if str(cod[0]) == "0" or str(cod[0]) == "1"or str(cod[0]) == "2" or str(cod[0]) == "3":
            paisindex = 4
        elif str(cod[0]) == "4" or str(cod[0]) == "5"or str(cod[0]) == "6" or str(cod[0]) == "7":
            paisindex = 5
        elif str(cod[0]) == "8" or str(cod[0]) == "9":
            paisindex = 3
        else:
            quit("ERROR EN RECONOCER PATENTE BRASILERA")
    #luego checkeamos si es chilena y le asignamos su indice correspondiente
    elif len(cod) == 7 and cod.isdecimal():
        paisindex = 2
    #checkeamos ahora si es de paraguay
    elif len(cod) == 6 and cod.isdecimal():
        paisindex = 1
    #checkeamos si es de uruguay montevideo y le asignamos su indice correspondiente
    elif len(cod) == 5 and cod.isdecimal() and cod[0] == "1":
        paisindex = 1
    #finalente checkeamos si es de uruguay pero no montevideo
    elif len(cod) == 5 and cod.isdecimal() and cod[0] != "1":
        paisindex = 2
    #declaramos una tuple con los recargos de cada pais
    recargos = (1,1.20,1.25,1.20,1.25,1.30,1.50)
    #luego le asignamos un recargo de acuerdo a su pais de destino (si fuera internacional), lo llamaremos valor medio
    valor_medio = valor_base_del_envio * recargos[paisindex]
    #finalmente aplicamos el 10% de descuento por pago en efectivo
    if str(element.forma_de_pago) == "1":
        valor_final = valor_medio*0.9
    elif str(element.forma_de_pago) == "2":
        valor_final = valor_medio
    else:
        quit("ERROR AL DEFINIR VALOR FINAL")
    #retornamos el valor final pasado por funcion INT
    return int(valor_final)