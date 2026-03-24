def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)

    print("Dinero recibido")
    dinero_recibido = int(input())
    print(dinero_recibido)

    vuelto = dinero_recibido - gasto

    print()
    print("Vuelto")
    print()

    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
