import json
from pathlib import Path


ARCHIVO_TICKETS = Path(__file__).resolve().parent / "tickets.json"


def cargar_tickets():
    """Lee los tickets guardados o devuelve una lista vacía."""

    if not ARCHIVO_TICKETS.exists():
        return []

    with ARCHIVO_TICKETS.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_ticket(ticket):
    """Añade un ticket al historial y guarda la lista completa."""

    tickets = cargar_tickets()
    tickets.append(ticket)

    with ARCHIVO_TICKETS.open("w", encoding="utf-8") as archivo:
        json.dump(tickets, archivo, ensure_ascii=False, indent=4)