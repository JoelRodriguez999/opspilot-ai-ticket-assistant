def crear_ticket():
    """Solicita los datos básicos de un incidente y los organiza."""

    print("\n=== Registro inicial de incidente ===")

    descripcion = input("Describe el incidente: ").strip()
    impacto = input("Impacto (bajo, medio o alto): ").strip().lower()
    urgencia = input("Urgencia (baja, media o alta): ").strip().lower()

    ticket = {
        "descripcion": descripcion,
        "impacto": impacto,
        "urgencia": urgencia,
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