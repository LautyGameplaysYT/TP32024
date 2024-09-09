"""
Este es el modulo Main

El modulo main contiene el control de flujo "if __name__" ademas del bucle principal del menu y la funcion de ejecucion principal del programa.
"""

#COMENTARIOS PARA QUIEN NOS CORRIGA EL TP:

#Todas las funciones tienen documentación custom. colocando el cursor por encima le dara una breve descripcion de lo que hace esa funcion/clase/modulo.
#Que parametros toma, Que retorna, etc

#Ademas en las partes mas "spagetti" del codigo cada 2 o 3 lineas de codigo hay comentarios explicando nuestro tren de pensamiento a la hora de programarlo.

#El programa se encuentra dividido en 5 modulos: el modulo principal (main) y 4 modulos auxiliares que decidimos llamar con letras del alfabeto griego porque quedaba fachero ;)
#Al igual que las funciones, los modulos tabien tienen una breve docuentacion custom de lo que contienen y su proposito.

#Una vez que nos corrija y devuelva el tp, si no es mucha molestia, nos podria pasar el archivo/archivos que utilizen para la correccion del tp junto con los valores que el programa deberia de tirar?
#Esto por si nos va mal, poder aprender y encontrar nuestros errores, porque la verdad sin ese documento encontrar errores en un codigo que aparentemente funciona correctamente es una mision imposible :)
#Un buen lugar para pasarnos los archivos seria en un link en el comentario de la correccion en la pagina de la uv si le queda comodo.
from Gamma import *
from Beta import *


def main():
    """
    Función principal del script
    """
    menu()


def menu():
    """
    Funcion principal de managment del menu
    """
    registry = None
    while True:
        clear()
        menu_content()
        user_selected = None
        user_selected= input("Ingrese opcion deseada -->")
        if menu_validator(user_selected):
            clear()
            if user_selected == "1":
                registry = menu_choice_caller(user_selected)
            elif user_selected == "2":
                registry = menu_choice_caller(user_selected,registry)
            elif user_selected == "5":
                registry = menu_choice_caller(user_selected,registry)
            else:
                menu_choice_caller(user_selected, registry)


if __name__ == '__main__':
    main()