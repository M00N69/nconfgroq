import streamlit as st
import PyPDF2
import requests
from fpdf import FPDF
import io
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Configuration
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def analyze_text(text, criteria):
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    results = []
    for criterion in criteria:
        payload = {
            "inputs": f"Premise: {text}\nHypothesis: {criterion}",
            "parameters": {"candidate_labels": ["Conforme", "Non conforme", "Partiellement conforme"]},
            "options": {"wait_for_model": True}
        }
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            label = result['labels'][0]
            score = result['scores'][0]
            results.append((criterion, label, score))
        except requests.exceptions.RequestException as e:
            st.error(f"Error analyzing criterion: {criterion}. Error: {str(e)}")
            results.append((criterion, "Erreur", 0))
    
    return results

def generate_pdf_report(results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", size=16)
    pdf.cell(200, 10, txt="Rapport d'Analyse de Déclaration d'Alimentarité", ln=1, align='C')
    pdf.set_font("Arial", size=10)
    
    pdf.cell(100, 10, txt="Critère", border=1)
    pdf.cell(50, 10, txt="Résultat", border=1)
    pdf.cell(40, 10, txt="Score", border=1)
    pdf.ln()
    
    for criterion, label, score in results:
        pdf.multi_cell(100, 10, txt=criterion, border=1)
        pdf.cell(50, 10, txt=label, border=1)
        pdf.cell(40, 10, txt=f"{score:.2f}", border=1)
        pdf.ln()
    
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output

def main():
    st.set_page_config(page_title="Analyseur de Déclaration d'Alimentarité", page_icon="🍽️", layout="wide")
    st.title("Analyseur de Déclaration d'Alimentarité")

    criteria = [
        "0.1. Titre explicatif «Déclaration de conformité» ou autre existant",
        "0.2. Titre = «Déclaration de conformité»",
        "1.1. L'identité et l'adresse de l'émetteur sont indiquées",
        "1.2. L'identité et l'adresse du destinataire sont indiquées",
        # Add all other criteria here
        "11.3. Indications sur des documents de validation du travail de conformité effectué par des laboratoires tiers disponibles"
    ]

    uploaded_file = st.file_uploader("Choisissez votre déclaration d'alimentarité (PDF)", type="pdf")
    
    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)
        
        if st.button("Analyser"):
            with st.spinner("Analyse en cours..."):
                results = analyze_text(text, criteria)
            
            st.subheader("Résultats de l'analyse")
            
            df = pd.DataFrame(results, columns=["Critère", "Résultat", "Score"])
            st.dataframe(df.style.format({"Score": "{:.2f}"}))
            
            pdf_report = generate_pdf_report(results)
            st.download_button(
                label="Télécharger le rapport PDF",
                data=pdf_report,
                file_name="rapport_analyse.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    main()
