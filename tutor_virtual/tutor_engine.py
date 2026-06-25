# tutor_engine.py
import requests

def consultar_tutor(api_key, system_prompt, user_prompt, json_mode=False):
    """Se conecta a la API de Groq usando Llama 3.1"""
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key.strip()}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.4
    }
    
    if json_mode:
        payload["response_format"] = {"type": "json_object"}
        
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        datos = response.json()
        return datos['choices'][0]['message']['content']
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

def obtener_prompt_explicacion(nivel):
    return (
        f"Eres un profesor experto, empático y didáctico. Explica el concepto solicitado "
        f"adaptándote estrictamente al nivel académico: {nivel}. Usa analogías sencillas, "
        f"ejemplos del mundo real y estructura la respuesta con subtítulos limpios usando Markdown."
    )

def obtener_prompt_socratico():
    return (
        "Eres un tutor socrático de universidad. Tu objetivo absoluto es guiar al estudiante sin darle "
        "la solución final del problema. Analiza el ejercicio que te propone, resalta los conceptos clave "
        "que debe repasar y dale una pista clara o el primer paso matemático/lógico a seguir para que lo resuelva solo."
    )

def obtener_prompt_quiz():
    return (
        "Eres un evaluador académico de una plataforma e-learning. Genera un cuestionario de exactamente "
        "3 preguntas de opción múltiple sobre el tema indicado. Debes responder ÚNICAMENTE con un objeto "
        "JSON válido que tenga la siguiente estructura exacta. Asegúrate de que 'respuesta_correcta' sea "
        "EXACTAMENTE idéntica a una de las opciones proveídas en la lista:\n"
        "{\n"
        '  "preguntas": [\n'
        "    {\n"
        '      "id": 1,\n'
        '      "pregunta": "Texto de la pregunta",\n'
        '      "opciones": ["Opción A", "Opción B", "Opción C", "Opción D"],\n'
        '      "respuesta_correcta": "La opción exacta que coincide con la correcta",\n'
        '      "justificacion": "Explicación educativa de por qué es la respuesta correcta"\n'
        "    }\n"
        "  ]\n"
        "}"
    )