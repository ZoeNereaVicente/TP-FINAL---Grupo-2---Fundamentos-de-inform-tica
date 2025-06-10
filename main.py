from datos import ingresar_datos
from calculos import calcular_promedio_expensas, ordenar_por_superficie
from resultados import mostrar_resultados

def main():
    """Función principal del sistema."""
    print("Sistema de Gestión de Expensas")

    unidades, superficies, valor_por_metro = ingresar_datos()

    if unidades is None:
        return

    promedio = calcular_promedio_expensas(superficies, valor_por_metro)
    unidades, superficies = ordenar_por_superficie(unidades, superficies)
    mostrar_resultados(unidades, superficies, promedio)

if __name__ == "__main__":
    main()