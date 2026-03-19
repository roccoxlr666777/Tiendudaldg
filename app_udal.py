import streamlit as st
from PIL import Image
import os

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA UDAL URBANO
# ==========================================
st.set_page_config(
    page_title="udal Storefront - Laboratorio Urbano", 
    page_icon="🎨", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. INYECCIÓN DE DISEÑO VISUAL (CSS) - EFECTO NEÓN Y URBANO
# ==========================================
st.markdown("""
    <style>
    /* Fondo General Oscuro */
    .stApp {
        background-color: #080808; 
    }

    /* Títulos Principales con EFECTO NEÓN (UDAL Colors) */
    h1, h2, h3 {
        font-family: 'Courier New', Courier, monospace;
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    
    /* Neón UDAL Azul/Oro */
    .neon-title {
        color: #fff;
        text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #f2a900, 0 0 20px #f2a900, 0 0 25px #f2a900;
        text-align: center;
        font-size: 3rem !important;
        margin-bottom: 30px;
    }
    
    /* Neón UDAL Fucsia/Cian (de la imagen) */
    .neon-sub {
        color: #fff;
        text-shadow: 0 0 5px #fff, 0 0 10px #ff00ff, 0 0 15px #00ffff, 0 0 20px #00ffff;
        text-align: center;
        margin-bottom: 10px;
    }

    /* Cajas de Contenido con Borde Dorado */
    .udal-card {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #f2a900;
        box-shadow: 0 4px 15px rgba(242, 169, 0, 0.2);
        margin-bottom: 20px;
    }

    /* Estilo del Banner de En Construcción */
    .construction-banner {
        background: linear-gradient(45deg, #f2a900, #ff00ff, #00ffff);
        color: black;
        padding: 10px;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
        border-radius: 5px;
        margin-bottom: 25px;
        font-family: sans-serif;
    }

    /* Estilo del Botón de Votación */
    .stButton>button {
        background-color: transparent;
        color: #f2a900;
        border: 2px solid #f2a900;
        border-radius: 5px;
        width: 100%;
        transition: 0.3s;
        text-transform: uppercase;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #f2a900;
        color: black;
        box-shadow: 0 0 10px #f2a900;
    }

    /* Ocultar elementos estándar de Streamlit */
    #MainMenu, footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. INTERFAZ PRINCIPAL (PANTALLA ÚNICA)
# ==========================================

# Banner de Status
st.markdown("<div class='construction-banner'>🚧 STOREFRONT UDAL: EN CONSTRUCCIÓN 🚧</div>", unsafe_allow_html=True)

# Encabezado Neón
st.markdown("<h1 class='neon-title'>Laboratorio Urbano de Desarrollo de Accesorios</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='neon-sub'>Diseño Gráfico UDAL</h3>", unsafe_allow_html=True)

# Layout de dos columnas (Izquierda: Imagen, Derecha: Votación e Integración)
col_imagen, col_interaccion = st.columns([2, 1])

# --- Columna Izquierda: Imagen del Catálogo ---
with col_imagen:
    # Cargar y mostrar la imagen provided por el usuario
    if os.path.exists("image_6.png"):
        image = Image.open("image_6.png")
        st.image(image, caption="Catálogo Próximamente Disponible (Diseños de Alumnos)", use_container_width=True)
    else:
        st.error("Error: No se encontró la imagen 'image_6.png' en la misma carpeta del script.")

# --- Columna Derecha: Interacción ---
with col_interaccion:
    
    # Caja 1: Votación Interactiva
    st.markdown("<div class='udal-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #f2a900;'>🗳️ ¡Vota por tu diseño favorito!</h4>", unsafe_allow_html=True)
    st.write("¿Cuál de estos diseños neon-graffiti deberíamos lanzar primero?")
    
    # Opciones de votación basadas en la imagen
    diseno_sel = st.radio(
        "Elige tu diseño:",
        ["Sudadera Neon Jaguar (Negra)", "Sudadera Graffiti UDAL (Blanca)", "Playera Ubal Graffiti (Over-size)"]
    )
    
    if st.button("Enviar Voto"):
        st.balloons()
        st.success(f"¡Voto registrado para: **{diseno_sel}**!")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Caja 2: Integración WhatsApp y Código de Barras (QR)
    st.markdown("<div class='udal-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #00ffff;'>📲 Pre-pedidos vía WhatsApp</h4>", unsafe_allow_html=True)
    st.write("Escanea el código o dale clic para contactarnos y separar tu diseño.")
    
    # Crear un QR funcional que abra WhatsApp con un mensaje predefinido
    # CAMBIA ESTE NÚMERO POR EL TUYO REAL (Ej. +521222...)
    # NÚMERO DE EJEMPLO DEL USUARIO: +52 221 653 1593 (formateado)
    whatsapp_url = "https://wa.me/52122216531593?text=Hola UDAL, quiero info sobre las nuevas sudaderas neón."
    
    # Usamos una API gratuita para generar el QR side-by-side
    st.markdown(f'<a href="{whatsapp_url}"><img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={whatsapp_url}" width="150"></a>', unsafe_allow_html=True)
    st.write("") # Espacio
    st.markdown(f'<a href="{whatsapp_url}"><div style="background-color: transparent; color: #00ffff; border: 2px solid #00ffff; padding: 10px; border-radius: 5px; text-align: center; text-transform: uppercase;">Abrir WhatsApp</div></a>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 4. SECCIÓN DE RECOMPENSAS (Marcador de posición)
# ==========================================
st.markdown("---")
st.markdown("<h3 class='neon-sub'>¡Comparte y Gana Recompensas!</h3>", unsafe_allow_html=True)

# Usamos st.warning para indicar que falta información, como pediste.
st.warning("⚠️ Zona de recompensas en construcción (esperando las imágenes de los muchachos y las instrucciones finales). Próximamente: Invita a tus amigos y recibe descuentos exclusivos.")
