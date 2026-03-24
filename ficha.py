def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre=input("Nombre: ")
    email=input("Email: ")
    nota_1=int(input("Nota1: "))
    nota_2=int(input("Nota2: "))
    nota_3=int(input("Nota: "))
    multilinea = """========================
    FICHA DEL ALUMNO
========================"""
    print(multilinea)
    nombre_limpio= (nombre.title().strip())
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(nombre_limpio)}")
    espacio=(nombre_limpio.find(" "))
    espacio_2=(espacio + 2)
    print(f"Iniciales: {nombre_limpio[0] + nombre_limpio[espacio+1:espacio_2]}")
    usuario= ((nombre_limpio.replace(nombre_limpio[:espacio],nombre_limpio[espacio+1:]).replace(" ",".")).lower())
    punto=usuario.find(".")
    usuario_parte1= (usuario[:punto+1])
    usuario_parte2=(nombre_limpio[:espacio].lower())
    print(f"Usuario: {usuario_parte1 + usuario_parte2}")
    print(f"Email valido: {"@" in email}")
    arroba=email.find("@")
    print(f"Dominio: {email[arroba+1:].lower()}")
    nombre_archivo=(nombre_limpio.replace(" ","_"))
    print(f"Nombre para archivo: {nombre_archivo}")
    print(f"Cantidad de a: {nombre_limpio.count("a")}")
    codigo=(nombre_limpio[::-1].upper())
    print(f"Codigo secreto: {codigo}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    suma=(nota_1 + nota_2 + nota_3)
    print(f"Suma: {suma}")
    promedio=(suma/3)
    print(f"Promedio: {float(promedio)}")
    promedio_entero=(suma//3)
    print(f"Promedio entero: {promedio_entero}")
    print("="*24)
