import google.generativeai as genai
import os

# Levantamos la clave que ya tenés exportada en la consola
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Falta la API KEY.")
    exit()

genai.configure(api_key=api_key)

print("--- Modelos disponibles para tu cuenta ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error al consultar: {e}")