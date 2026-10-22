from priority import calcular_prioridad
from validators import pedir_descripcion, pedir_opcion
from storage import (
    guardar_ticket,
    cargar_tickets,
    buscar_ticket_por_id,
    actualizar_estado_ticket,
)
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

def consultar_ticket_por_id():
    """Solicita un ID y muestra el ticket si existe."""

    ticket_id = input("\nIntroduce el ID del ticket: ").strip()
    ticket = buscar_ticket_por_id(ticket_id)

    if ticket is None:
        print("\nNo se encontró ningún ticket con ese ID.")
        return

    mostrar_ticket(ticket)

def cambiar_estado_ticket():
    """Solicita un ID y permite actualizar el estado del ticket."""

    ticket_id = input("\nIntroduce el ID del ticket: ").strip()
    ticket = buscar_ticket_por_id(ticket_id)

    if ticket is None:
        print("\nNo se encontró ningún ticket con ese ID.")
        return

    mostrar_ticket(ticket)

    nuevo_estado = pedir_opcion(
        "\nNuevo estado (nuevo, en progreso o resuelto): ",
        ["nuevo", "en progreso", "resuelto"],
    )

    if actualizar_estado_ticket(ticket_id, nuevo_estado):
        print(f"\nEstado actualizado a: {nuevo_estado}.")
    else:
        print("\nNo se encontró ningún ticket con ese ID.")

def main():
    while True:
        print("\n=== OpsPilot ===")
        print("1. Crear ticket")
        print("2. Consultar historial")
        print("3. Buscar ticket por ID")
        print("4. Actualizar estado")
        print("5. Salir")

        opcion = pedir_opcion(
            "Selecciona una opción (1, 2, 3, 4 o 5): ",
            ["1", "2", "3", "4", "5"],
        )

        if opcion == "1":
            ticket = crear_ticket()
            guardar_ticket(ticket)
            mostrar_ticket(ticket)
            print("\nTicket guardado en tickets.json.")

        elif opcion == "2":
            mostrar_historial()

        elif opcion == "3":
            consultar_ticket_por_id()

        elif opcion == "4":
            cambiar_estado_ticket()

        elif opcion == "5":
            print("\nHasta pronto.")
            break

if __name__ == "__main__":
    main()