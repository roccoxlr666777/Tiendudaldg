import streamlit as st
import pandas as pd
import os
import random

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
# 2. INYECCIÓN DE DISEÑO VISUAL (CSS) - NEÓN Y TIPOGRAFÍAS
# ==========================================
st.markdown("""
    <style>
    /* Fondo General Oscuro */
    .stApp {
        background-color: #080808; 
    }

    /* SISTEMA TIPOGRÁFICO: Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Anton&family=Open+Sans:wght@400;700&display=swap');

    /* Títulos Principales (Anton) - EFECTO NEÓN (UDAL Colors) */
    h1, h2 {
        font-family: 'Anton', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
    }
    
    /* Neón UDAL Azul Rey */
    .neon-title {
        color: #fff;
        text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #002366, 0 0 20px #002366, 0 0 25px #002366;
        font-size: 3rem !important;
        margin-bottom: 30px;
    }
    
    /* Neón Rojo Sangre */
    .neon-sub {
        color: #fff;
        text-shadow: 0 0 5px #fff, 0 0 10px #880808, 0 0 15px #880808, 0 0 20px #880808;
        font-size: 1.8rem !important;
        margin-bottom: 20px;
        font-family: 'Anton', sans-serif !important;
    }

    /* Texto General (Open Sans) */
    p, li, .stMarkdown, .stButton {
        font-family: 'Open Sans', sans-serif !important;
        color: #ccc;
    }

    /* Cajas de Contenido con Borde Neón Azul Rey */
    .udal-card {
        background-color: #1a1a1a;
        padding: 25px;
        border-radius: 12px;
        border: 2px solid #002366;
        box-shadow: 0 4px 20px rgba(0, 35, 102, 0.4);
        margin-bottom: 25px;
    }

    /* Estilo del Banner de En Construcción */
    .construction-banner {
        background: linear-gradient(45deg, #002366, #880808, #f2a900);
        color: black;
        padding: 12px;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
        border-radius: 5px;
        margin-bottom: 30px;
        font-family: 'anton', sans-serif !important;
        font-size: 1.2rem;
    }

    /* Estilo de los Botones de Votación y WhatsApp */
    .stButton>button, a.udal-btn {
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
    }
    .stButton>button:hover, a.udal-btn:hover {
        background-color: #f2a900 !important;
        color: black !important;
        box-shadow: 0 0 15px #f2a900 !important;
    }
    
    /* Estilo Sticker para Promociones */
    .sticker-promo {
        display: inline-block;
        background-color: #222;
        color: #f2a900;
        padding: 8px 15px;
        margin: 5px;
        border-radius: 20px;
        border: 2px dashed #f2a900;
        font-family: 'Anton', sans-serif !important;
        text-transform: uppercase;
    }

    /* Ocultar elementos estándar de Streamlit */
    #MainMenu, footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SISTEMA DE VOTACIÓN (CEREBRO / BACK-END)
# ==========================================
# Archivo donde guardaremos los votos de forma persistente
ARCHIVO_VOTOS = "votos_udal.csv"

# Función para inicializar o cargar el archivo de votos
def cargar_votos():
    if not os.path.exists(ARCHIVO_VOTOS):
        # Si no existe, creamos el archivo con 0 votos
        df = pd.DataFrame({
            'Diseño': ["VANDAL ROOTS", "AGGROUDAL", "STREET", "LEOR"],
            'Votos': [0, 0, 0, 0]
        })
        df.to_csv(ARCHIVO_VOTOS, index=False)
    return pd.read_csv(ARCHIVO_VOTOS)

# Función para registrar un voto real
def registrar_voto(diseno_elegido):
    df_votos = cargar_votos()
    # Busca el diseño en el CSV y le suma 1 voto
    df_votos.loc[df_votos['Diseño'] == diseno_elegido, 'Votos'] += 1
    # Guarda el archivo actualizado
    df_votos.to_csv(ARCHIVO_VOTOS, index=False)
    st.session_state.voto_registrado = True # Memoria temporal para mostrar éxito

# Carga inicial de votos para las barras de progreso
cargar_votos()

# ==========================================
# 4. INTERFAZ PRINCIPAL
# ==========================================

# Banner de Status
st.markdown("<div class='construction-banner'>🚧 STOREFRONT UDAL: EN CONSTRUCCIÓN 🚧</div>", unsafe_allow_html=True)

# Encabezado Neón
st.markdown("<h1 class='neon-title'>Urban Development Academic Lab</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='neon-sub'>Diseño Gráfico UDAL</h2>", unsafe_allow_html=True)

# Layout: Dos columnas principales (Diseños a la izq, Interacción a la der)
col_disenos, col_interaccion = st.columns([3, 1])

# --- COLUMNA IZQUIERDA: LOS 4 DISEÑOS ---
with col_disenos:
    st.markdown("<div class='udal-card'>", unsafe_allow_html=True)
    st.markdown("### 🖼️ Catálogo Próximamente Disponible</h3>", unsafe_allow_html=True)
    
    # Maquetamos los diseños en 2 columnas (2x2)
    grid_col1, grid_col2 = st.columns(2)
    
    # 1. VANDAL ROOTS
    with grid_col1:
        st.image("vandal_roots.png", use_container_width=True)
        st.markdown("<b style='color:#f2a900;'>VANDAL ROOTS</b>", unsafe_allow_html=True)
        st.write("*(Emoji Sticker Style)*")
        st.caption("“Luce con orgullo tu escuela”")
        if st.button("🗳️ Votar por VANDAL ROOTS", key="vote_vandal"):
            registrar_voto("VANDAL ROOTS")
            
    # 2. AGGROUDAL
    with grid_col2:
        st.image("aggroudal.png", use_container_width=True)
        st.markdown("<b style='color:#f2a900;'>AGGROUDAL</b>", unsafe_allow_html=True)
        st.write("*(Chamarra negra / Chavos Fuertes)*")
        st.caption("“Viste como lo que eres, se fuerte, se exitoso”")
        if st.button("🗳️ Votar por AGGROUDAL", key="vote_aggro"):
            registrar_voto("AGGROUDAL")
    
    # Espacio entre filas
    st.write("---")
    grid_col3, grid_col4 = st.columns(2)
    
    # 3. STREET
    with grid_col3:
        st.image("street.png", use_container_width=True)
        st.markdown("<b style='color:#f2a900;'>STREET</b>", unsafe_allow_html=True)
        st.write("*(El más neón)*")
        st.caption("“Orgullos que se viste” | (Pocas piezas disponibles)")
        if st.button("🗳️ Votar por STREET", key="vote_street"):
            registrar_voto("STREET")
            
    # 4. LEOR
    with grid_col4:
        st.image("leor.png", use_container_width=True)
        st.markdown("<b style='color:#f2a900;'>LEOR</b>", unsafe_allow_html=True)
        st.write("*(Azul con dorado)*")
        st.caption("1- “Tu estilo pide más... Nosotros ya lo creamos. Solo tómalo.”")
        st.caption("2- “No es ropa cualquiera... es la que todos quisieran tener.”")
        if st.button("🗳️ Votar por LEOR", key="vote_leor"):
            registrar_voto("LEOR")
            
    st.markdown("</div>", unsafe_allow_html=True)

# --- COLUMNA DERECHA: INTERACCIÓN Y PROMOS ---
with col_interaccion:
    
    # Caja 1: Zona de Votación y Resultados (Cerebro)
    st.markdown("<div class='udal-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #880808;'>🗳️ Resultados en Tiempo Real</h4>", unsafe_allow_html=True)
    st.write("¿Cuál de estos diseños neon-graffiti deberíamos lanzar primero?")
    
    # Mostramos mensaje de éxito si ya votó (sin globos)
    if 'voto_registrado' in st.session_state and st.session_state.voto_registrado:
        st.success("¡Voto registrado en el servidor! Gracias por apoyar a tu favorito.")
        st.session_state.voto_registrado = False # Reset
        
    # Cargamos votos actualizados para mostrar las barras
    df_actualizado = cargar_votos()
    total_votos = df_actualizado['Votos'].sum()
    
    for _, row in df_actualizado.iterrows():
        st.markdown(f"<b style='color:#ccc;'>{row['Diseño']}</b>: {row['Votos']} votos", unsafe_allow_html=True)
        if total_votos > 0:
            progreso = row['Votos'] / total_votos
            st.progress(progreso)
        else:
            st.progress(0)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Caja 2: Integración WhatsApp y Código QR
    st.markdown("<div class='udal-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #002366;'>📲 Pre-pedidos WhatsApp</h4>", unsafe_allow_html=True)
    st.write("Escanea o da clic para separar tu diseño exclusivo.")
    
    # NÚMERO DE EJEMPLO DEL USUARIO: +52 221 653 1593 (formateado)
    whatsapp_url = "https://wa.me/5212216531593?text=Hola UDAL Academic Lab, quiero info sobre las nuevas sudaderas neón."
    
    # Usamos una API gratuita para generar el QR side-by-side
    st.markdown(f'<a href="{whatsapp_url}"><img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={whatsapp_url}" width="150" style="border: 2px solid #002366;"></a>', unsafe_allow_html=True)
    st.write("") # Espacio
    
    st.markdown(f'<a href="{whatsapp_url}" class="udal-btn">Abrir WhatsApp</a>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 5. SECCIÓN DE PROMOCIONES (STICKER STYLE)
# ==========================================
st.markdown("---")
st.markdown("<h3 class='neon-sub'>¡Apoya a tu favorito! (Opciones UDAL)</h3>", unsafe_allow_html=True)

st.markdown("""
<div class='udal-card' style='text-align:center;'>
    <div class='sticker-promo'>VANDAL ROOTS Sticker #UDAL</div>
    <div class='sticker-promo'>AGGROUDAL Strong style</div>
    <div class='sticker-promo'>STREET Neon Look</div>
    <div class='sticker-promo'>LEOR Golden vibes</div>
    <p style='margin-top:10px;'>Invita a tus amigos a votar y prepárate para recompensas exclusivas en el lanzamiento.</p>
</div>
""", unsafe_allow_html=True)

st.warning("⚠️ Zona de recompensas e instrucciones finales en construcción (esperando imágenes de los muchachos y las instrucciones para el sistema de rewards).")
