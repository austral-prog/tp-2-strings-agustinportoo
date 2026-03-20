def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass

    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    nombre_completo= (nombre+ " "+ apellido)

    print(f"{nombre_completo.lower()}")
    print(f"{nombre_completo.title()}")
    print(f"{nombre_completo.upper()}")
    print(f"\t{nombre_completo.lower()}")
