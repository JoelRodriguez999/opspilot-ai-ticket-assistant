def calcular_prioridad(impacto, urgencia):
    """Calcula la prioridad utilizando una matriz de reglas."""

    matriz = {
        "bajo": {
            "baja": "P4 - Baja",
            "media": "P3 - Media",
            "alta": "P3 - Media",
        },
        "medio": {
            "baja": "P3 - Media",
            "media": "P3 - Media",
            "alta": "P2 - Alta",
        },
        "alto": {
            "baja": "P3 - Media",
            "media": "P2 - Alta",
            "alta": "P1 - Crítica",
        },
    }

    return matriz[impacto][urgencia]