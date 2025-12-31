import streamlit as st

st.set_page_config(page_title="Titu Bhaiya & Soni Didi 10th Anniversary", layout="wide")

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

st.components.v1.html(html_content, height=4000, scrolling=True)
