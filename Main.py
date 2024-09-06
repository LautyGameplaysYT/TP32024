from Gamma import *
from Beta import *


def main():
    """
    Funcion principal del script
    """
    menu()

def menu():
    """
    Funcion principal de managment del menu
    """
    menu_content()
    user_selected = None
    user_selected= input("Ingrese opcion deseada -->")
    if menu_validator(user_selected):
        clear()
        loop_var = menu_choice_caller(user_selected)
        if loop_var == -1:
            clear()
            menu()
    else:
        clear()
        menu()


if __name__ == '__main__':
    main()