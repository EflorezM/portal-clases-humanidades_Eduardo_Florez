import streamlit as st
from docx import Document
import io

st.set_page_config(page_title="Ficha Cívica - Salud Pública", page_icon="⚖️", layout="centered")

st.markdown("### FICHA DE CÍVICA – SESIÓN 2° AÑO A - B - C")
st.markdown("**Tema:** Derecho a la Vida y la Salud Pública")
st.markdown("**Prof:** Eduardo Florez Montero / Unidad 1")
st.markdown("---")

# DATOS DEL ESTUDIANTE (Con selector de sección)
col1, col2, col3, col4 = st.columns([3, 1, 2, 2])
with col1:
    nombre = st.text_input("Estudiante:")
with col2:
    seccion = st.selectbox("Sección:", ["", "A", "B", "C"])
with col3:
    fecha = st.text_input("Fecha:")
with col4:
    st.info("Tiempo: 30min")

st.markdown("---")

with st.expander("🎯 META DE HOY", expanded=True):
    st.write("Relacionar el derecho a la vida con la salud pública y proponer normas de prevención e información responsable.")

with st.expander("📋 INDICACIONES", expanded=True):
    st.write("1) Resuelve TODO el Nivel 1 (Fácil).\n2) Luego elige UN reto: Nivel 2 (Medio) o Nivel 3 (Difícil).\n3) Si falta tiempo, completa en casa.")

col_a, col_b = st.columns(2)
with col_a:
    st.success("**APOYOS (DUA)**\n- Ejemplos de prevención en pizarra.\n- Plantilla “medida–beneficio–responsabilidad”.")
with col_b:
    st.warning("**BANCO DE PALABRAS**\nsalud pública, prevención, higiene, vacuna, información, verificar")

st.markdown("---")

# MATERIAL DE APOYO
st.subheader("📚 Material de Apoyo")
st.write("Descarga la presentación de la clase para repasar los conceptos clave.")
try:
    with open("Presentacion_Civica.pdf", "rb") as file:
        st.download_button("📄 Descargar Presentación de la Clase (PDF)", data=file, file_name="Presentacion_Civica.pdf", mime="application/pdf")
except FileNotFoundError:
    st.info("📌 La presentación de la clase se está procesando y aparecerá aquí en breve.")

st.markdown("---")

st.markdown("### LECTURAS POR NIVELES (ELIGE UNA)")
tab1, tab2, tab3 = st.tabs(["Texto A (Fácil)", "Texto B (Medio)", "Texto C (Difícil)"])
with tab1: st.write("La salud pública cuida la vida de todas las personas. La prevención ayuda a evitar enfermedades.")
with tab2: st.write("Compartir información responsable en redes también protege la vida.")
with tab3: st.write("La desinformación en salud puede poner vidas en riesgo. Verificar fuentes es clave.")

st.markdown("---")

st.subheader("NIVEL 1 (FÁCIL) – PARA TODOS")
col_n1a, col_n1b = st.columns(2)
with col_n1a: q1_1 = st.text_input("1.1) Acción prevención 1:")
with col_n1b: q1_2 = st.text_input("1.2) Acción prevención 2:")
q2 = st.text_input("2) Difundir información falsa puede...")
q3 = st.radio("3) Antes de compartir una noticia debo:", ["verificar", "reenviar sin leer", "insultar"], horizontal=True)
q4 = st.text_input("4) 1 compromiso de salud en el aula:")

st.markdown("---")

st.subheader("NIVEL 2 (MEDIO) – RETO 1")
st.write("5) Caso: “Las vacunas hacen daño” (sin pruebas). 2 preguntas para verificar:")
q5_1 = st.text_input("Pregunta 1 para verificar:")
q5_2 = st.text_input("Pregunta 2 para verificar:")
st.write("6) 2 normas para compartir información de salud:")
q6_1 = st.text_input("Norma 1:")
q6_2 = st.text_input("Norma 2:")

st.markdown("---")

st.subheader("NIVEL 3 (DIFÍCIL) – RETO 2")
q7 = st.text_area("7) Mensaje de campaña (2 líneas):")
q8 = st.text_area("8) En 5 líneas: ¿por qué la información responsable protege la vida?")

st.markdown("---")
st.subheader("📊 Valoración de la Actividad")
val_funcional = st.slider("1. ¿Qué tan fácil te pareció usar esta ficha digital?", 1, 5, 5)
val_interes = st.radio("2. ¿El tema te pareció interesante?", ["Sí, mucho", "Estuvo bien", "No mucho"], horizontal=True)

st.markdown("---")

# VALIDACIÓN Y GENERACIÓN
if st.button("Generar mi Evidencia en Word"):
    if not nombre.strip() or seccion == "":
        st.error("⚠️ Por favor, ingresa tu nombre y selecciona tu sección antes de descargar.")
    elif not q1_1.strip() or not q1_2.strip() or not q2.strip() or not q4.strip():
        st.error("⚠️ Debes completar todas las preguntas del **NIVEL 1 (FÁCIL)**.")
    else:
        doc = Document()
        doc.add_heading('FICHA DE CÍVICA – SESIÓN 2° AÑO', level=1)
        doc.add_paragraph(f'Estudiante: {nombre} | Sección: {seccion} | Fecha: {fecha}')
        doc.add_paragraph('---')
        doc.add_heading('NIVEL 1 (FÁCIL)', level=2)
        doc.add_paragraph(f'1) Prevención: {q1_1}, {q1_2}\n2) Info falsa: {q2}\n3) Compartir: {q3}\n4) Compromiso: {q4}')
        doc.add_heading('NIVEL 2 (MEDIO)', level=2)
        doc.add_paragraph(f'5) Caso vacunas: {q5_1}, {q5_2}\n6) Normas: {q6_1}, {q6_2}')
        doc.add_heading('NIVEL 3 (DIFÍCIL)', level=2)
        doc.add_paragraph(f'7) Campaña: {q7}\n8) Info responsable: {q8}')
        doc.add_heading('Valoración', level=2)
        doc.add_paragraph(f'Funcionalidad: {val_funcional} | Interés: {val_interes}')
        
        bio = io.BytesIO()
        doc.save(bio)
        if q7.strip() and q8.strip(): st.balloons()
        st.success("¡Tu archivo está listo para entregar!")
        st.download_button("📥 Descargar .docx", data=bio.getvalue(), file_name=f"Ficha_Civica_2{seccion}_{nombre.replace(' ', '_')}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
