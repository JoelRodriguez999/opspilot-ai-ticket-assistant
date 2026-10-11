from priority import calcular_prioridad
from validators import pedir_descripcion, pedir_opcion
from storage import guardar_ticket, cargar_tickets
from datetime import datetime
from uuid import uuid4

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
        "id": str(uuid4()),
        "fecha_creacion": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
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

def mostrar_historial():
    """Muestra todos los tickets guardados."""

    tickets = cargar_tickets()

    if not tickets:
        print("\nTodavía no hay tickets guardados.")
        return

    print(f"\n=== Historial: {len(tickets)} tickets ===")

    for numero, ticket in enumerate(tickets, start=1):
        print(f"\nTicket {numero}")
        mostrar_ticket(ticket)
        
def main():
    while True:
        print("\n=== OpsPilot ===")
        print("1. Crear ticket")
        print("2. Consultar historial")
        print("3. Salir")

        opcion = pedir_opcion(
            "Selecciona una opción (1, 2 o 3): ",
            ["1", "2", "3"],
        )

        if opcion == "1":
            ticket = crear_ticket()
            guardar_ticket(ticket)
            mostrar_ticket(ticket)
            print("\nTicket guardado en tickets.json.")

        elif opcion == "2":
            mostrar_historial()

        elif opcion == "3":
            print("\nHasta pronto.")
            break

if __name__ == "__main__":
    main()