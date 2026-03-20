def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    pass
    nombre=input("Nombre: ")
    nombre_min=(f"{nombre.lower()}")
    cont_a=("a" in nombre_min)
    print(f"Contiene a: {cont_a}")
    cont_e=("e" in nombre_min)
    print(f"Contiene e: {cont_e}")
    cont_i=("i" in nombre_min)
    print(f"Contiene i: {cont_i}")
    cont_o=("o" in nombre_min)
    print(f"Contiene o: {cont_o}")
    cont_u=("u" in nombre_min)
    print(f"Contiene u: {cont_u}") 
