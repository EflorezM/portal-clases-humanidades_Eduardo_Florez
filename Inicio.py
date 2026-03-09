import streamlit as st

# Fondo blanco limpio y layout centrado por defecto
st.set_page_config(page_title="Portal de Clases", page_icon="🏫", layout="centered")

# Título amigable con emojis
st.title("🏫 Bienvenido al Portal de Clases")
st.subheader("👨‍🏫 Profesor: Eduardo Florez Montero")

st.markdown("---")
st.write("¡Hola a todos! 👋 En este aplicativo encontrarán sus fichas de trabajo interactivas de Cívica, Religión y PFRH.")

st.info("🎯 **INSTRUCCIONES PARA LA CLASE DE HOY:**")

st.markdown("""
**Paso 1: Busca tu clase** 🔍
Abre el menú lateral izquierdo (si estás en tu celular, toca la pequeña flechita `>` arriba a la izquierda). Busca tu curso y selecciona la sesión que te indique el profesor.

**Paso 2: Resuelve la ficha** ✍️
Llena tus datos completos, selecciona tu **sección** correctamente y responde las preguntas de los niveles. ¡Anímate a hacer los retos!

**Paso 3: Descarga tu evidencia** 📥
Al terminar, haz clic en el botón verde **"Generar mi Evidencia en Word"** que está al final de la ficha. El archivo se guardará automáticamente en tu equipo.

**Paso 4: Entrega tu tarea en Google Classroom** 🚀
Ve a nuestro Google Classroom, busca la tarea del día y **adjunta el archivo Word** que acabas de descargar. ¡Y listo!
""")

st.markdown("---")
st.success("🌟 ¡Mucho éxito en tus actividades! Si tienes alguna duda durante la clase, levanta la mano o escribe en el chat.")
