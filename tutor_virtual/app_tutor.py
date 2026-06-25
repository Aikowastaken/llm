
import streamlit as st
import json
import tutor_engine as engine

# Configuración de página
st.set_page_config(
    page_title="EstudIA | Tutor virtual ", 
    page_icon="🎓", 
    layout="wide"
)

# --- SISTEMA DE DISEÑO ADAPTATIVO MEJORADO ---
st.markdown("""
    <style>
    /* El fondo de la app cambia según el tema activo */
    .stApp { background-color: var(--background-color); } 
    
    /* Títulos dinámicos que se adaptan al Modo Claro y Oscuro */
    .main-title { 
        font-size: 2.6rem; 
        font-weight: 800; 
        color: #1E3A8A; 
        margin-bottom: 2px; 
        font-family: 'Helvetica Neue', sans-serif; 
    }
    
    /* Subtítulos adaptables en contraste */
    .subtitle { 
        font-size: 1.15rem; 
        color: var(--text-color); 
        opacity: 0.8;
        margin-bottom: 30px; 
    }
    
    /* Configuración dinámica de la Barra Lateral para combinar en ambos modos */
    [data-testid="stSidebar"] { 
        background-color: var(--background-color); 
        border-right: 1px solid rgba(128, 128, 128, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- PANEL DE CONTROL LATERAL (DINÁMICO) ---
with st.sidebar:
    st.write("")
    st.image("https://cdn-icons-png.flaticon.com/512/3413/3413535.png", width=70)
    st.markdown("### **EstudIA Control**")
    st.caption("Portal de Acceso Universitario")
    st.write("---")
    
    api_key = st.text_input("Clave de Acceso (API Key):", type="password")
    st.write("---")
    st.caption("Conexión cifrada directa con los modelos académicos.")

# --- CUERPO PRINCIPAL ---
left_space, main_col, right_space = st.columns([1, 6, 1])

with main_col:
    st.markdown('<div class="main-title">EstudIA: tutor virtual</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Una forma de estudio más personal.</div>', unsafe_allow_html=True)

    if api_key:
        tab1, tab2, tab3 = st.tabs(["Cátedra Virtual", "Tutoría de Proyectos", "Módulo de Evaluación"])

        # ---------------------------------------------------------
        # PESTAÑA 1: CÁTEDRA VIRTUAL (EXPLICADOR)
        # ---------------------------------------------------------
        with tab1:
            # Usamos contenedores nativos con borde para evitar cuadros vacíos u opacos
            with st.container(border=True):
                st.markdown("### Aula de Conceptos Adaptativos")
                st.write("Especifica un tema de estudio y el modelo ajustará la profundidad pedagógica de forma inmediata.")
                
                tema = st.text_input("¿Qué concepto o materia deseas analizar hoy?", placeholder="Ej. Redes Neuronales Convolucionales, Álgebra Lineal...")
                
                nivel = st.select_slider(
                    "Nivel de profundidad académica requerido:",
                    options=["Nivel Escolar (Explicación conceptual básica)", "Nivel Universitario (Estándar)", "Nivel Avanzado / Científico-Técnico"]
                )
                
                if st.button("Iniciar Clase Magistral", key="btn_explicar"):
                    if tema:
                        with st.spinner("⏳ Generando material didáctico estructurado..."):
                            try:
                                sys_prompt = engine.obtener_prompt_explicacion(nivel)
                                respuesta = engine.consultar_tutor(api_key, sys_prompt, f"Explícame: {tema}")
                                
                                st.write("---")
                                st.markdown("### Notas y Apuntes de la Lección:")
                                st.markdown(respuesta)
                            except Exception as e:
                                st.error(f"Error en el sistema de cátedra: {e}")
                    else:
                        st.warning("Por favor, introduce el tema académico que deseas revisar.")

        # ---------------------------------------------------------
        # PESTAÑA 2: TUTORÍA DE PROYECTOS (MODO SOCRÁTICO)
        # ---------------------------------------------------------
        with tab2:
            with st.container(border=True):
                st.markdown("### Consultoría Académica Socrática")
                st.write("Ingresa un problema complejo o línea de código. Tu asesor te guiará críticamente mediante pistas clave sin entregarte la solución directa.")
                
                problema = st.text_area("Enunciado del ejercicio matemático, algoritmo o bloque teórico:", height=130, placeholder="Copia aquí tu problema...")
                
                if st.button("Solicitar Pista Estratégica", key="btn_tarea"):
                    if problema:
                        with st.spinner("El consultor está desglosando los componentes del problema..."):
                            try:
                                sys_prompt = engine.obtener_prompt_socratico() 
                                respuesta = engine.consultar_tutor(api_key, sys_prompt, problema)
                                
                                st.write("---")
                                st.info("**Orientación y primer vector de resolución sugerido:**")
                                st.write(respuesta)
                            except Exception as e:
                                st.error(f"Error en el canal de asesoría: {e}")
                    else:
                        st.warning("Por favor, ingresa el problema que deseas desglosar.")

        # ---------------------------------------------------------
        # PESTAÑA 3: MÓDULO DE EVALUACIÓN
        # ---------------------------------------------------------
        with tab3:
            with st.container(border=True):
                st.markdown("### Centro de Evaluación y Diagnóstico")
                st.write("Pon a prueba tu retención de conocimientos generando exámenes de opción múltiple interactivos en tiempo real.")
                
                tema_quiz = st.text_input("Materia o unidad temática a evaluar:", placeholder="Ej. Programación Orientada a Objetos, Termodinámica...")

                if "quiz_datos" not in st.session_state: st.session_state.quiz_datos = None
                if "quiz_tema_actual" not in st.session_state: st.session_state.quiz_tema_actual = ""
                if "quiz_evaluado" not in st.session_state: st.session_state.quiz_evaluado = False

                if tema_quiz != st.session_state.quiz_tema_actual:
                    st.session_state.quiz_datos = None
                    st.session_state.quiz_evaluado = False

                if st.button("Diseñar Examen de Diagnóstico", key="btn_generar_quiz"):
                    if tema_quiz:
                        with st.spinner("El departamento de evaluación está estructurando los reactivos..."):
                            try:
                                sys_prompt = engine.obtener_prompt_quiz()
                                respuesta_raw = engine.consultar_tutor(api_key, sys_prompt, tema_quiz, json_mode=True)
                                st.session_state.quiz_datos = json.loads(respuesta_raw)
                                st.session_state.quiz_tema_actual = tema_quiz
                                st.session_state.quiz_evaluado = False
                            except Exception as e:
                                st.error(f"Error al compilar el examen: {e}")
                    else:
                        st.warning("Por favor, define la materia para el examen.")

                if st.session_state.quiz_datos and "preguntas" in st.session_state.quiz_datos:
                    st.write("---")
                    st.markdown(f"#### **Examen de Autoevaluación:** {st.session_state.quiz_tema_actual}")
                    
                    respuestas_alumno = {}
                    for idx, q in enumerate(st.session_state.quiz_datos["preguntas"]):
                        st.markdown(f"**Pregunta {idx+1}:** {q['pregunta']}")
                        respuestas_alumno[idx] = st.radio(
                            "Selecciona la opción correcta:", 
                            options=q["opciones"], 
                            key=f"pregunta_{idx}", 
                            index=None,
                            label_visibility="collapsed"
                        )
                        st.write("")

                    if st.button("Entregar Examen para Calificación", type="primary"):
                        if None in respuestas_alumno.values():
                            st.warning("No has respondido todos los reactivos del examen.")
                        else:
                            st.session_state.quiz_evaluado = True

                    if st.session_state.quiz_evaluado:
                        st.markdown("### Reporte Oficial de Rendimiento")
                        aciertos = 0
                        
                        for idx, q in enumerate(st.session_state.quiz_datos["preguntas"]):
                            alumno_ans = respuestas_alumno[idx]
                            correcta_ans = q["respuesta_correcta"]
                            
                            st.markdown(f"**Reactivo {idx+1}:** {q['pregunta']}")
                            st.write(f"Tu respuesta: *{alumno_ans}*")
                            
                            if alumno_ans.strip() == correcta_ans.strip():
                                st.success("¡Correcto!")
                                aciertos += 1
                            else:
                                st.error(f"Incorrecto. Opción esperada: **{correcta_ans}**")
                            st.caption(f"*Sustento Académico:* {q['justificacion']}")
                            st.write("---")
                        
                        score = (aciertos / len(st.session_state.quiz_datos["preguntas"])) * 100
                        st.metric(label="Calificación Final", value=f"{score:.0f}%", delta=f"{aciertos} de 3 aciertos")
                        if aciertos == 3:
                            st.balloons()
    else:
        st.info("Bienvenido a EstudIA. Para poder usar nuestra plataforma, por favor introduce la clave de acceso institucional (Groq API Key) en el panel izquierdo.")