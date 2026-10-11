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