from priority import calcular_prioridad
from validators import pedir_descripcion, pedir_opcion
from storage import guardar_ticket

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
    guardar_ticket(ticket)
    mostrar_ticket(ticket)
    print("\nTicket guardado en tickets.json.")

if __name__ == "__main__":
    main()