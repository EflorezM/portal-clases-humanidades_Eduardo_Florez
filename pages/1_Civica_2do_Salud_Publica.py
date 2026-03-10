import streamlit as st
import time
from docx import Document
import io

st.set_page_config(page_title="Ficha Cívica - Salud Pública", page_icon="⚖️", layout="centered")

# --- SISTEMA DE TIEMPO INTELIGENTE ---
if 'inicio_tiempo_civica' not in st.session_state:
    st.session_state.inicio_tiempo_civica = time.time()
    st.session_state.minutos_asignados_civica = 20

segundos_transcurridos = time.time() - st.session_state.inicio_tiempo_civica
segundos_restantes = (st.session_state.minutos_asignados_civica * 60) - segundos_transcurridos
tiempo_agotado = segundos_restantes <= 0
bloquear_inputs = tiempo_agotado 

# --- MENÚ LATERAL: RELOJ Y TIEMPO EXTRA ---
with st.sidebar:
    st.markdown("### ⏱️ Cronómetro de ficha")
    if not tiempo_agotado:
        minutos = int(segundos_restantes // 60)
        segundos = int(segundos_restantes % 60)
        st.success(f"## {minutos:02d}:{segundos:02d}")
        
        if st.button("➕ Dar 4 min extra"):
            st.session_state.minutos_asignados_civica += 4
            st.rerun()
        
        st.caption("Actualiza la página (F5) o interactúa con la ficha para ver el tiempo exacto.")
    else:
        st.error("## 00:00")
        st.error("⚠️ TIEMPO AGOTADO")
        st.write("Tu ficha ha sido bloqueada. Por favor, descarga tu avance en la parte inferior.")
        
        if st.button("🔓 Desbloquear (Dar 4 min)"):
            st.session_state.minutos_asignados_civica += 4
            st.rerun()
# --------------------------------------

st.markdown("### FICHA DE CÍVICA – SESIÓN 2° AÑO A - B - C")
st.markdown("**Tema:** Derecho a la Vida y la Salud Pública")
st.markdown("**Prof:** Eduardo Florez Montero / Unidad 1")
st.markdown("---")

col1, col2, col3 = st.columns([3, 1, 2])
with col1: nombre = st.text_input("Estudiante:", disabled=bloquear_inputs)
with col2: seccion = st.selectbox("Sección:", ["", "A", "B", "C"], disabled=bloquear_inputs)
with col3: fecha = st.text_input("Fecha:", disabled=bloquear_inputs)

st.markdown("---")
with st.expander("🎯 META DE HOY", expanded=True): st.write("Relacionar el derecho a la vida con la salud pública y proponer normas de prevención e información responsable.")

st.markdown("---")
st.subheader("📚 Material de Apoyo")
try:
    with open("Presentacion_Civica.pdf", "rb") as file:
        st.download_button("📄 Descargar Presentación de la Clase (PDF)", data=file, file_name="Presentacion_Civica.pdf", mime="application/pdf")
except FileNotFoundError:
    st.info("📌 La presentación de la clase se está procesando y aparecerá aquí en breve.")

st.markdown("---")
st.subheader("NIVEL 1 (FÁCIL) – PARA TODOS")
st.write("Empecemos identificando acciones cotidianas que protegen nuestra comunidad.")
col_n1a, col_n1b = st.columns(2)
with col_n1a: q1_1 = st.text_input("1.1) Menciona una primera acción concreta de prevención:", disabled=bloquear_inputs)
with col_n1b: q1_2 = st.text_input("1.2) Menciona una segunda acción de prevención:", disabled=bloquear_inputs)

q2 = st.text_input("2) Completa la frase: Si una persona difunde información falsa sobre temas de salud, esto puede ocasionar que...", disabled=bloquear_inputs)
q3 = st.radio("3) Marca la opción correcta. Antes de compartir una noticia sobre salud en mis redes sociales, lo primero que debo hacer es:", ["verificar si la fuente es confiable", "reenviar rápidamente sin leer", "insultar a quien lo publicó"], horizontal=True, disabled=bloquear_inputs)
q4 = st.text_input("4) Escribe un compromiso personal que puedas aplicar dentro del aula para mantener una buena salud grupal:", disabled=bloquear_inputs)

st.markdown("---")
st.subheader("NIVEL 2 (MEDIO) – RETO 1")
st.write("5) Lee el siguiente caso: Ves una publicación en redes que dice 'Las vacunas hacen daño' pero no muestra ninguna fuente científica ni prueba. Escribe dos preguntas críticas que te harías para verificar si esa información es falsa:")
q5_1 = st.text_input("Pregunta crítica 1:", disabled=bloquear_inputs)
q5_2 = st.text_input("Pregunta crítica 2:", disabled=bloquear_inputs)

st.write("6) Escribe dos normas o reglas de oro que todos deberíamos seguir antes de compartir información de salud en internet:")
q6_1 = st.text_input("Regla de oro 1:", disabled=bloquear_inputs)
q6_2 = st.text_input("Regla de oro 2:", disabled=bloquear_inputs)

st.markdown("---")
st.subheader("NIVEL 3 (DIFÍCIL) – RETO 2")
st.write("7) Imagina que eres el líder de una campaña de salud escolar. Crea un mensaje corto y llamativo (máximo 2 líneas) para animar a tus compañeros a prevenir enfermedades:")
q7 = text_area_1 = st.text_area("Mensaje de campaña:", disabled=bloquear_inputs)

st.write("8) Redacta un párrafo corto (aprox. 5 líneas) explicando con tus propias palabras: ¿Por qué crees que informarnos responsablemente es una forma de proteger nuestra vida y la de los demás?")
q8 = st.text_area("Tu reflexión:", disabled=bloquear_inputs)

st.markdown("---")

if st.button("Generar mi Evidencia en Word"):
    if not nombre.strip() or seccion == "":
        st.error("⚠️ Por favor, ingresa tu nombre y selecciona tu sección para poder identificarte.")
    
    # Exige Nivel 1, 2 y 3 si hay tiempo
    elif not tiempo_agotado and (
        not q1_1.strip() or not q1_2.strip() or not q2.strip() or not q4.strip() or 
        not q5_1.strip() or not q5_2.strip() or not q6_1.strip() or not q6_2.strip() or
        not q7.strip() or not q8.strip()
    ):
        st.error("⚠️ Aún tienes tiempo. Debes completar las preguntas de **TODOS LOS NIVELES (1, 2 y 3)** antes de descargar tu evidencia.")
        
    else:
        doc = Document()
        doc.add_heading('FICHA DE CÍVICA – SESIÓN 2° AÑO', level=1)
        doc.add_paragraph(f'Estudiante: {nombre} | Sección: {seccion} | Fecha: {fecha}')
        doc.add_paragraph('---')
        doc.add_heading('NIVEL 1', level=2)
        doc.add_paragraph(f'1) Prevención: {q1_1}, {q1_2}\n2) Info falsa: {q2}\n3) Compartir: {q3}\n4) Compromiso: {q4}')
        doc.add_heading('NIVEL 2', level=2)
        doc.add_paragraph(f'5) Caso vacunas: {q5_1}, {q5_2}\n6) Normas: {q6_1}, {q6_2}')
        doc.add_heading('NIVEL 3', level=2)
        doc.add_paragraph(f'7) Campaña: {q7}\n8) Info responsable: {q8}')
        
        if tiempo_agotado: doc.add_paragraph('\n[Entregado al finalizar el tiempo reglamentario]')
            
        bio = io.BytesIO()
        doc.save(bio)
        
        if not tiempo_agotado: st.balloons()
            
        st.success("¡Tu archivo está listo para entregar!")
        st.download_button("📥 Descargar .docx", data=bio.getvalue(), file_name=f"Ficha_Civica_2{seccion}_{nombre.replace(' ', '_')}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
