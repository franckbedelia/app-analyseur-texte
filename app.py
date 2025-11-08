# app.py
import streamlit as st

st.set_page_config(page_title="Analyseur de Texte", page_icon="📊")

st.title("📊 Analyseur de Texte Intelligent")

text = st.text_area("Entrez votre texte ici:", height=200)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Compter les mots"):
        words = len(text.split())
        st.metric("Nombre de mots", words)

with col2:
    if st.button("Compter les caractères"):
        chars = len(text)
        st.metric("Nombre de caractères", chars)

with col3:
    if st.button("Mettre en majuscules"):
        st.text_area("Résultat:", text.upper(), height=200)
