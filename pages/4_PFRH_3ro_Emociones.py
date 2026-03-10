import streamlit as st
import time
from docx import Document
import io

st.set_page_config(page_title="Ficha PFRH - Emociones", page_icon="🧠", layout="centered")

# --- SISTEMA DE TIEMPO INTELIGENTE Y BOTÓN GO ---
if 'ficha_iniciada_pfrh' not in st.session_state:
    st.session_state.ficha_iniciada_pfrh = False

if not st.session_state.ficha_iniciada_pfrh:
    st.info("👋 ¡Hola! Tienes 20 minutos para resolver esta ficha. El tiempo comenzará a correr cuando presiones el botón de abajo.")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("🚀 ESTOY LISTO: INICIAR FICHA (GO)", use_container_width=True):
            st.session_state.ficha_iniciada_pfrh = True
            st.session_state.inicio_tiempo_pfrh = time.time()
            st.session_state.minutos_asignados_pfrh = 20
            st.rerun()
    st.stop()

segundos_transcurridos = time.time() - st.session_state.inicio_tiempo_pfrh
segundos_restantes = (st.session_state.minutos_asignados_pfrh * 60) - segundos_transcurridos
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
            st.session_state.minutos_asignados_pfrh += 4
            st.rerun()
        
        st.caption("Actualiza la página (F5) o interactúa con la ficha para ver el tiempo exacto.")
    else:
        st.error("## 00:00")
        st.error("⚠️ TIEMPO AGOTADO")
        st.write("Tu ficha ha sido bloqueada. Por favor, descarga tu avance en la parte inferior.")
        
        if st.button("🔓 Desbloquear (Dar 4 min extra)"):
            st.session_state.minutos_asignados_pfrh += 4
            st.rerun()
# --------------------------------------

st.markdown("### FICHA DE PFRH – SESIÓN 3° AÑO A - B - C")
st.markdown("**Tema:** Las emociones que experimentamos.")
st.markdown("**Prof:** Eduardo Florez Montero / Unidad 1")
st.markdown("---")

col1, col2, col3 = st.columns([3, 1, 2])
with col1: nombre = st.text_input("Estudiante:", disabled=bloquear_inputs)
with col2: seccion = st.selectbox("Sección:", ["", "A", "B", "C"], disabled=bloquear_inputs)
with col3: fecha = st.text_input("Fecha:", disabled=bloquear_inputs)

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
q1 = st.selectbox("1) Haz una pausa y reflexiona: ¿Cuál de estas emociones describe mejor cómo te sientes el día de hoy?", ["", "alegría", "enojo", "tristeza", "miedo", "vergüenza", "calma"], disabled=bloquear_inputs)
q2 = st.text_input("2) Observa tus reacciones físicas. Completa la frase: Cuando siento enojo o frustración, noto que mi cuerpo...", disabled=bloquear_inputs)
q3 = st.text_area("3) Identifica el pensamiento: Escribe un pensamiento frecuente que suele aparecer en tu mente cuando experimentas enojo (recuerda no usar nombres reales de otras personas):", disabled=bloquear_inputs)
q4 = st.text_area("4) Busca una salida sana: Escribe una forma respetuosa y asertiva en la que podrías expresar o canalizar esa emoción sin lastimar a nadie:", disabled=bloquear_inputs)

st.markdown("---")
st.subheader("NIVEL 2 (MEDIO) – RETO 1")
st.write("5) Analiza el siguiente caso: Le escribes un mensaje importante a un amigo y te deja 'en visto' sin responder. Completa los espacios identificando qué emoción sentirías, qué pensarías y cuál sería tu respuesta:")
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1: q5_emo = st.text_input("¿Qué emoción sentirías?:", disabled=bloquear_inputs)
with col_c2: q5_pen = st.text_input("¿Qué pensamiento cruzaría tu mente?:", disabled=bloquear_inputs)
with col_c3: q5_res = st.text_input("¿Cuál sería una respuesta respetuosa?:", disabled=bloquear_inputs)

st.markdown("---")
st.subheader("NIVEL 3 (DIFÍCIL) – RETO 2")
q6 = st.text_area("6) Reflexiona profundo (5 líneas): ¿Cuáles crees que son las consecuencias emocionales y sociales si te guardas todo lo que sientes y terminas 'explotando' impulsivamente en tus redes sociales?", disabled=bloquear_inputs)
st.write("7) Crea dos frases cortas y positivas de 'autocuidado' emocional que podrías repetirte a ti mismo/a en momentos de mucho estrés o tristeza:")
q7_1 = st.text_input("Frase de autocuidado 1:", disabled=bloquear_inputs)
q7_2 = st.text_input("Frase de autocuidado 2:", disabled=bloquear_inputs)

st.markdown("---")

if st.button("Generar mi Evidencia en Word"):
    if not nombre.strip() or seccion == "":
        st.error("⚠️ Por favor, ingresa tu nombre y selecciona tu sección para poder identificarte.")
        
    elif not tiempo_agotado and (
        q1 == "" or not q2.strip() or not q3.strip() or not q4.strip() or
        not q5_emo.strip() or not q5_pen.strip() or not q5_res.strip() or
        not q6.strip() or not q7_1.strip() or not q7_2.strip()
    ):
        st.error("⚠️ Aún tienes tiempo. Debes completar las preguntas de **TODOS LOS NIVELES (1, 2 y 3)** antes de descargar tu evidencia.")
        
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
        doc.add_paragraph(f'6) Explotar redes: {q6}\n7) Autocuidado: 1) {q7_1} | 2) {q7_2}')
        
        if tiempo_agotado: doc.add_paragraph('\n[Entregado al finalizar el tiempo reglamentario]')
        
        bio = io.BytesIO()
        doc.save(bio)
        
        if not tiempo_agotado: st.balloons()
            
        st.success("¡Tu archivo está listo para entregar!")
        st.download_button("📥 Descargar .docx", data=bio.getvalue(), file_name=f"Ficha_PFRH_3{seccion}_{nombre.replace(' ', '_')}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
