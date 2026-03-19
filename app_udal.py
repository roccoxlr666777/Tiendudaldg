import streamlit as st
import pandas as pd
import os
import io

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA (ESTILO GRÁFICO UDAL)
# ==========================================
st.set_page_config(
    page_title="udal Storefront - Urban Development Academic Lab", 
    page_icon="🎨", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. INYECCIÓN DE DISEÑO VISUAL (CSS)
# ==========================================
st.markdown("""
    <style>
    /* Fondo General Oscuro y fuentes profesionales */
    .stApp { background-color: #080808; }

    @import url('https://fonts.googleapis.com/css2?family=Anton&family=Open+Sans:wght@400;700&display=swap');

    h1, h2, h3, h4 {
        font-family: 'Anton', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
    }
    
    .neon-title {
        color: #fff;
        text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #002366, 0 0 20px #002366;
        font-size: 3.2rem !important;
        margin-bottom: 25px;
    }
    
    .neon-sub {
        color: #fff;
        text-shadow: 0 0 5px #fff, 0 0 10px #880808, 0 0 15px #880808;
        font-size: 2rem !important;
        margin-bottom: 20px;
    }

    /* Texto General: Open Sans con ajuste automático de palabras */
    p, li, .stMarkdown, .stCaption {
        font-family: 'Open Sans', sans-serif !important;
        color: #ccc;
        line-height: 1.5 !important;
        word-wrap: break-word; 
        overflow-wrap: break-word;
    }

    /* Caja de Contenido Estilo UDAL */
    .udal-card {
        background-color: #1a1a1a;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #002366;
        box-shadow: 0 4px 20px rgba(0, 35, 102, 0.4);
        margin-bottom: 25px;
    }

    /* Botones de Descarga y Contacto con el look neón */
    .stDownloadButton>button, a.udal-contact-btn {
        background-color: transparent !important;
        color: #f2a900 !important;
        border: 2px solid #f2a900 !important;
        border-radius: 8px !important;
        width: 100% !important;
        transition: 0.3s !important;
        text-transform: uppercase !important;
        font-weight: bold !important;
        text-align: center;
        display: block;
        padding: 12px;
        text-decoration: none;
        font-family: 'Open Sans', sans-serif !important;
    }
    .stDownloadButton>button:hover, a.udal-contact-btn:hover {
        background-color: #f2a900 !important;
        color: black !important;
        box-shadow: 0 0 15px #f2a900 !important;
    }

    /* Logo de WhatsApp para contacto */
    .whatsapp-logo-container {
        text-align: center;
        margin-bottom: 10px;
    }
    .whatsapp-logo-container img {
        width: 60px;
        transition: 0.3s;
    }
    .whatsapp-logo-container img:hover {
        transform: scale(1.1);
        filter: drop-shadow(0 0 10px #25d366);
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. INTERFAZ PRINCIPAL (DRAFTING)
# ==========================================

# Encabezado Neón
st.markdown("<h1 class='neon-title'>Urban Development Academic Lab</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='neon-sub'>Diseño Gráfico UDAL</h2>", unsafe_allow_html=True)

# Sección 1: Instrucciones Generales
st.markdown("<div class='udal-card'>", unsafe_allow_html=True)
st.markdown("""
### ¡Descarga el sticker de tu diseño preferido! </h3>
<p style='text-align:center;'>
Compártelo, úsalo en tus redes sociales, pégalo, etc. Y mándanos una foto para obtener beneficios o premios de lanzamiento y participar en la rifa de prendas.
</p>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Sección 2: El Catálogo y los Botones de DESCARGA (Guiados)
st.markdown("### Selecciona el sticker para descargar</h3>", unsafe_allow_html=True)
st.write("Estamos en construcción. Si ves un error, es porque nos falta el archivo del sticker.")

col1, col2, col3, col4 = st.columns(4)

# Función para simular data de imagen para descarga real (para este ejemplo)
def get_dummy_data():
    return io.BytesIO(b"\x00" * 1024).read()

# Función para intentar cargar un sticker de forma segura
def mostrar_sticker(column, filename, sticker_title, dl_id):
    with column:
        # El código busca el archivo individual. Si no existe, muestra un error guiado.
        if os.path.exists(filename):
            st.image(filename, use_container_width=True)
            st.markdown(f"<h4 style='color:#f2a900;'>{sticker_title}</h4>", unsafe_allow_html=True)
            st.download_button(
                label="DESCARGAR ⬇️", 
                data=get_dummy_data(), # Reemplazar por data real de la imagen en prod.
                file_name=f"udal_sticker_{filename}", 
                mime="image/png", 
                key=dl_id
            )
        else:
            # ERROR GUIADO: El simulador te dice exactamente qué te falta.
            st.markdown(f"<div class='udal-card' style='border-color:#880808; text-align:center;'>", unsafe_allow_html=True)
            st.error(f"Falta el archivo: **`{filename}`**")
            st.markdown("<p style='font-size:0.8rem;'>Suba el sticker individual a GitHub con este nombre exacto.</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# 1. Sticker 1
mostrar_sticker(col1, "sticker_1.png", "Diseño 1", "dl1")

# 2. Sticker 2
mostrar_sticker(col2, "sticker_2.png", "Diseño 2", "dl2")

# 3. Sticker 3
mostrar_sticker(col3, "sticker_3.png", "Diseño 3", "dl3")

# 4. Sticker 4
mostrar_sticker(col4, "sticker_4.png", "Diseño 4", "dl4")

st.markdown("---")

# ==========================================
# 4. NUEVA SECCIÓN DE INFORMACIÓN Y CONTACTO
# ==========================================
st.markdown("### MÁS INFORMACIÓN DEL PROYECTO 360</h3>", unsafe_allow_html=True)

col_info, col_contacto = st.columns([2, 1])

# Información Académica
with col_info:
    st.markdown("<div class='udal-card' style='border-color:#f2a900; box-shadow: 0 4px 20px rgba(242, 169, 0, 0.3);'>", unsafe_allow_html=True)
    st.markdown("<b style='color:#f2a900; font-size:1.1rem;'>Urban Development Academic Lab (UDAL) - Puebla</b>", unsafe_allow_html=True)
    st.markdown("""
    El UDAL es una aceleradora de talento y centro de investigación en diseño y comunicación de Puebla. Este proyecto de stickers es la primera fase del lanzamiento de la Aceleradora UDAL, buscando la creación de productos que marquen la pauta en la escena urbana.
    
    Este simulador es un ejercicio académico integral de Diseño Gráfico que conecta la planeación corporativa (misión, visión, FODA) con el desarrollo técnico de productos (INCI, COFEPRIS) y estrategias de marketing bilingües de alto nivel.
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Sección de Contacto WhatsApp (LOGO FUNCIONAL)
with col_contacto:
    st.markdown("<div class='udal-card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<b style='color:#ccc; font-size:1.1rem; text-transform:uppercase;'>Contáctanos vía WhatsApp</b>", unsafe_allow_html=True)
    st.write("Dudas, informes o envía tus fotos para la rifa.")
    
    # URL de WhatsApp con mensaje pre-escrito a tu celular: 2221158614
    whatsapp_url = "https://wa.me/5212221158614?text=Hola UDAL Academic Lab, requiero informes sobre el proyecto de stickers y la Aceleradora de Talento."
    
    # Logo de WhatsApp como enlace clickable
    st.markdown(f'<div class="whatsapp-logo-container"><a href="{whatsapp_url}"><img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp UDAL Lab"></a></div>', unsafe_allow_html=True)
    
    # Botón de texto alternativo
    st.markdown(f'<a href="{whatsapp_url}" class="udal-contact-btn">2221158614</a>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
