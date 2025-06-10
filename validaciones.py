def validar_unidad(unidad, unidades):
    """Valida que el número de unidad sea entero, esté entre 1 y 20, y no esté duplicado."""
    try:
        unidad = int(unidad)
        if unidad < 1 or unidad > 20:
            return False, "El número de unidad debe estar entre 1 y 20."
        if unidad in unidades:
            return False, "El número de unidad ya está registrado."
        return True, ""
    except ValueError:
        return False, "El número de unidad debe ser un entero."

def validar_superficie(superficie):
    """Valida que la superficie sea un número flotante mayor a 0."""
    try:
        superficie = float(superficie)
        if superficie <= 0:
            return False, "La superficie debe ser mayor a 0."
        return True, ""
    except ValueError:
        return False, "La superficie debe ser un número válido."

def validar_valor_por_metro(valor):
    """Valida que el valor por metro cuadrado sea un número flotante mayor a 0."""
    try:
        valor = float(valor)
        if valor <= 0:
            return False, "El valor por metro cuadrado debe ser mayor a 0."
        return True, ""
    except ValueError:
        return False, "El valor por metro cuadrado debe ser un número válido."