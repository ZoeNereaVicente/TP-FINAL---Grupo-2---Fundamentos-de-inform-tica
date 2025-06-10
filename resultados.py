def mostrar_resultados(unidades, superficies, promedio):
    """Muestra el promedio de expensas y el listado ordenado."""
    print(f"\nPromedio de expensas del mes: ${promedio:.2f}")
    print("Listado ordenado por superficie (mayor a menor):")
    for unidad, superficie in zip(unidades, superficies):
        print(f"Unidad: {unidad} - Superficie: {superficie:.2f} m²")