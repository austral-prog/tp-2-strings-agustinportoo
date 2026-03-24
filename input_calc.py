def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base=int(input("Base: "))
    altura=int(input("Altura: "))
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    area = (base*altura)
    print(f"Area: {area}")
    perimetro= (2*base + 2*altura)
    print(f"Perimetro: {perimetro}")
