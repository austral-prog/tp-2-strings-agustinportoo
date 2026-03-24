def ficha():
    nombre = input()
    email = input()
    nota_1 = int(input())
    nota_2 = int(input())
    nota_3 = int(input())

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")

    nombre_limpio = nombre.strip().title()
    print(f"Nombre: {nombre_limpio}")

    email_lower = email.lower()
    print(f"Email: {email_lower}")

    print(f"Caracteres en nombre: {len(nombre_limpio)}")

    espacio = nombre_limpio.find(" ")
    iniciales = nombre_limpio[0] + nombre_limpio[espacio + 1]
    print(f"Iniciales: {iniciales}")

    nombre_parte = nombre_limpio[:espacio].lower()
    apellido_parte = nombre_limpio[espacio + 1:].lower()
    print(f"Usuario: {apellido_parte}.{nombre_parte}")

    print(f"Email valido: {'@' in email}")

    arroba = email.find("@")
    print(f"Dominio: {email[arroba + 1:].lower()}")

    print(f"Nombre para archivo: {nombre_limpio.replace(' ', '_')}")

    print(f"Cantidad de a: {nombre_limpio.lower().count('a')}")

    print(f"Codigo secreto: {nombre_limpio[::-1].upper()}")

    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")

    suma = nota_1 + nota_2 + nota_3
    print(f"Suma: {suma}")

    promedio = suma / 3
    print(f"Promedio: {promedio}")

    print(f"Promedio entero: {suma // 3}")

    print("=" * 24)
