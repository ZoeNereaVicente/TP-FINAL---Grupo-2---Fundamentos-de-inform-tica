def calcular_promedio_expensas(superficies, valor_por_metro):
    """Calcula el promedio de expensas del mes."""
    if not superficies:
        return 0
    expensas = [superficie * valor_por_metro for superficie in superficies]
    return sum(expensas) / len(expensas)

def ordenar_por_superficie(unidades, superficies):
    """Ordena las listas de unidades y superficies por superficie (mayor a menor)."""
    pares = list(zip(superficies, unidades))
    pares_ordenados = sorted(pares, reverse=True)
    superficies_ordenadas, unidades_ordenadas = zip(*pares_ordenados)
    return list(unidades_ordenadas), list(superficies_ordenadas)