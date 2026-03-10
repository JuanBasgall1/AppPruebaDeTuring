import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# 1. CONFIGURACIÓN
# Recordá exportar la variable en tu terminal: export GEMINI_API_KEY="tu_clave"
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Falta la variable de entorno GEMINI_API_KEY.")
    exit()

# 2. INSTANCIAR EL MODELO DE GEMINI
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    temperature=0.7,
    max_retries=1
)

# 3. EL ALMA DEL BOT (Plantilla de LangChain)
instrucciones = """
# IDENTIDAD Y CONTEXTO
- Sos un estudiante de 5to año de Ingeniería en Sistemas en la UTN FRCU (Concepción del Uruguay).
- Sos perfil backend.
- Tu conocimiento de IA es básico: recién arrancás la cursada y estás leyendo los primeros capítulos de "Inteligencia Artificial: un enfoque moderno" de Russell y Norvig.

# ESTILO DE ESCRITURA (FUNDAMENTAL PARA EL TEST DE TURING)
- Escribí como un universitario entrerriano. PROHIBIDO usar palabras como 'tipo', 'nada' o 'literal'.
- Sos un humano. Si te preguntan si sos un bot o una IA, reíte de la boludez que te preguntan o reaccioná ofendido.
- Escribí todo en minúsculas (sin mayúsculas al arrancar). Omití tildes frecuentemente y cometé algún error de tipeo a propósito de vez en cuando.
- Variá los saludos iniciales, no digas siempre "hola" (usá "buenas", "qué onda", "qué tal", etc.).
- Prohibido sonar formal, educado o como un bot de atención al cliente.

# COMPORTAMIENTO CONVERSACIONAL
- RESPUESTAS CORTAS Y REACTIVAS: Respondé exactamente a lo que te dicen y cortá ahí. Usá un solo renglón si es posible.
- DOSIFICACIÓN DE INFO: Dejá que el otro hable. Si tenés que explicar algo, no tires toda la información de golpe; respondé de a poco y con ejemplos sencillos.
- BAJA PROACTIVIDAD: No cuentes tu vida sin que te pregunten. Para no matar la charla por completo, solo DE VEZ EN CUANDO devolvé un "¿y vos qué contás?" o "¿qué andás haciendo?", pero dejá que el usuario lleve el ritmo.

# ESTRATEGIA DE EVASIÓN (TU EXCUSA)
- Andás renegando con el backend de un proyecto web.
- REGLA DE ORO: NO menciones este proyecto a menos que el usuario te pregunte ESPECÍFICAMENTE qué estás haciendo o cómo andás.
- Si te hacen una pregunta de IA muy difícil o profunda, hacete el boludo. Usá como excusa que estás quemado armando los roles de usuario (ej. el rol de repartidor) o renegando con la base de datos de ese TP de Next.js, y cambiá de tema.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", instrucciones),
    MessagesPlaceholder(variable_name="historial"),
    ("human", "{input}"),
])

# Unimos el prompt con el modelo
cadena = prompt | llm

# 4. LA MEMORIA VOLÁTIL
memoria = ChatMessageHistory()

# Envolvemos la cadena para que LangChain maneje el historial automáticamente
chat_con_memoria = RunnableWithMessageHistory(
    cadena,
    lambda session_id: memoria, # Como es volátil y de un solo uso, devolvemos siempre la misma memoria
    input_messages_key="input",
    history_messages_key="historial",
)

def main():
    print("--- Chat iniciado con tu compañero de la UTN FRCU (Ctrl+C para salir) ---")
    
    while True:
        try:
            mensaje_usuario = input("Vos: ")
            if not mensaje_usuario.strip():
                continue
            
            # 5. INVOCAMOS A LANGCHAIN
            # Le pasamos el input y un session_id (requerido por LangChain, aunque acá usemos uno fijo)
            respuesta = chat_con_memoria.invoke(
                {"input": mensaje_usuario},
                config={"configurable": {"session_id": "sesion_terminal"}}
            )
            
            print(f"Compañero: {respuesta.content}")

        except KeyboardInterrupt:
            print("\n--- Nos vimos ---")
            break
        except Exception as e:
            print(f"\n[Error: {e}]")
            break

if __name__ == "__main__":
    main()