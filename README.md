# 🤖 Prueba de Turing: Estudiante UTN FRCU

Un bot conversacional de consola diseñado para pasar la Prueba de Turing simulando ser un estudiante humano de 5to año de Ingeniería en Sistemas. Está construido con **Python**, orquestado con **LangChain** y potenciado por la API de **Google Gemini**.

## 📌 Características Principales

* **Ingeniería de Prompts Avanzada:** El modelo tiene instrucciones estrictas para anular su "sesgo de asistente". Responde de forma cortante, sin proactividad y con errores de tipeo intencionales.
* **Contexto Local:** Utiliza jerga y modismos propios de un universitario de la región de Entre Ríos (Concepción del Uruguay).
* **Evasión Táctica:** Posee un *backstory* programado (está renegando con un proyecto de Next.js) que utiliza estratégicamente para evadir preguntas sobre Inteligencia Artificial que delatarían su naturaleza de bot.
* **Memoria de Sesión:** Implementa `ChatMessageHistory` de LangChain para mantener el hilo de la conversación en tiempo real.

## 🛠️ Arquitectura y Tecnologías

* **Lenguaje:** Python 3
* **Framework LLM:** LangChain (`langchain`, `langchain-community`)
* **Modelo LLM:** Google Gemini (`langchain-google-genai`, utilizando el modelo `gemini-2.0-flash`)

## 🚀 Instalación y Configuración

Los siguientes pasos están optimizados para evitar conflictos de dependencias en el sistema operativo (especialmente en macOS con PEP 668).

1. **Clonar el repositorio:**
  python3 -m venv venv
  source venv/bin/activate

2. Crear y activar un entorno virtual aislado:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

3. Instalar las dependencias del proyecto:
  pip install langchain langchain-google-genai langchain-community

4. Configurar las credenciales:
   Necesitás una API Key gratuita de Google AI Studio. Una vez generada, exportala en tu terminal:
   ```
    export GEMINI_API_KEY="TU_CLAVE_AQUI"
   ```

🎮 Ejecución

Con el entorno virtual activado y la variable de entorno configurada, dale arranque al script principal:
```
python estudianteUTN.py
```
