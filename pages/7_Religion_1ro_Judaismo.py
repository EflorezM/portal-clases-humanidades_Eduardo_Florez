import streamlit as st
from docx import Document
import io

st.set_page_config(page_title="Ficha de Religión - El judaísmo", page_icon="📜", layout="centered")

st.markdown("### FICHA DE RELIGIÓN – SESIÓN 1° AÑO A - B - C")
st.markdown("**Tema:** El judaísmo: Cuna de las religiones monoteístas.")
st.markdown("**Prof:** Eduardo Florez Montero / Unidad 1")
st.markdown("---")

col1, col2, col3, col4 = st.columns([3, 1, 2, 2])
with col1: nombre = st.text_input("Estudiante:")
with col2: seccion = st.selectbox("Sección:", ["", "A", "B", "C"])
with col3: fecha = st.text_input("Fecha:")
with col4: st.info("Tiempo: 30min")

st.markdown("---")
with st.expander("🎯 META DE HOY", expanded=True): st.write("Reconocer aportes del judaísmo y practicar diálogo respetuoso sin prejuicios.")

st.markdown("---")
st.subheader("📚 Material de Apoyo")
try:
    with open("Presentacion_Religion.pdf", "rb") as file:
        st.download_button("📄 Descargar Presentación de la Clase (PDF)", data=file, file_name="Presentacion_Religion.pdf", mime="application/pdf")
except FileNotFoundError:
    st.info("📌 La presentación de la clase se está procesando y aparecerá aquí en breve.")

st.markdown("---")
st.subheader("NIVEL 1 (FÁCIL) – PARA TODOS")
q1 = st.text_input("1) Monoteísmo significa creer en:")
q2 = st.radio("2) Abraham es importante para:", ["judaísmo", "cristianismo", "ambos"], horizontal=True)
col_v1, col_v2 = st.columns(2)
with col_v1: q3_1 = st.text_input("3.1) Valor 1 Abraham:")
with col_v2: q3_2 = st.text_input("3.2) Valor 2 Abraham:")
q4 = st.text_input("4) 1 regla para dialogar con respeto:")

st.markdown("---")
st.subheader("NIVEL 2 (MEDIO) – RETO 1")
st.info("💡 **Reto 1:** Piensa en lo que hemos aprendido en clase. ¿En qué se parecen el judaísmo y el cristianismo? Escribe dos características que ambas religiones compartan (semejanzas).")
col_s1, col_s2 = st.columns(2)
with col_s1: q5_1 = st.text_input("5.1) Primera semejanza:")
with col_s2: q5_2 = st.text_input("5.2) Segunda semejanza:")
q6 = st.text_input("6) 1 prejuicio que debo evitar:")

st.markdown("---")
st.subheader("NIVEL 3 (DIFÍCIL) – RETO 2")
q7 = st.text_area("7) En 5 líneas: ¿por qué el respeto es parte de valores cristianos?")
q8_1 = st.text_input("8) Acción convivencia:")

st.markdown("---")
if st.button("Generar mi Evidencia en Word"):
    if not nombre.strip() or seccion == "":
        st.error("⚠️ Por favor, ingresa tu nombre y selecciona tu sección.")
    elif not q1.strip() or not q3_1.strip() or not q4.strip():
        st.error("⚠️ Debes completar el **NIVEL 1 (FÁCIL)**.")
    else:
        doc = Document()
        doc.add_heading('FICHA DE RELIGIÓN – SESIÓN 1° AÑO', level=1)
        doc.add_paragraph(f'Estudiante: {nombre} | Sección: {seccion} | Fecha: {fecha}')
        doc.add_paragraph('---')
        doc.add_heading('NIVEL 1', level=2)
        doc.add_paragraph(f'1) Monoteísmo: {q1}\n2) Abraham: {q2}\n3) Valores: {q3_1}, {q3_2}\n4) Regla: {q4}')
        doc.add_heading('NIVEL 2', level=2)
        doc.add_paragraph(f'5) Semejanzas: {q5_1}, {q5_2}\n6) Prejuicio: {q6}')
        doc.add_heading('NIVEL 3', level=2)
        doc.add_paragraph(f'7) Respeto: {q7}\n8) Acción: {q8_1}')
        
        bio = io.BytesIO()
        doc.save(bio)
        st.success("¡Tu archivo está listo para entregar!")
        st.download_button("📥 Descargar .docx", data=bio.getvalue(), file_name=f"Ficha_Religion_1{seccion}_{nombre.replace(' ', '_')}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
