class Envio:
    """
    Clase Envio, registro vacio por ahora
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

    Esto lo hacemos para limpiar la output de consola obteniendo una ejecucion mas limpia
    Ya que no podemos hacer interfaces de usuario.
    """
    print("\n"*100)


