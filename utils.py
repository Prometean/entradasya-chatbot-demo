def simulate_event_response(user_input, reply):
    events = [
        {"nombre": "Festival del Merengue", "fecha": "viernes 20 de abril", "lugar": "Parque Mirador Sur"},
        {"nombre": "Concierto de Música Urbana", "fecha": "sábado 21 de abril", "lugar": "Estadio Olímpico"},
        {"nombre": "Stand Up Comedy Night", "fecha": "domingo 22 de abril", "lugar": "Barcelo Convention Center"},
    ]
    if "eventos" in user_input.lower():
        eventos_listado = "\n\n".join([f"🎤 {e['nombre']}\n📅 {e['fecha']}\n📍 {e['lugar']}" for e in events])
        reply += f"\n\nEstos son algunos eventos destacados de esta semana:\n{eventos_listado}"
    return reply
