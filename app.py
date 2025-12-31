import streamlit as st

st.set_page_config(page_title="Titu Bhaiya & Soni Didi 10th Anniversary 💖", layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {padding: 0;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

st.markdown(html, unsafe_allow_html=True)
