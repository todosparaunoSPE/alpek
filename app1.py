# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 15:14:42 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuración de la página
st.set_page_config(
    page_title="ALPEK - Portafolio Analista Financiero",
    layout="wide",
    page_icon="📈",
    initial_sidebar_state="expanded"
)


# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)




# Estilos CSS personalizados
st.markdown("""
<style>
    .header-style {
        font-size: 26px;
        font-weight: bold;
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 5px;
    }
    .subheader-style {
        font-size: 20px;
        font-weight: bold;
        color: #2980b9;
        margin-top: 20px;
    }
    .metric-box {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        padding: 8px 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .stDataFrame {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar para filtros y controles
with st.sidebar:
    st.image("logo.png", width=150)
    st.markdown("## Controles de Análisis")
    
    # Selector de período de análisis
    analysis_period = st.selectbox(
        "Período de Análisis",
        ["Últimos 3 meses", "Últimos 6 meses", "Último año", "Personalizado"]
    )
    
    # Selector de tipo de visualización
    chart_type = st.radio(
        "Tipo de Visualización",
        ["Gráfico de Línea", "Gráfico de Barras", "Gráfico de Área"]
    )
    
    st.markdown("---")
    st.markdown("**Configuración Avanzada**")
    show_annotations = st.checkbox("Mostrar anotaciones", value=True)
    show_confidence = st.checkbox("Mostrar bandas de confianza", value=False)
    
    st.markdown("---")
    st.markdown("""
    **Acerca de este portafolio**  
    Herramienta interactiva para análisis financiero  
    Desarrollado por Javier Horacio Pérez Ricárdez 
    Versión 1.0
    """)

# Título principal con estilo ejecutivo
st.markdown("""
<div style="background-color:#3498db;padding:20px;border-radius:10px;margin-bottom:30px">
    <h1 style="color:white;text-align:center;margin:0;">ANALISTA DE PLANEACIÓN FINANCIERA</h1>
    <h3 style="color:white;text-align:center;margin:0;">Portafolio Profesional - Javier Horacio Pérez Ricárdez</h3>
</div>
""", unsafe_allow_html=True)

# Generación de datos dinámicos basados en selección del usuario
if analysis_period == "Últimos 3 meses":
    periods = 90
elif analysis_period == "Últimos 6 meses":
    periods = 180
elif analysis_period == "Último año":
    periods = 365
else:
    periods = st.slider("Seleccione número de días", 30, 730, 120)

price_data = pd.DataFrame({
    'Fecha': pd.date_range(end=datetime.today(), periods=periods, freq='D'),
    'Precio Acción ($MXN)': pd.Series(
        90 + (pd.Series(range(periods)).apply(lambda x: 5 * (x/periods)**0.5) + 
              pd.Series(np.random.normal(0, 2, periods)).values
    ))
})

# Calcular métricas dinámicas
rendimiento_promedio = price_data['Precio Acción ($MXN)'].pct_change().mean() * 100
volatilidad = price_data['Precio Acción ($MXN)'].pct_change().std() * 100
roic_simulado = np.random.uniform(12, 18)  # Simulamos un ROIC entre 12% y 18%
beta_simulado = np.random.uniform(0.8, 1.5)  # Simulamos un Beta entre 0.8 y 1.5

# Tendencia (comparación con período anterior)
tendencia_rendimiento = "↑" if rendimiento_promedio > 10 else "↓"
tendencia_volatilidad = "↓" if volatilidad < 10 else "↑"
tendencia_roic = "↑" if roic_simulado > 15 else "↓"
tendencia_beta = "↓" if beta_simulado < 1.2 else "↑"

# Sección de métricas clave dinámicas
st.markdown("## 📊 Métricas Clave")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="metric-box">
        <h3 style="color:#3498db;margin-top:0;">Rendimiento</h3>
        <h1 style="text-align:center;color:#2c3e50;">{rendimiento_promedio:.2f}%</h1>
        <p style="text-align:center;color:{'#27ae60' if tendencia_rendimiento == '↑' else '#e74c3c'}">
        {tendencia_rendimiento} {abs(rendimiento_promedio - 10):.2f}% vs benchmark</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <h3 style="color:#3498db;margin-top:0;">Volatilidad</h3>
        <h1 style="text-align:center;color:#2c3e50;">{volatilidad:.2f}%</h1>
        <p style="text-align:center;color:{'#27ae60' if tendencia_volatilidad == '↓' else '#e74c3c'}">
        {tendencia_volatilidad} {abs(volatilidad - 10):.2f}% vs benchmark</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <h3 style="color:#3498db;margin-top:0;">ROIC</h3>
        <h1 style="text-align:center;color:#2c3e50;">{roic_simulado:.2f}%</h1>
        <p style="text-align:center;color:{'#27ae60' if tendencia_roic == '↑' else '#e74c3c'}">
        {tendencia_roic} {abs(roic_simulado - 15):.2f}% vs período anterior</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-box">
        <h3 style="color:#3498db;margin-top:0;">Beta</h3>
        <h1 style="text-align:center;color:#2c3e50;">{beta_simulado:.2f}</h1>
        <p style="text-align:center;color:{'#27ae60' if tendencia_beta == '↓' else '#e74c3c'}">
        {tendencia_beta} {abs(beta_simulado - 1.2):.2f} vs período anterior</p>
    </div>
    """, unsafe_allow_html=True)

# Sección de perfil profesional
st.markdown("## 👤 Perfil Profesional")
st.markdown("""
<div style="background-color:#f8f9fa;padding:20px;border-radius:10px;margin-bottom:20px">
    <p style="font-size:16px;line-height:1.6;">
    <strong>Especialista en análisis financiero</strong> con experiencia en el monitoreo de emisoras bursátiles, 
    evaluación de estrategias de recompra, análisis de inteligencia de mercado y desarrollo de informes ejecutivos 
    para la toma de decisiones estratégicas. Dominio avanzado de herramientas como Excel, PowerPoint, Power BI y 
    Bloomberg para análisis cuantitativos y presentación ejecutiva.
    </p>
    <p style="font-size:16px;line-height:1.6;">
    <strong>Habilidades clave:</strong> Pensamiento analítico y crítico, organización y capacidad de síntesis, 
    proactividad y enfoque a resultados, modelado financiero avanzado, comunicación ejecutiva.
    </p>
</div>
""", unsafe_allow_html=True)

# Sección de análisis bursátil con datos dinámicos
st.markdown("## 💹 Análisis del Desempeño Bursátil de la Emisora")

# Gráfico interactivo con selección de tipo
if chart_type == "Gráfico de Línea":
    fig1 = px.line(price_data, x='Fecha', y='Precio Acción ($MXN)', 
                  title=f'Desempeño de la Acción - {analysis_period}',
                  labels={'Precio Acción ($MXN)': 'Precio ($MXN)'})
elif chart_type == "Gráfico de Barras":
    fig1 = px.bar(price_data, x='Fecha', y='Precio Acción ($MXN)', 
                 title=f'Desempeño de la Acción - {analysis_period}',
                 labels={'Precio Acción ($MXN)': 'Precio ($MXN)'})
else:
    fig1 = px.area(price_data, x='Fecha', y='Precio Acción ($MXN)', 
                  title=f'Desempeño de la Acción - {analysis_period}',
                  labels={'Precio Acción ($MXN)': 'Precio ($MXN)'})

# Añadir anotaciones si está seleccionado
if show_annotations:
    max_price = price_data['Precio Acción ($MXN)'].max()
    min_price = price_data['Precio Acción ($MXN)'].min()
    max_date = price_data.loc[price_data['Precio Acción ($MXN)'].idxmax(), 'Fecha']
    min_date = price_data.loc[price_data['Precio Acción ($MXN)'].idxmin(), 'Fecha']
    
    fig1.add_annotation(x=max_date, y=max_price,
                       text=f"Máximo: {max_price:.2f}",
                       showarrow=True,
                       arrowhead=1)
    fig1.add_annotation(x=min_date, y=min_price,
                       text=f"Mínimo: {min_price:.2f}",
                       showarrow=True,
                       arrowhead=1)

# Añadir bandas de confianza si está seleccionado
if show_confidence:
    price_data['MA_20'] = price_data['Precio Acción ($MXN)'].rolling(window=20).mean()
    price_data['Upper'] = price_data['MA_20'] + price_data['Precio Acción ($MXN)'].rolling(window=20).std()
    price_data['Lower'] = price_data['MA_20'] - price_data['Precio Acción ($MXN)'].rolling(window=20).std()
    
    fig1.add_trace(go.Scatter(
        x=price_data['Fecha'],
        y=price_data['Upper'],
        line=dict(color='rgba(0,0,0,0)'),
        showlegend=False,
        name='Banda Superior'
    ))
    
    fig1.add_trace(go.Scatter(
        x=price_data['Fecha'],
        y=price_data['Lower'],
        line=dict(color='rgba(0,0,0,0)'),
        fill='tonexty',
        fillcolor='rgba(52, 152, 219, 0.2)',
        showlegend=False,
        name='Banda Inferior'
    ))

fig1.update_layout(
    hovermode="x unified",
    xaxis_title="Fecha",
    yaxis_title="Precio ($MXN)",
    height=500
)
st.plotly_chart(fig1, use_container_width=True)

# Sección: Evaluación fondo de recompra con análisis interactivo
st.markdown("## 🔄 Evaluación del Fondo de Recompra")

# Slider para simular diferentes escenarios de recompra
buyback_percentage = st.slider(
    "Porcentaje de acciones para recompra simulada",
    0.0, 10.0, 5.0, 0.5,
    help="Simula el impacto en el precio según diferentes porcentajes de recompra"
)

price_data['Recompra Impacto (%)'] = (price_data['Precio Acción ($MXN)'].pct_change().rolling(window=5).mean() * 100 * 
                                    (1 + buyback_percentage/10))

fig2 = make_subplots(specs=[[{"secondary_y": True}]])

# Añadir trazas según tipo de gráfico seleccionado
if chart_type == "Gráfico de Línea":
    fig2.add_trace(
        go.Scatter(x=price_data['Fecha'], y=price_data['Precio Acción ($MXN)'], 
                  name="Precio Acción", line=dict(color='#3498db')),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=price_data['Fecha'], y=price_data['Recompra Impacto (%)'], 
                  name="Impacto Recompra (%)", line=dict(color='#e74c3c')),
        secondary_y=True,
    )
elif chart_type == "Gráfico de Barras":
    fig2.add_trace(
        go.Bar(x=price_data['Fecha'], y=price_data['Precio Acción ($MXN)'], 
               name="Precio Acción", marker_color='#3498db'),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Bar(x=price_data['Fecha'], y=price_data['Recompra Impacto (%)'], 
               name="Impacto Recompra (%)", marker_color='#e74c3c'),
        secondary_y=True,
    )
else:
    fig2.add_trace(
        go.Scatter(x=price_data['Fecha'], y=price_data['Precio Acción ($MXN)'], 
                  name="Precio Acción", fill='tozeroy', line=dict(color='#3498db')),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=price_data['Fecha'], y=price_data['Recompra Impacto (%)'], 
                  name="Impacto Recompra (%)", fill='tozeroy', line=dict(color='#e74c3c')),
        secondary_y=True,
    )

fig2.update_layout(
    title=f"Impacto Estimado de Recompra ({buyback_percentage}% de acciones) en Precio",
    xaxis_title="Fecha",
    yaxis_title="Precio ($MXN)",
    yaxis2_title="Impacto (%)",
    hovermode="x unified",
    height=500
)
st.plotly_chart(fig2, use_container_width=True)

# Sección: Inteligencia de mercado con filtros interactivos
st.markdown("## 📈 Análisis de Tendencias e Inteligencia de Mercado")

# Selector de sectores para análisis comparativo
selected_sectors = st.multiselect(
    "Seleccione sectores para comparar",
    ["Energía", "Químico", "Plásticos", "Empaque", "Textil", "Tecnología", "Salud", "Financiero"],
    default=["Químico", "Plásticos", "Empaque"]
)

# Generar datos dinámicos basados en selección
tendencias = pd.DataFrame({
    "Sector": selected_sectors,
    "Crecimiento Anual (%)": np.random.uniform(1.5, 6.0, len(selected_sectors)),
    "Margen EBITDA (%)": np.random.uniform(12, 25, len(selected_sectors))
})

# Gráfico de radar para comparación multidimensional
fig3 = go.Figure()

for i, sector in enumerate(tendencias["Sector"]):
    fig3.add_trace(go.Scatterpolar(
        r=[tendencias.loc[i, "Crecimiento Anual (%)"], 
           tendencias.loc[i, "Margen EBITDA (%)"]],
        theta=["Crecimiento Anual", "Margen EBITDA"],
        fill='toself',
        name=sector
    ))

fig3.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 30]
        )),
    showlegend=True,
    title="Comparativa de Sectores - Múltiples Métricas",
    height=500
)

st.plotly_chart(fig3, use_container_width=True)

# Sección: Datos financieros con capacidad de descarga
st.markdown("## 🧾 Datos Financieros Interactivos")

# Generar datos trimestrales con variabilidad
trimestres = ["Q1", "Q2", "Q3", "Q4"]
base_ingresos = 1200
base_costos = 800

datos_fin = pd.DataFrame({
    "Trimestre": trimestres * 2,
    "Tipo": ["Ingresos"] * 4 + ["Costos"] * 4,
    "Monto (M MXN)": [
        base_ingresos * (1 + np.random.uniform(-0.05, 0.1)),
        base_ingresos * (1 + np.random.uniform(-0.03, 0.12)),
        base_ingresos * (1 + np.random.uniform(-0.07, 0.08)),
        base_ingresos * (1 + np.random.uniform(-0.02, 0.15)),
        base_costos * (1 + np.random.uniform(-0.03, 0.08)),
        base_costos * (1 + np.random.uniform(-0.05, 0.1)),
        base_costos * (1 + np.random.uniform(-0.07, 0.07)),
        base_costos * (1 + np.random.uniform(-0.04, 0.09))
    ]
})

# Mostrar datos con estilo
styled_df = datos_fin.pivot(index="Trimestre", columns="Tipo", values="Monto (M MXN)")
styled_df["Utilidad"] = styled_df["Ingresos"] - styled_df["Costos"]
styled_df["Margen"] = (styled_df["Utilidad"] / styled_df["Ingresos"]) * 100

st.dataframe(
    styled_df.style
    .format("{:.1f}")
    .background_gradient(subset=["Margen"], cmap="RdYlGn")
    .highlight_max(subset=["Utilidad"], color="#27ae60")
    .highlight_min(subset=["Utilidad"], color="#e74c3c")
)

# Gráfico de cascada para flujo financiero
fig4 = go.Figure(go.Waterfall(
    name="Flujo Financiero",
    orientation="v",
    measure=["absolute", "relative", "relative", "relative", "total"],
    x=trimestres + ["Total"],
    y=[base_ingresos, 
       styled_df.loc["Q2", "Ingresos"] - styled_df.loc["Q1", "Ingresos"],
       styled_df.loc["Q3", "Ingresos"] - styled_df.loc["Q2", "Ingresos"],
       styled_df.loc["Q4", "Ingresos"] - styled_df.loc["Q3", "Ingresos"],
       0],
    connector={"line":{"color":"rgb(63, 63, 63)"}},
))

fig4.update_layout(
    title="Flujo de Ingresos Trimestral",
    showlegend=False,
    height=400
)

st.plotly_chart(fig4, use_container_width=True)

# Sección: Informe ejecutivo generativo
st.markdown("## 🧠 Informe Ejecutivo Automatizado")

# Selector de tipo de informe
report_type = st.radio(
    "Tipo de Informe",
    ["Resumen Ejecutivo", "Análisis Detallado", "Recomendaciones Estratégicas"],
    horizontal=True
)

# Helper function para formato de porcentaje
def format_percentage(value):
    return f"{value:.2f}%"

# Generar informe basado en selecciones
if report_type == "Resumen Ejecutivo":
    st.markdown(f"""
    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;">
        <h3 style="color:#2c3e50;">Resumen Ejecutivo - {analysis_period}</h3>
        <p>El análisis del período seleccionado muestra un <strong>rendimiento promedio del {format_percentage(rendimiento_promedio)}</strong>, 
        con una volatilidad del {format_percentage(volatilidad)}.</p>
        <p>La simulación de recompra del <strong>{buyback_percentage}%</strong> sugiere un impacto positivo potencial 
        del {format_percentage(price_data['Recompra Impacto (%)'].mean())} en el precio de la acción.</p>
        <p>Los sectores <strong>{tendencias.loc[tendencias['Crecimiento Anual (%)'].idxmax(), 'Sector']}</strong> 
        y <strong>{tendencias.loc[tendencias['Margen EBITDA (%)'].idxmax(), 'Sector']}</strong> presentan los mejores 
        indicadores de crecimiento y rentabilidad respectivamente.</p>
    </div>
    """, unsafe_allow_html=True)
    
elif report_type == "Análisis Detallado":
    st.markdown(f"""
    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;">
        <h3 style="color:#2c3e50;">Análisis Detallado - {analysis_period}</h3>
        <h4 style="color:#3498db;">Desempeño Bursátil</h4>
        <p>La acción mostró un rango de precios entre {price_data['Precio Acción ($MXN)'].min():.2f} MXN y 
        {price_data['Precio Acción ($MXN)'].max():.2f} MXN durante el período analizado, con una tendencia 
        {'alcista' if price_data['Precio Acción ($MXN)'].iloc[-1] > price_data['Precio Acción ($MXN)'].iloc[0] else 'bajista'} 
        general.</p>
        
        <h4 style="color:#3498db;">Impacto de Recompra</h4>
        <p>La estrategia de recompra del {buyback_percentage}% muestra correlación con mejoras en el desempeño, 
        particularmente en períodos de alta volatilidad. El impacto promedio estimado es del 
        {format_percentage(price_data['Recompra Impacto (%)'].mean())}.</p>
        
        <h4 style="color:#3498db;">Inteligencia de Mercado</h4>
        <p>El sector {tendencias.loc[tendencias['Crecimiento Anual (%)'].idxmax(), 'Sector']} lidera el crecimiento 
        con {format_percentage(tendencias['Crecimiento Anual (%)'].max())}, mientras que {tendencias.loc[tendencias['Margen EBITDA (%)'].idxmax(), 'Sector']} 
        presenta el mayor margen EBITDA con {format_percentage(tendencias['Margen EBITDA (%)'].max())}.</p>
    </div>
    """, unsafe_allow_html=True)
    
else:
    st.markdown(f"""
    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;">
        <h3 style="color:#2c3e50;">Recomendaciones Estratégicas</h3>
        <h4 style="color:#3498db;">Acciones Recomendadas</h4>
        <ul>
            <li>Considerar implementación de programa de recompra de acciones en el rango del {buyback_percentage-1:.1f}% al {buyback_percentage+1:.1f}%</li>
            <li>Diversificar exposición hacia el sector {tendencias.loc[tendencias['Crecimiento Anual (%)'].idxmax(), 'Sector']} para aprovechar tendencias de crecimiento</li>
            <li>Optimizar estructura de costos para alcanzar márgenes comparables a los del sector {tendencias.loc[tendencias['Margen EBITDA (%)'].idxmax(), 'Sector']}</li>
        </ul>
        
        <h4 style="color:#3498db;">Riesgos a Monitorear</h4>
        <ul>
            <li>Volatilidad del mercado actual: {format_percentage(volatilidad)}</li>
            <li>Presión competitiva en sectores con menor margen EBITDA</li>
            <li>Condiciones macroeconómicas que puedan afectar el crecimiento sectorial</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Sección de contacto profesional
st.markdown("---")
st.markdown("## 📞 Contacto Profesional")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;">
        <h3 style="color:#2c3e50;margin-top:0;">Javier Horacio Pérez Ricárdez</h3>
        <p><strong>Especialidad:</strong> Análisis Financiero y Planeación Estratégica</p>
        <p><strong>Correo:</strong> jahoperi@gmail.com</p>
        <p><strong>Teléfono:</strong> +52 56 1056 4095</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color:#f8f9fa;padding:20px;border-radius:10px;">
        <h3 style="color:#2c3e50;margin-top:0;">Conecta</h3>
        <p><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/javier-horacio-perez-ricardez-5b3a5777/" target="_blank">linkedin.com/in/tuperfil</a></p>
        <p><strong>Portafolio:</strong> <a href="https://kmagcap20251-yklkrgukwke2mnresypdsc.streamlit.app/" target="_blank">https://kmagcap20251-yklkrgukwke2mnresypdsc.streamlit.app/</a></p>
        <button style="background-color:#3498db;color:white;border:none;padding:8px 16px;border-radius:5px;cursor:pointer;">
            Solicitar Información
        </button>
    </div>
    """, unsafe_allow_html=True)

# Nota al pie
st.markdown("---")
st.markdown(f"""
<div style="text-align:center;color:#7f8c8d;font-size:14px;">
    <p>Portafolio interactivo desarrollado con Python | Última actualización: {datetime.now().strftime("%d/%m/%Y")}</p>
</div>
""", unsafe_allow_html=True)
