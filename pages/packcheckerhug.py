import streamlit as st
import PyPDF2
import requests
from fpdf import FPDF
import io
import os
from dotenv import load_dotenv
import pandas as pd
import time

# Load environment variables from .env file
load_dotenv()

# Configuration
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

def extract_text_from_pdf(file):
    """Extracts text from an uploaded PDF file."""
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def analyze_text(text, criteria):
    """Analyzes the extracted text against the given criteria using Zero-Shot Classification."""
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    results = []
    for criterion in criteria:
        payload = {
            "inputs": text,
            "parameters": {
                "candidate_labels": [criterion],
                "hypothesis_template": "This text is related to {}."
            },
        }
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()

            # Extract the label and score for this specific criterion
            if isinstance(result, dict) and 'labels' in result and 'scores' in result:
                label = result['labels'][0]
                score = result['scores'][0]
                results.append((criterion, label, score))
            else:
                st.error(f"Unexpected response structure for criterion: {criterion}")
                results.append((criterion, "Erreur", 0))
        except requests.exceptions.RequestException as e:
            st.error(f"Error analyzing criterion: {criterion}. Error: {str(e)}")
            results.append((criterion, "Erreur", 0))
    
    return results

def generate_pdf_report(results):
    """Generates a PDF report from the analysis results."""
    try:
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
    
    except Exception as e:
        st.error(f"An error occurred while generating the PDF: {e}")
        raise  # Re-raise the error for further debugging

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(page_title="Analyseur de Déclaration d'Alimentarité", page_icon="🍽️", layout="wide")
    st.title("Analyseur de Déclaration d'Alimentarité")

    # Define the criteria for analysis
    criteria = [
        "0.1. Titre explicatif «Déclaration de conformité» ou autre existant",
        "0.2. Titre = «Déclaration de conformité»",
        "1.1. L'identité et l'adresse de l'émetteur sont indiquées",
        "1.2. L'identité et l'adresse du destinataire sont indiquées",
        "11.3. Indications sur des documents de validation du travail de conformité effectué par des laboratoires tiers disponibles"
    ]

    # Upload PDF file
    uploaded_file = st.file_uploader("Choisissez votre déclaration d'alimentarité (PDF)", type="pdf")
    
    if uploaded_file is not None:
        # Extract text from the PDF
        text = extract_text_from_pdf(uploaded_file)
        
        # Analyze the text
        if st.button("Analyser"):
            with st.spinner("Analyse en cours..."):
                results = analyze_text(text, criteria)
            
            # Display the results
            if results:
                st.subheader("Résultats de l'analyse")
                
                # Create a DataFrame from the results
                df = pd.DataFrame(results, columns=["Critère", "Résultat", "Score"])
                
                # Display the DataFrame
                st.dataframe(df.style.format({"Score": "{:.2f}"}))
                
                # Generate and provide PDF report download
                pdf_report = generate_pdf_report(results)
                st.download_button(
                    label="Télécharger le rapport PDF",
                    data=pdf_report,
                    file_name="rapport_analyse.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("L'analyse n'a pas produit de résultats. Veuillez vérifier le contenu du PDF et réessayer.")

if __name__ == "__main__":
    main()

