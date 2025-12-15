import streamlit as st
from transformers import pipeline
from io import BytesIO
import PyPDF2

st.title("Resumidor profesional de PDFs IA seguro")

# Selector de longitud de resumen
longitud = st.selectbox(
    "Selecciona la longitud del resumen:",
    ("Corto", "Medio", "Largo")
)

if longitud == "Corto":
    min_len, max_len = 20, 80
elif longitud == "Medio":
    min_len, max_len = 50, 150
else:
    min_len, max_len = 100, 250

# Usamos un modelo más ligero para evitar errores
summarizer = pipeline("summarization", model="t5-small")

# Dividir texto en bloques más pequeños
def dividir_texto(texto, max_palabras=300):
    palabras = texto.split()
    bloques = []
    for i in range(0, len(palabras), max_palabras):
        bloques.append(" ".join(palabras[i:i+max_palabras]))
    return bloques

def resumir_texto(texto):
    try:
        resumen = summarizer(texto, max_length=max_len, min_length=min_len, do_sample=False)
        return resumen[0]['summary_text']
    except Exception as e:
        st.error(f"Error al resumir un bloque: {e}")
        return ""

# Subida del PDF
archivo = st.file_uploader("Sube tu archivo PDF", type="pdf")

if st.button("Resumir PDF"):
    if archivo is not None:
        pdf_reader = PyPDF2.PdfReader(archivo)
        texto_pdf = ""
        for pagina in pdf_reader.pages:
            pagina_texto = pagina.extract_text()
            if pagina_texto:
                texto_pdf += pagina_texto + "\n"

        if not texto_pdf.strip():
            st.warning("El PDF no contiene texto legible para resumir.")
        else:
            bloques = dividir_texto(texto_pdf)
            resumen_final = ""
            for i, bloque in enumerate(bloques):
                st.info(f"Resumiendo bloque {i+1}/{len(bloques)}...")
                resumen_final += resumir_texto(bloque) + " "

            # Botón para descargar
            st.write("**Resumen final del PDF:**")
            st.write(resumen_final)
            resumen_bytes = BytesIO(resumen_final.encode('utf-8'))
            st.download_button(
                "Descargar resumen",
                data=resumen_bytes,
                file_name="resumen_seguro.txt",
                mime="text/plain"
            )
    else:
        st.warning("Por favor, sube un archivo PDF.")



# 1. Para iniciar la app hacer cd + ubicacion del archivo en la Terminal.
# 2. Introducir el comando :streamlit run resumidor.py
