from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon=":atom_symbol:",
    layout="wide",
    initial_sidebar_state="expanded"
)

css_file = Path(__file__).parent / "assets" / "style.css"

if css_file.exists():
    st.markdown(
        f"<style>{css_file.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

st.title("Sales Analytics Dashboard")

st.markdown(
    """
    Bem-vindo ao dashboard de análise de vendas.

    Utilize o menu lateral para navegar entre as análises disponíveis.
    """
)

st.info(
    "Selecione uma página no menu lateral para iniciar a análise."
)
