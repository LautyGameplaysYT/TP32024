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
            else:
                menu_choice_caller(user_selected, registry)


if __name__ == '__main__':
    main()