import streamlit as st
from docx import Document
import io

st.set_page_config(page_title="Ficha PFRH - Emociones", page_icon="🧠", layout="centered")

st.markdown("### FICHA DE PFRH – SESIÓN 3° AÑO A - B - C")
st.markdown("**Tema:** Las emociones que experimentamos.")
st.markdown("**Prof:** Eduardo Florez Montero / Unidad 1")
st.markdown("---")

col1, col2, col3, col4 = st.columns([3, 1, 2, 2])
with col1: nombre = st.text_input("Estudiante:")
with col2: seccion = st.selectbox("Sección:", ["", "A", "B", "C"])
with col3: fecha = st.text_input("Fecha:")
with col4: st.info("Tiempo: 25min")

st.markdown("---")
with st.expander("🎯 META DE HOY", expanded=True): st.write("Reconocer emoción–pensamiento–situación y expresar emociones con respeto.")

st.markdown("---")
st.subheader("📚 Material de Apoyo")
try:
    with open("Presentacion_PFRH.pdf", "rb") as file:
        st.download_button("📄 Descargar Presentación de la Clase (PDF)", data=file, file_name="Presentacion_PFRH.pdf", mime="application/pdf")
except FileNotFoundError:
    st.info("📌 La presentación de la clase se está procesando y aparecerá aquí en breve.")

st.markdown("---")
st.subheader("NIVEL 1 (FÁCIL) – PARA TODOS")
q1 = st.selectbox("1) Marca tu emoción de hoy:", ["", "alegría", "enojo", "tristeza", "miedo", "vergüenza", "calma"])
q2 = st.text_input("2) Completa: Cuando siento enojo, mi cuerpo...")
q3 = st.text_area("3) Escribe 1 pensamiento que suele aparecer:")
q4 = st.text_area("4) Escribe 1 forma respetuosa de expresar esa emoción:")

st.markdown("---")
st.subheader("NIVEL 2 (MEDIO) – RETO 1")
st.write("5) Caso: Me dejan en visto en el chat.")
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1: q5_emo = st.text_input("Emoción:")
with col_c2: q5_pen = st.text_input("Pensamiento:")
with col_c3: q5_res = st.text_input("Respuesta:")

st.markdown("---")
st.subheader("NIVEL 3 (DIFÍCIL) – RETO 2")
q6 = st.text_area("6) Escribe 5 líneas: ¿qué pasa si guardo emociones y exploto en redes?")
q7_1 = st.text_input("7) Frase autocuidado:")

st.markdown("---")
if st.button("Generar mi Evidencia en Word"):
    if not nombre.strip() or seccion == "":
        st.error("⚠️ Por favor, ingresa tu nombre y selecciona tu sección.")
    elif q1 == "" or not q2.strip() or not q3.strip():
        st.error("⚠️ Debes completar el **NIVEL 1 (FÁCIL)**.")
    else:
        doc = Document()
        doc.add_heading('FICHA DE PFRH – SESIÓN 3° AÑO', level=1)
        doc.add_paragraph(f'Estudiante: {nombre} | Sección: {seccion} | Fecha: {fecha}')
        doc.add_paragraph('---')
        doc.add_heading('NIVEL 1', level=2)
        doc.add_paragraph(f'1) Emoción: {q1}\n2) Cuerpo: {q2}\n3) Pensamiento: {q3}\n4) Expresar: {q4}')
        doc.add_heading('NIVEL 2', level=2)
        doc.add_paragraph(f'5) En visto: Emo: {q5_emo} | Pen: {q5_pen} | Res: {q5_res}')
        doc.add_heading('NIVEL 3', level=2)
        doc.add_paragraph(f'6) Explotar redes: {q6}\n7) Autocuidado: {q7_1}')
        
        bio = io.BytesIO()
        doc.save(bio)
        st.success("¡Tu archivo está listo para entregar!")
        st.download_button("📥 Descargar .docx", data=bio.getvalue(), file_name=f"Ficha_PFRH_3{seccion}_{nombre.replace(' ', '_')}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
