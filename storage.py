import json
from pathlib import Path


ARCHIVO_TICKETS = Path(__file__).resolve().parent / "tickets.json"


def cargar_tickets():
    """Lee el historial y detecta errores de formato."""

    if not ARCHIVO_TICKETS.exists():
        return []

    try:
        with ARCHIVO_TICKETS.open("r", encoding="utf-8") as archivo:
            tickets = json.load(archivo)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ValueError(
            "El archivo tickets.json está dañado o tiene un formato inválido."
        ) from error

    if not isinstance(tickets, list):
        raise ValueError(
            "El archivo tickets.json debe contener una lista de tickets."
        )

    if not all(isinstance(ticket, dict) for ticket in tickets):
        raise ValueError(
            "Cada ticket del historial debe ser un objeto JSON."
        )

    return tickets


def guardar_ticket(ticket):
    """Añade un ticket al historial y guarda la lista completa."""

    tickets = cargar_tickets()
    tickets.append(ticket)

    with ARCHIVO_TICKETS.open("w", encoding="utf-8") as archivo:
        json.dump(tickets, archivo, ensure_ascii=False, indent=4)

def buscar_ticket_por_id(ticket_id):
    """Busca un ticket por su ID y devuelve None si no existe."""

    for ticket in cargar_tickets():
        if ticket.get("id") == ticket_id:
            return ticket

    return None

def actualizar_estado_ticket(ticket_id, nuevo_estado):
    """Actualiza el estado y devuelve True si encuentra el ticket."""

    tickets = cargar_tickets()

    for ticket in tickets:
        if ticket.get("id") == ticket_id:
            ticket["estado"] = nuevo_estado

            with ARCHIVO_TICKETS.open("w", encoding="utf-8") as archivo:
                json.dump(tickets, archivo, ensure_ascii=False, indent=4)

            return True

    return False