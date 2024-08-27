import requests
import streamlit as st


def buscarLetra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra


st.image("https://i.imgur.com/SmktDIH.png")
st.title("Letra da música")

banda = st.text_input("Nome da banda: ", key="banda")
musica = st.text_input("Nome da música: ", key="musica")
pesquisar = st.button("Pesquisar")

if pesquisar:
    letra = buscarLetra(banda, musica)
    if letra:
        st.success("Música encontrada com sucesso!")
        st.text(letra)
    else:
        st.error("Música não encontrada!")
