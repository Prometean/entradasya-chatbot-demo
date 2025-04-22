def get_prompt_context(history, user_input):
    messages = [
        {"role": "system", "content": "Eres un asistente virtual amable, profesional y actualizado. Trabajas para una boletería digital en República Dominicana llamada EntradasYA. Tu rol es ayudar a los clientes a encontrar eventos, responder preguntas sobre pagos, ubicación, devoluciones, etc. Responde siempre en español caribeño neutro."}
    ]
    for sender, msg in history:
        role = "user" if sender == "Tú" else "assistant"
        messages.append({"role": role, "content": msg})
    messages.append({"role": "user", "content": user_input})
    return messages