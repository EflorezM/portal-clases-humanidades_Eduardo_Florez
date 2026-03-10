import streamlit as st
import time
from docx import Document
import io

st.set_page_config(page_title="Ficha de Religión - El judaísmo", page_icon="📜", layout="centered")

# --- SISTEMA DE TIEMPO INTELIGENTE ---
if 'inicio_tiempo_religion' not in st.session_state:
    st.session_state.inicio_tiempo_religion = time.time()
    st.session_state.minutos_asignados_religion = 20

segundos_transcurridos = time.time() - st.session_state.inicio_tiempo_religion
segundos_restantes = (st.session_state.minutos_asignados_religion * 60) - segundos_transcurridos
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
            st.session_state.minutos_asignados_religion += 4
            st.rerun()
        
        st.caption("Actualiza la página (F5) o interactúa con la ficha para ver el tiempo exacto.")
    else:
        st.error("## 00:00")
        st.error("⚠️ TIEMPO AGOTADO")
        st.write("Tu ficha ha sido bloqueada. Por favor, descarga tu avance en la parte inferior.")
        
        if st.button("🔓 Desbloquear (Dar 4 min)"):
            st.session_state.minutos_asignados_religion += 4
            st.rerun()
# --------------------------------------

st.markdown("### FICHA DE RELIGIÓN – SESIÓN 1° AÑO A - B - C")
st.markdown("**Tema:** El judaísmo: Cuna de las religiones monoteístas.")
st.markdown("**Prof:** Eduardo Florez Montero / Unidad 1")
st.markdown("---")

col1, col2, col3 = st.columns([3, 1, 2])
with col1: nombre = st.text_input("Estudiante:", disabled=bloquear_inputs)
with col2: seccion = st.selectbox("Sección:", ["", "A", "B", "C"], disabled=bloquear_inputs)
with col3: fecha = st.text_input("Fecha:", disabled=bloquear_inputs)

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
st.write("¡Comencemos recordando los conceptos clave de la clase de hoy!")
q1 = st.text_input("1) Piensa en la palabra 'monoteísmo'. Según lo que vimos, ¿qué significa exactamente creer en esto?", disabled=bloquear_inputs)
q2 = st.radio("2) Selecciona la opción correcta: La figura histórica de Abraham es importante para...", ["judaísmo", "cristianismo", "ambos"], horizontal=True, disabled=bloquear_inputs)

st.write("3) Abraham demostró muchas cualidades. Menciona 2 valores importantes que podemos aprender de su historia:")
col_v1, col_v2 = st.columns(2)
with col_v1: q3_1 = st.text_input("Valor 1:", disabled=bloquear_inputs)
with col_v2: q3_2 = st.text_input("Valor 2:", disabled=bloquear_inputs)

q4 = st.text_input("4) Escribe una regla de oro que debes usar siempre para dialogar con respeto sobre las creencias de otras personas:", disabled=bloquear_inputs)

st.markdown("---")
st.subheader("NIVEL 2 (MEDIO) – RETO 1")
st.info("💡 **Reto 1:** Piensa en lo que hemos aprendido en clase. ¿En qué se parecen el judaísmo y el cristianismo? Escribe dos características que ambas religiones compartan (semejanzas):")
col_s1, col_s2 = st.columns(2)
with col_s1: q5_1 = st.text_input("Primera semejanza:", disabled=bloquear_inputs)
with col_s2: q5_2 = st.text_input("Segunda semejanza:", disabled=bloquear_inputs)

q6 = st.text_input("6) Para mantener una buena convivencia, escribe un prejuicio o idea equivocada sobre otras religiones que debemos evitar en el salón de clases:", disabled=bloquear_inputs)

st.markdown("---")
st.subheader("NIVEL 3 (DIFÍCIL) – RETO 2")
q7 = st.text_area("7) Reflexiona a profundidad (aprox. 5 líneas): ¿Por qué crees que el respeto hacia otras creencias es una parte fundamental de los valores cristianos?", disabled=bloquear_inputs)

st.write("8) Propón 3 acciones prácticas que podrías hacer en tu día a día para mejorar la convivencia con personas que tienen creencias diferentes a las tuyas:")
q8_1 = st.text_input("Acción 1:", disabled=bloquear_inputs)
q8_2 = st.text_input("Acción 2:", disabled=bloquear_inputs)
q8_3 = st.text_input("Acción 3:", disabled=bloquear_inputs)

st.markdown("---")
if st.button("Generar mi Evidencia en Word"):
    if not nombre.strip() or seccion == "":
        st.error("⚠️ Por favor, ingresa tu nombre y selecciona tu sección para poder identificarte.")
        
    elif not tiempo_agotado and (
        not q1.strip() or not q3_1.strip() or not q3_2.strip() or not q4.strip() or
        not q5_1.strip() or not q5_2.strip() or not q6.strip() or
        not q7.strip() or not q8_1.strip() or not q8_2.strip() or not q8_3.strip()
    ):
        st.error("⚠️ Aún tienes tiempo. Debes completar las preguntas de **TODOS LOS NIVELES (1, 2 y 3)** antes de descargar tu evidencia.")
        
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
        doc.add_paragraph(f'7) Respeto: {q7}\n8) Acciones: 1) {q8_1} | 2) {q8_2} | 3) {q8_3}')

        if tiempo_agotado: doc.add_paragraph('\n[Entregado al finalizar el tiempo reglamentario]')

        bio = io.BytesIO()
        doc.save(bio)

        if not tiempo_agotado: st.balloons()

        st.success("¡Tu archivo está listo para entregar!")
        st.download_button("📥 Descargar .docx", data=bio.getvalue(), file_name=f"Ficha_Religion_1{seccion}_{nombre.replace(' ', '_')}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
