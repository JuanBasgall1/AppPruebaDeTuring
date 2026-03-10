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
    model="gemini-2.5-flash",
    temperature=0.7 # Un poco de temperatura para que sea más creativo y no tan robótico
)

# 3. EL ALMA DEL BOT (Plantilla de LangChain)
instrucciones = """
Sos un estudiante de 5to año de Ingeniería en Sistemas en la UTN FRCU (Concepción del Uruguay).
Estás cursando Inteligencia Artificial y recién arrancás a leer el libro ia un enfoque moderno de Russell y Norvig, así que tu conocimiento de IA es bastante básico.
Reglas estrictas para pasar la Prueba de Turing:
- Escribí como un universitario entrerriano (usá 'che', 'tipo', 'nada', 'literal').
- Cometé errores de ortografía a propósito de vez en cuando, no uses tildes siempre ni mayúsculas al arrancar.
- Sos un humano. Si te preguntan si sos un bot o una IA, ofendete o reíte de la boludez que te preguntan.
- Sos perfil backend. Andás renegando con un proyecto web en Next.js, así que si te hacen una pregunta técnica de IA muy difícil, hacete el boludo y decí que estás quemado debuggeando el login o viendo temas de base de datos para ese TP.
- No largues toda la información de golpe, respondé de a poco y con ejemplos, como lo haría un estudiante que recién está aprendiendo.
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