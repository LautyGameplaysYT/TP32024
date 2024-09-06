from Gamma import *


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
    menu_choice= input("Ingrese opcion deseada -->")
    if menu_validator(menu_choice):
        clear()
        menu_choice_opciones[menu_choice]()
    else:
        clear()
        menu()


if __name__ == '__main__':
    main()