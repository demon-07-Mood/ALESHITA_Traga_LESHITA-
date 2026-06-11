import streamlit as st

# Inicializar el estado de la etapa si no existe
if 'etapa' not in st.session_state:
    st.session_state.etapa = 1

# ETAPA 1: La decisión (Aventura)
if st.session_state.etapa == 1:
    st.markdown("### Capítulo 1: El comienzo")
    st.write("Estás frente a un castillo y hay dos entradas. ¿Por dónde quieres entrar?")
    
    # Botones apilados para móvil
    if st.button("Puerta principal"):
        st.session_state.etapa = 2
        st.rerun() # Recarga la página para ir a la etapa 2
        
    if st.button("Ventana secreta"):
        st.session_state.etapa = 3
        st.rerun()

# ETAPA 2: El Acertijo (Búsqueda del Tesoro)
elif st.session_state.etapa == 2:
    st.markdown("### La Puerta Principal")
    st.write("Un guardia te detiene. Para pasar y leer tu primer mensaje, debes responder:")
    
    respuesta = st.text_input("¿En qué mes nos conocimos?").lower()
    
    if respuesta == "octubre": # Reemplaza por la respuesta real
        st.success("¡Correcto! Eres increíble.")
        st.write("✨ **Mensaje desbloqueado:** *Siempre recuerdo ese día, fue de los mejores...*")
        st.balloons()
        
        if st.button("Continuar la aventura"):
            st.session_state.etapa = 4
            st.rerun()
    elif respuesta != "":
        st.error("Mmm, haz memoria. ¡Intenta de nuevo!")

# ETAPA 3: Ruta alternativa
elif st.session_state.etapa == 3:
    st.write("Entraste por la ventana y encontraste un cofre sorpresa...")
    # Aquí puedes poner otro acertijo o simplemente avanzar



































































































