import streamlit as st
import wikipedia

st.set_page_config(page_title="AI-Mythen Checker", layout="centered")

st.title("AI-Mythen Checker")
st.markdown(
    "Voer hieronder een bewering over AI in. "
    "De checker zoekt in Wikipedia en geeft een korte, feitelijke uitleg met bronnen."
)

claim = st.text_input("Bewering", placeholder="Voorbeeld: ‘AI gaat binnen vijf jaar alle banen overnemen’")

def zoek_uitleg(tekst: str) -> str:
    if not tekst.strip():
        return "⚠️ Vul eerst een bewering in."
    try:
        zoekresultaten = wikipedia.search(tekst, results=5, suggestion=False)
        if not zoekresultaten:
            return "Geen directe Wikipedia-hits gevonden. Probeer een andere formulering."
        pagina = wikipedia.page(zoekresultaten[0])
        samenvatting = wikipedia.summary(pagina.title, sentences=5)
        uitleg = (
            f"### Gevonden artikel: **{pagina.title}**\n\n"
            f"{samenvatting}\n\n"
            f"Bron: {pagina.url}"
        )
        return uitleg
    except Exception as e:
        return f"Er ging iets mis: {e}"

if st.button("Check bewering"):
    st.markdown(zoek_uitleg(claim), unsafe_allow_html=True)
