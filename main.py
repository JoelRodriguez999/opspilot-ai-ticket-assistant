def pedir_descripcion():
    """Repite la pregunta hasta recibir una descripción con texto."""

    while True:
        descripcion = input("Describe el incidente: ").strip()

        if descripcion:
            return descripcion

        print("La descripción no puede estar vacía. Inténtalo de nuevo.")


def pedir_opcion(mensaje, opciones):
    """Repite la pregunta hasta recibir una opción permitida."""

    while True:
        respuesta = input(mensaje).strip().lower()

        if respuesta in opciones:
            return respuesta

        print(f"Opción inválida. Escribe: {', '.join(opciones)}.")

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

def crear_ticket():
    """Solicita datos válidos y calcula la prioridad del incidente."""

    print("\n=== Registro inicial de incidente ===")

    descripcion = pedir_descripcion()

    impacto = pedir_opcion(
        "Impacto (bajo, medio o alto): ",
        ["bajo", "medio", "alto"],
    )

    urgencia = pedir_opcion(
        "Urgencia (baja, media o alta): ",
        ["baja", "media", "alta"],
    )

    prioridad = calcular_prioridad(impacto, urgencia)

    ticket = {
        "descripcion": descripcion,
        "impacto": impacto,
        "urgencia": urgencia,
        "prioridad": prioridad,
        "estado": "nuevo",
    }

    return ticket


def mostrar_ticket(ticket):
    """Muestra ordenadamente la información registrada."""

    print("\n=== Ticket registrado ===")

    for campo, valor in ticket.items():
        print(f"{campo.capitalize()}: {valor}")


def main():
    ticket = crear_ticket()
    mostrar_ticket(ticket)


if __name__ == "__main__":
    main()