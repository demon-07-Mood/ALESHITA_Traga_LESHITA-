
import streamlit as st

# Configuración móvil (sin barras laterales ni distracciones)
st.set_page_config(page_title="Para Aleshita", page_icon="✨", layout="centered")

# Ocultar menú de Streamlit para que parezca una app nativa
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Inicializar sistema de niveles
if 'nivel' not in st.session_state:
    st.session_state.nivel = 0

# NIVEL 0: Pantalla de inicio (Obligatorio para que el celular permita el autoplay de audio)
if st.session_state.nivel == 0:
    st.title("Una aventura secreta... 🤫")
    st.write("Sube el volumen de tu celular y presiona el botón cuando estés lista.")
    if st.button("Comenzar Aventura"):
        st.session_state.nivel = 1
        st.rerun()

# NIVEL 1: El Bosque (Inicio del suspenso)
elif st.session_state.nivel == 1:
    # Reproduce la música de suspenso
    st.audio("suspenso.mp3", format="audio/mp3", autoplay=True, loop=True)
    
    st.markdown("### Nivel 1: El Bosque Oscuro 🌲")
    st.write("Caminas por un bosque oscuro y el sendero se divide. ¿Qué camino tomas?")
    
    if st.button("El sendero con huellas"):
        st.error("Caíste en una trampa de barro. ¡Regresa!")
    
    if st.button("El sendero cubierto de neblina"):
        st.session_state.nivel = 2
        st.rerun()

# NIVEL 2: El Candado del Tiempo
elif st.session_state.nivel == 2:
    st.audio("suspenso.mp3", format="audio/mp3", autoplay=True, loop=True)
    
    st.markdown("### Nivel 2: La Puerta de Piedra 🪨")
    st.write("Lograste pasar. Ahora una puerta bloquea tu paso con la siguiente pregunta:")
    
    # .strip().lower() evita errores si ella pone mayúsculas o espacios al final
    r1 = st.text_input("¿En qué mes empezamos a hablar? (escríbelo en minúsculas)").strip().lower()
    
    if r1 == "octubre": # REEMPLAZA "octubre" POR LA RESPUESTA REAL
        st.success("¡La puerta se abre!")
        if st.button("Avanzar a la bóveda"):
            st.session_state.nivel = 3
            st.rerun()
    elif r1 != "":
        st.warning("La puerta no se mueve. Intenta de nuevo.")

# NIVEL 3: La Bóveda Final
elif st.session_state.nivel == 3:
    st.audio("suspenso.mp3", format="audio/mp3", autoplay=True, loop=True)
    
    st.markdown("### Nivel 3: La Bóveda de Seguridad 🔐")
    st.write("Estás frente a la bóveda final. Necesitas la contraseña clave.")
    
    r2 = st.text_input("¿Cuál es el apodo por el que te llamo?").strip().lower()
    
    if r2 == "aleshita":
        st.session_state.nivel = 4
        st.rerun()
    elif r2 != "":
        st.warning("Contraseña incorrecta.")

# NIVEL 4: Recompensa y Mensaje Final
elif st.session_state.nivel == 4:
    st.balloons()
    
    st.title("¡Lo lograste! 🎉")
    st.write("Superaste todos los obstáculos.")
    st.markdown("Quería hacer algo único para ti. Te tengo muchísimo cariño y valoro todo lo que compartimos. ¡Espero que este pequeño juego te haya sacado una sonrisa!")
    st.write("💖")
    
    # Botón opcional para reiniciar
    if st.button("Volver a jugar"):
        st.session_state.nivel = 0
        st.rerun()













































































