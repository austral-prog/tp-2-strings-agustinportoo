def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio = int(input())
    descuento = float(input())
    cantidad = int(input())

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")

    precio_con_descuento = (precio - descuento)
    print(f"Precio con descuento: {precio_con_descuento}")

    total = precio_con_descuento * cantidad
    print(f"Total: {total}")
