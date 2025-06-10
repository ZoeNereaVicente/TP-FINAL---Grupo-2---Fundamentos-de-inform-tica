from validaciones import validar_unidad, validar_superficie, validar_valor_por_metro

def ingresar_datos():
    """Permite ingresar unidades, superficies y valor por metro cuadrado."""
    unidades = []
    superficies = []

    print("Ingreso de unidades (máximo 20). Ingrese '0' para finalizar.")
    while len(unidades) < 20:
        unidad_input = input("Número de unidad (1-20, 0 para salir): ")
        if unidad_input == '0':
            break

        es_valido, mensaje = validar_unidad(unidad_input, unidades)
        if not es_valido:
            print(f"Error: {mensaje}")
            continue

        superficie_input = input("Superficie en m²: ")
        es_valido, mensaje = validar_superficie(superficie_input)
        if not es_valido:
            print(f"Error: {mensaje}")
            continue

        unidades.append(int(unidad_input))
        superficies.append(float(superficie_input))

    if not unidades:
        print("No se ingresaron unidades.")
        return None, None, None

    while True:
        valor_input = input("Valor por metro cuadrado: ")
        es_valido, mensaje = validar_valor_por_metro(valor_input)
        if es_valido:
            break
        print(f"Error: {mensaje}")

    return unidades, superficies, float(valor_input)