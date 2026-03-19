import streamlit as st
import pandas as pd
import os

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS
# ==========================================
st.set_page_config(page_title="udal Storefront", page_icon="🎨", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp { background-color: #080808; }
    @import url('https://fonts.googleapis.com/css2?family=Anton&family=Open+Sans:wght@400;700&display=swap');

    h1, h2, h3, h4 { font-family: 'Anton', sans-serif !important; text-transform: uppercase; letter-spacing: 2px; text-align: center; }
    
    .neon-title { color: #fff; text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #002366, 0 0 20px #002366; font-size: 3.2rem !important; margin-bottom: 25px; }
    .neon-sub { color: #fff; text-shadow: 0 0 5px #fff, 0 0 10px #880808, 0 0 15px #880808; font-size: 2rem !important; margin-bottom: 20px; }

    p, li, .stMarkdown, .stCaption { font-family: 'Open Sans', sans-serif !important; color: #ccc; line-height: 1.5 !important; word-wrap: break-word; overflow-wrap: break-word; }

    /* Forzar que TODAS las imágenes de los lookbooks tengan el mismo tamaño exacto */
    [data-testid="stImage"] img {
        height: 380px !important;
        object-fit: cover !important;
        border-radius: 8px;
        border: 1px solid #333;
    }

    .udal-card { background-color: #1a1a1a; padding: 25px; border-radius: 12px; border: 2px solid #002366; box-shadow: 0 4px 20px rgba(0, 35, 102, 0.4); margin-bottom: 25px; height: auto; }
    .construction-banner { background: linear-gradient(45deg, #002366, #880808, #f2a900); color: black; padding: 12px; text-align: center; font-weight: bold; text-transform: uppercase; border-radius: 5px; margin-bottom: 30px; font-family: 'anton', sans-serif !important; font-size: 1.2rem; }

    .stButton>button, .stDownloadButton>button, a.udal-btn {
        background-color: transparent !important; color: #f2a900 !important; border: 2px solid #f2a900 !important; border-radius: 8px !important; width: 100% !important; transition: 0.3s !important; text-transform: uppercase !important; font-weight: bold !important; text-align: center; display: block; padding: 12px; text-decoration: none; font-family: 'Open Sans', sans-serif !important;
    }
    .stButton>button:hover, .stDownloadButton>button:hover, a.udal-btn:hover { background-color: #f2a900 !important; color: black !important; box-shadow: 0 0 15px #f2a900 !important; }

    .whatsapp-logo-container { text-align: center; margin-bottom: 10px; }
    .whatsapp-logo-container img { width: 60px; transition: 0.3s; }
    .whatsapp-logo-container img:hover { transform: scale(1.1); filter: drop-shadow(0 0 10px #25d366); }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. FUNCIONES DE BACKEND (VOTOS)
# ==========================================
ARCHIVO_VOTOS = "votos_udal.csv"

def cargar_votos():
    if not os.path.exists(ARCHIVO_VOTOS):
        df = pd.DataFrame({'Diseño': ["VANDAL ROOTS", "AGGROUDAL", "STREET", "LEOR"], 'Votos': [0, 0, 0, 0]})
        df.to_csv(ARCHIVO_VOTOS, index=False)
    return pd.read_csv(ARCHIVO_VOTOS)

def registrar_voto(diseno_elegido):
    df_votos = cargar_votos()
    df_votos.loc[df_votos['Diseño'] == diseno_elegido, 'Votos'] += 1
    df_votos.to_csv(ARCHIVO_VOTOS, index=False)
    st.session_state.voto_registrado = True 

cargar_votos()

# ==========================================
# 3. INTERFAZ PRINCIPAL: LOOKBOOKS
# ==========================================
st.markdown("<div class='construction-banner'>🚧 STOREFRONT EN CONSTRUCCIÓN 🚧</div>", unsafe_allow_html=True)
st.markdown("<h1 class='neon-title'>Urban Development Academic Lab</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='neon-sub'>Diseño Gráfico UDAL</h2>", unsafe_allow_html=True)

col_disenos, col_interaccion = st.columns([3, 1])

with col_disenos:
    st.markdown("<div class='udal-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#ccc;'>🖼️ Choose your Style</h3>", unsafe_allow_html=True)
    
    grid_col1, grid_col2 = st.columns(2)
    
    # 1. VANDAL ROOTS
    with grid_col1:
        if os.path.exists("vandal_roots.jpg"): st.image("vandal_roots.jpg", use_container_width=True)
        else: st.error("Falta: vandal_roots.jpg")
        st.markdown("<h4 style='color:#f2a900; margin-top:10px;'>VANDAL ROOTS</h4>", unsafe_allow_html=True)
        st.caption("<b style='font-size:1.1rem;'>Luce con orgullo tu escuela</b>", unsafe_allow_html=True)
        if st.button("🗳️ Votar por VANDAL ROOTS", key="vandal"): registrar_voto("VANDAL ROOTS")
            
    # 2. AGGROUDAL
    with grid_col2:
        if os.path.exists("aggroudal.jpg"): st.image("aggroudal.jpg", use_container_width=True)
        else: st.error("Falta: aggroudal.jpg")
        st.markdown("<h4 style='color:#f2a900; margin-top:10px;'>AGGROUDAL</h4>", unsafe_allow_html=True)
        st.caption("<b style='font-size:1.1rem;'>Viste como lo que eres, se fuerte, se exitoso</b>", unsafe_allow_html=True)
        if st.button("🗳️ Votar por AGGROUDAL", key="aggro"): registrar_voto("AGGROUDAL")
    
    st.write("---")
    grid_col3, grid_col4 = st.columns(2)
    
    # 3. STREET
    with grid_col3:
        if os.path.exists("street.jpg"): st.image("street.jpg", use_container_width=True)
        else: st.error("Falta: street.jpg")
        st.markdown("<h4 style='color:#f2a900; margin-top:10px;'>STREET</h4>", unsafe_allow_html=True)
        st.caption("<b style='font-size:1.1rem;'>Orgullos que se viste | Pocas piezas</b>", unsafe_allow_html=True)
        if st.button("🗳️ Votar por STREET", key="street"): registrar_voto("STREET")
            
    # 4. LEOR (Texto unificado)
    with grid_col4:
        if os.path.exists("leor.jpg"): st.image("leor.jpg", use_container_width=True)
        else: st.error("Falta: leor.jpg")
        st.markdown("<h4 style='color:#f2a900; margin-top:10px;'>LEOR</h4>", unsafe_allow_html=True)
        st.caption("<b style='font-size:1.1rem;'>Tu estilo pide más... Nosotros ya lo creamos. No es ropa cualquiera, es la que todos quisieran tener.</b>", unsafe_allow_html=True)
        if st.button("🗳️ Votar por LEOR", key="leor"): registrar_voto("LEOR")
            
    st.markdown("</div>", unsafe_allow_html=True)

# --- COLUMNA DERECHA: RESULTADOS Y COMPARTIR ---
with col_interaccion:
    st.markdown("<div class='udal-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #880808;'>🗳️ Resultados en Tiempo Real</h4>", unsafe_allow_html=True)
    
    if 'voto_registrado' in st.session_state and st.session_state.voto_registrado:
        st.success("¡Voto registrado!")
        st.session_state.voto_registrado = False 
        
    df_actualizado = cargar_votos()
    total_votos = df_actualizado['Votos'].sum()
    
    for _, row in df_actualizado.iterrows():
        st.markdown(f"<b style='color:#ccc;'>{row['Diseño']}</b>: {row['Votos']} votos", unsafe_allow_html=True)
        if total_votos > 0: st.progress(row['Votos'] / total_votos)
        else: st.progress(0)
    
    # Botón para que TÚ descargues la base de datos de votos
    with open(ARCHIVO_VOTOS, "rb") as f:
        st.download_button("📥 Descargar Reporte de Votos (CSV)", f, file_name="reporte_votos_udal.csv")
    st.markdown("</div>", unsafe_allow_html=True)

    # NUEVO: SECCIÓN DE COMPARTIR Y QR URBANO
    st.markdown("<div class='udal-card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #002366;'>🌐 Comparte la Tienda</h4>", unsafe_allow_html=True)
    
    # URL de tu app en Streamlit (Cambia esto si tu link es diferente)
    app_url = "https://udal-storefront.streamlit.app" 
    
    # QR personalizado: bg color 1a1a1a (gris oscuro), color f2a900 (dorado)
    qr_urbano = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={app_url}&color=f2a900&bgcolor=1a1a1a&margin=10"
    
    st.markdown(f'<img src="{qr_urbano}" style="border: 2px solid #f2a900; border-radius: 10px; margin-bottom: 15px;">', unsafe_allow_html=True)
    st.code(app_url, language="text")
    st.caption("Copia este link o escanea el QR para votar.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# 4. SECCIÓN: DESCARGA DE STICKERS
# ==========================================
st.markdown("<h3 class='neon-sub'>¡Descarga tu Sticker UDAL!</h3>", unsafe_allow_html=True)
st.write("Compártelo en redes y mándanos foto a WhatsApp para participar en la rifa de lanzamiento.")

col_s1, col_s2, col_s3, col_s4 = st.columns(4)

def mostrar_sticker(columna, archivo_sticker, titulo):
    with columna:
        if os.path.exists(archivo_sticker):
            st.image(archivo_sticker, use_container_width=True)
            st.markdown(f"<h4 style='color:#f2a900; font-size:1.2rem;'>{titulo}</h4>", unsafe_allow_html=True)
            with open(archivo_sticker, "rb") as file:
                st.download_button(label="DESCARGAR ⬇️", data=file, file_name=f"UDAL_{titulo}.png", mime="image/png", key=f"dl_{titulo}")
        else:
            st.error(f"⚠️ Falta archivo: {archivo_sticker}")

mostrar_sticker(col_s1, "sticker_1.PNG", "VANDAL ROOTS")
mostrar_sticker(col_s2, "sticker_2.PNG", "AGGROUDAL")
mostrar_sticker(col_s3, "sticker_3.PNG", "STREET")
mostrar_sticker(col_s4, "sticker_4.PNG", "LEOR")

st.markdown("---")

# ==========================================
# 5. SECCIÓN FINAL: INFORMACIÓN Y WHATSAPP
# ==========================================
st.markdown("### MÁS INFORMACIÓN DEL PROYECTO</h3>", unsafe_allow_html=True)

col_info, col_contacto = st.columns([2, 1])

with col_info:
    st.markdown("<div class='udal-card' style='border-color:#f2a900;'>", unsafe_allow_html=True)
    st.markdown("<b style='color:#f2a900; font-size:1.1rem;'>Urban Development Academic Lab (UDAL)</b>", unsafe_allow_html=True)
    st.markdown("""
    El UDAL es una aceleradora de talento y centro de investigación en diseño de Puebla. Este proyecto conecta la planeación corporativa con el desarrollo técnico de productos y estrategias de marketing.
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_contacto:
    st.markdown("<div class='udal-card' style='text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<b style='color:#ccc; font-size:1.1rem; text-transform:uppercase;'>Contáctanos vía WhatsApp</b>", unsafe_allow_html=True)
    st.write("Dudas, pre-pedidos o envía tus fotos para la rifa.")
    whatsapp_url = "https://wa.me/5212221158614?text=Hola UDAL Academic Lab, requiero informes del proyecto."
    st.markdown(f'<div class="whatsapp-logo-container"><a href="{whatsapp_url}"><img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp UDAL Lab"></a></div>', unsafe_allow_html=True)
    st.markdown(f'<a href="{whatsapp_url}" class="udal-btn">222 115 8614</a>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
