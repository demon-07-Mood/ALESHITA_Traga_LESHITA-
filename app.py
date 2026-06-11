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

# --- 1. LOGICA DE AUDIO (Solo se ejecuta una vez) ---
if 'audio_iniciado' not in st.session_state:
    st.session_state.audio_iniciado = False

# La música NO se toca si ya está iniciada
if st.session_state.audio_iniciado:
    audio_bytes = open("suspenso.mp3", "rb").read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True, loop=True)

# Inicializar niveles
if 'nivel' not in st.session_state:
    st.session_state.nivel = -1

# --- NIVEL -1: Acceso Restringido ---
if st.session_state.nivel == -1:
    st.title("🔐 Acceso Restringido")
    palabra = st.text_input("Ingresa la palabra secreta:").lower().strip()
    
    if palabra == "alessia_kachera":
        st.success("Muy bien Cachorrita.")
        if st.button("Jugar"):
            st.session_state.audio_iniciado = True # Activa la música al entrar
            st.session_state.nivel = 0
            st.rerun()
    elif palabra != "":
        st.error("Rompe Mrda, escribe la palabra correcta!.")

# --- NIVEL 0: Inicio ---
elif st.session_state.nivel == 0:
    st.title("Responde Bien LINDURA... 🤫")
    if st.button("Comenzar a Kchar,,, digo Jugar😏"):
        st.session_state.nivel = 1
        st.rerun()

# --- NIVEL 1: El Bosque ---
elif st.session_state.nivel == 1:
    st.markdown("### Nivel 1: El inicio de una linda amistad 🥰")
    st.write("Hubo una vez, donde dos personas sin buscarse se encontraron y demostraron que funcionaron sin amarse. ¿En q año nos conocimos?")
    
    if st.button("2024"):
        st.error("Dejas mal Mrda, pero si fuera tu ex, altoke no Kcheraaa 🙄")
    if st.button("2025"):
        st.session_state.nivel = 2
        st.rerun()

# --- NIVEL 2: La Puerta de Piedra ---
elif st.session_state.nivel == 2:
    st.markdown("### Nivel 2: Muestra de Cariño 🥰")
    st.write("¿Cual es el apodo que me pusiste, o bueno con q nombre me llamas?")
    r1 = st.text_input("Contraseña:").lower().strip()
    if r1 == "leandro": 
        st.success("¡MUY BIEN!, TE KIERO AMIGUITA GUAPA")
        if st.button("Seguir"):
            st.session_state.nivel = 3
            st.rerun()
    elif r1 != "":
        st.warning("DEJAS MAL OH, TAKE NI PA ESO SIRVES, VUELVE A RESPONDER!!")

# --- NIVEL 3: ---
elif st.session_state.nivel == 3:
    st.markdown("### Nivel 3: La Pregunta Final")
    st.write("¿Como se llama la chica mas Guapa del Mundo?")
    r2 = st.text_input("Última contraseña:").lower().strip()
    if r2 == "alessita":
        st.session_state.nivel = 4
        st.rerun()
    elif r2 != "":
        st.warning("Responde bien GUAPA 😘")

# --- NIVEL 4: GIF Final ---
elif st.session_state.nivel == 4:
    st.balloons()
    st.title("¡Muy bien amiguita, espero te hayas divertido, Quiero q sepas q te kiero mucho, grcs por llegar a mi vida, y espero q nunca te alejes de mi o me olvides, yo nunca lo hare TE AMOOO PRECIOSURAAA! 🎉")
    st.write("Gracias por jugar, Muack 😘")
    st.image("kitty.gif")
    
    if st.button("Volver a Jugar 😏"):
        st.session_state.audio_iniciado = False # Apaga música al reiniciar
        st.session_state.nivel = -1
        st.rerun()
        




































