Debido a varias dificultades y errores con Google Gemini API se optó por otra alternativa


🔧 Instrucciones de Instalación y Configuración
Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. Crear y activar el entorno virtual (.venv)
Es altamente recomendable usar un entorno limpio para instalar las librerías:

python -m venv .venv
.venv\Scripts\activate

python -m venv .venv
2. Instalar las dependencias
Instala los paquetes necesarios listados en el archivo requirements.txt:

pip install -r requirements.txt

3. Obtener la API Key de Groq
Regístrate o inicia sesión de manera gratuita en Groq Console.

Ve a la sección API Keys en el menú lateral izquierdo.

Haz clic en Create API Key, asígnale un nombre y copia la clave generada (empezará con gsk_...).

🖥️ Ejecución de la Aplicación
Para encender el servidor local de Streamlit, ejecuta el siguiente comando en tu terminal con el entorno virtual activo:

streamlit run app_tutor.py
La aplicación se abrirá automáticamente en tu navegador web predeterminado (usualmente en la dirección http://localhost:8501). Introduce tu API Key en la barra de texto inicial para activar las funciones del tutor.

📝 Licencia
Este proyecto fue desarrollado con fines educativos como parte del módulo de Sistemas Inteligentes y Desarrollo de Aplicaciones con IA.