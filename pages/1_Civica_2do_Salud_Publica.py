import streamlit as st
import time
from docx import Document
import io

st.set_page_config(page_title="Ficha Cívica - Salud Pública", page_icon="⚖️", layout="centered")

# --- SISTEMA DE TIEMPO INTELIGENTE ---
# 1. Iniciar el cronómetro en la memoria de la sesión (20 minutos)
if 'inicio_tiempo' not in st.session_state:
    st.session_state.inicio_tiempo = time.time()
    st.session_state.minutos_asignados = 20

# 2. Calcular cuánto tiempo ha pasado
segundos_transcurridos = time.time() - st.session_state.inicio_tiempo
segundos_restantes = (st.session_state.minutos_asignados * 60) - segundos_transcurridos

# 3. Determinar si el tiempo se acabó (bloqueo)
tiempo_agotado = segundos_restantes <= 0
bloquear_inputs = tiempo_agotado 

# --- MENÚ LATERAL: RELOJ Y TIEMPO EXTRA ---
with st.sidebar:
    st.markdown("### ⏱️ Cronómetro de Clase")
    if not tiempo_agotado:
        minutos = int(segundos_restantes // 60)
        segundos = int(segundos_restantes % 60)
        st.success(f"## {minutos:02d}:{segundos:02d}")
        
        # Botón para añadir tiempo
        if st.button("➕ Dar 4 min extra"):
            st.session_state.minutos_asignados += 4
            st.rerun()
        
        st.caption("Actualiza la página (F5) o interactúa con la ficha para ver el tiempo exacto.")
    else:
        st.error("## 00:00")
        st.error("⚠️ TIEMPO AGOTADO")
        st.write("Tu ficha ha sido bloqueada. Por favor, descarga tu avance en la parte inferior.")
        
        # Opción para que el profesor desbloquee si es necesario
        if st.button("🔓 Desbloquear (Dar 4 min)"):
            st.session_state.minutos_asignados += 4
            st.rerun()
# --------------------------------------

st.markdown("### FICHA DE CÍVICA – SESIÓN 2° AÑO A - B - C")
st.markdown("**Tema:** Derecho a la Vida y la Salud Pública")
st.markdown("**Prof:** Eduardo Florez Montero / Unidad 1")
st.markdown("---")

# DATOS DEL ESTUDIANTE (Se bloquean si el tiempo se acaba)
col1, col2, col3 = st.columns([3, 1, 2])
with col1: nombre = st.text_input("Estudiante:", disabled=bloquear_inputs)
with col2: seccion = st.selectbox("Sección:", ["", "A", "B", "C"], disabled=bloquear_inputs)
with col3: fecha = st.text_input("Fecha:", disabled=bloquear_inputs)

st.markdown("---")
with st.expander("🎯 META DE HOY", expanded=True): st.write("Relacionar el derecho a la vida con la salud pública y proponer normas de prevención e información responsable.")

st.markdown("---")
st.subheader("NIVEL 1 (FÁCIL) – PARA TODOS")
col_n1a, col_n1b = st.columns(2)
with col_n1a: q1_1 = st.text_input("1.1) Acción prevención 1:", disabled=bloquear_inputs)
with col_n1b: q1_2 = st.text_input("1.2) Acción prevención 2:", disabled=bloquear_inputs)
q2 = st.text_input("2) Difundir información falsa puede...", disabled=bloquear_inputs)
q3 = st.radio("3) Antes de compartir una noticia debo:", ["verificar", "reenviar sin leer", "insultar"], horizontal=True, disabled=bloquear_inputs)
q4 = st.text_input("4) 1 compromiso de salud en el aula:", disabled=bloquear_inputs)

st.markdown("---")
st.subheader("NIVEL 2 (MEDIO) – RETO 1")
q5_1 = st.text_input("5.1) Pregunta 1 para verificar caso vacunas:", disabled=bloquear_inputs)
q5_2 = st.text_input("5.2) Pregunta 2 para verificar caso vacunas:", disabled=bloquear_inputs)
q6_1 = st.text_input("6.1) Norma 1 información salud:", disabled=bloquear_inputs)

st.markdown("---")
st.subheader("NIVEL 3 (DIFÍCIL) – RETO 2")
q7 = st.text_area("7) Mensaje de campaña (2 líneas):", disabled=bloquear_inputs)
q8 = st.text_area("8) En 5 líneas: ¿por qué la información responsable protege la vida?", disabled=bloquear_inputs)

st.markdown("---")

# --- LÓGICA CONDICIONAL DE DESCARGA (OBLIGATORIO 3 NIVELES) ---
if st.button("Generar mi Evidencia en Word"):
    if not nombre.strip() or seccion == "":
        st.error("⚠️ Por favor, ingresa tu nombre y selecciona tu sección para poder identificarte.")
    
    # CASO 1: Aún hay tiempo. Se exige TODO (Nivel 1, 2 y 3).
    elif not tiempo_agotado and (
        not q1_1.strip() or not q1_2.strip() or not q2.strip() or not q4.strip() or 
        not q5_1.strip() or not q5_2.strip() or not q6_1.strip() or 
        not q7.strip() or not q8.strip()
    ):
        st.error("⚠️ Aún tienes tiempo. Debes completar las preguntas de **TODOS LOS NIVELES (1, 2 y 3)** antes de descargar tu evidencia.")
        
    # CASO 2: El tiempo se acabó (o llenaron todo). Se descarga el archivo.
    else:
        doc = Document()
        doc.add_heading('FICHA DE CÍVICA – SESIÓN 2° AÑO', level=1)
        doc.add_paragraph(f'Estudiante: {nombre} | Sección: {seccion} | Fecha: {fecha}')
        doc.add_paragraph('---')
        doc.add_heading('NIVEL 1', level=2)
        doc.add_paragraph(f'1) Prevención: {q1_1}, {q1_2}\n2) Info falsa: {q2}\n3) Compartir: {q3}\n4) Compromiso: {q4}')
        doc.add_heading('NIVEL 2', level=2)
        doc.add_paragraph(f'5) Caso vacunas: {q5_1}, {q5_2}\n6) Normas: {q6_1}')
        doc.add_heading('NIVEL 3', level=2)
        doc.add_paragraph(f'7) Campaña: {q7}\n8) Info responsable: {q8}')
        
        # Sello de tiempo agotado en el Word si fue entregado incompleto
        if tiempo_agotado:
            doc.add_paragraph('\n[Entregado al finalizar el tiempo reglamentario]')
            
        bio = io.BytesIO()
        doc.save(bio)
        
        if not tiempo_agotado:
            st.balloons()
            
        st.success("¡Tu archivo está listo para entregar!")
        st.download_button("📥 Descargar .docx", data=bio.getvalue(), file_name=f"Ficha_Civica_2{seccion}_{nombre.replace(' ', '_')}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
