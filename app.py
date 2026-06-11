
import streamlit as st

# Configuración básica
st.set_page_config(page_title="Para Aleshita", layout="centered")

# Ocultar menús y footer de Streamlit
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Inicializar estados
if 'nivel' not in st.session_state:
    st.session_state.nivel = -1

# --- NIVEL -1: Acceso Restringido ---
if st.session_state.nivel == -1:
    st.title("🔐 Acceso Restringido")
    palabra = st.text_input("Ingresa la palabra secreta:").lower().strip()
    
    if palabra == "Soy Alessia y me gusta la Pinga":
        st.success("Muy bien Cachorrita.")
        if st.button("Jugar"):
            st.session_state.nivel = 0
            st.rerun()
    elif palabra != "":
        st.error("Rompe Mrda, escribe la palabra correcta!.")

# --- NIVEL 0: Inicio ---
elif st.session_state.nivel == 0:
    st.title(".Responde Bien LINDURA... 🤫")
    if st.button("Comenzar a Kchar,,, digo Jugar😏"):
        st.session_state.nivel = 1
        st.rerun()

# --- NIVEL 1: El Bosque ---
elif st.session_state.nivel == 1:
    audio_bytes = open("suspenso.mp3", "rb").read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True, loop=True)
    
    st.markdown("### Nivel 1: El inicio de una linda amistad 🥰")
    st.write("Hubo una vez, donde dos personas sin buscarse se encontraron y demostraron que funcionaron sin amarse. ¿En q año nos conocimos?")
    
    if st.button("2024"):
        st.error("Dejas mal Mrda, pero si fuera tu ex, altoke no Kcheraaa 🙄")
    if st.button("2025"):
        st.session_state.nivel = 2
        st.rerun()

# --- NIVEL 2: La Puerta de Piedra ---
elif st.session_state.nivel == 2:
    st.markdown("### Nivel 2: La Puerta de Piedra 🪨")
    r1 = st.text_input("Contraseña:").lower().strip()
    if r1 == "respuesta1": # EDITA TU RESPUESTA AQUÍ
        st.success("¡La puerta se abre!")
        if st.button("Continuar"):
            st.session_state.nivel = 3
            st.rerun()
    elif r1 != "":
        st.warning("Intenta de nuevo.")

# --- NIVEL 3: Bóveda Final ---
elif st.session_state.nivel == 3:
    st.markdown("### Nivel 3: La Bóveda 🔐")
    r2 = st.text_input("Última contraseña:").lower().strip()
    if r2 == "respuesta2": # EDITA TU RESPUESTA AQUÍ
        st.session_state.nivel = 4
        st.rerun()
    elif r2 != "":
        st.warning("Contraseña incorrecta.")

# --- NIVEL 4: GIF Final ---
elif st.session_state.nivel == 4:
    st.balloons()
    st.title("¡Lo lograste! 🎉")
    st.write("Gracias por jugar.")
    
    # Mostrar el GIF subido al repo
    st.image("kitty.gif")
    
    if st.button("Reiniciar"):
        st.session_state.nivel = -1
        st.rerun()
        




























































