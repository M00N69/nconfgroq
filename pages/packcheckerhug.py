import streamlit as st
import PyPDF2
import requests
from fpdf import FPDF
import io
import os
from dotenv import load_dotenv
import time

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Configuration
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"  # Use the API URL

def extract_text_from_pdf(file):
    """Extrait le texte d'un fichier PDF téléchargé."""
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def analyze_text(text, criteria):
    """Analyse le texte extrait par rapport aux critères donnés en utilisant la classification Zero-Shot."""
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    results = []

    for criterion in criteria:
        payload = {
            "inputs": {
                "question": criterion,  # Use "question" as input key
                "context": text 
            }
        }
        try:
            # Ajout d'un délai pour éviter les erreurs dues à des requêtes trop rapides
            time.sleep(2)

            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()  # Raise error if API call fails
            result = response.json()

            # Extract answer and score
            answer = result['answer']
            score = result['score']
            
            # Classify based on score (adjust threshold as needed)
            label = "Entailment" if score > 0.5 else "Contradiction"
            results.append((criterion, label, score))

        except requests.exceptions.RequestException as e:
            st.error(f"Erreur lors de l'analyse du critère : {criterion}. Erreur : {str(e)}")
            results.append((criterion, "Erreur", 0))

    return results

def generate_pdf_report(results):
    """Génère un rapport PDF à partir des résultats d'analyse."""
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
            pdf.cell(100, 10, txt=criterion, border=1)
            pdf.cell(50, 10, txt=label, border=1)
            pdf.cell(40, 10, txt=f"{score:.2f}", border=1)
            pdf.ln()
        
        pdf_output = io.BytesIO()
        pdf.output(pdf_output, 'S').encode('latin1')  # Sauvegarder dans BytesIO
        pdf_output.seek(0)
        return pdf_output
    
    except Exception as e:
        st.error(f"Une erreur est survenue lors de la génération du PDF : {e}")
        raise  # Relancer l'erreur pour un débogage plus approfondi

def display_results_table(results):
    """Affiche les résultats sous forme de tableau formaté."""
    table_md = "| **Critère** | **Résultat** | **Score** |\n"
    table_md += "|-------------|--------------|-----------|\n"
    
    for criterion, label, score in results:
        table_md += f"| {criterion} | {label} | {score:.2f} |\n"
    
    st.markdown(table_md)

def main():
    """Fonction principale pour exécuter l'application Streamlit."""
    st.set_page_config(page_title="Analyseur de Déclaration d'Alimentarité", page_icon="🍽️", layout="wide")
    st.title("Analyseur de Déclaration d'Alimentarité")

    # Définir les critères pour l'analyse
    criteria = [
        "Le titre indique clairement qu'il s'agit d'une Déclaration de conformité",
        "L'identité et l'adresse de l'émetteur sont indiquées",
        "L'identité et l'adresse du destinataire sont indiquées",
        "Des documents de validation du travail de conformité sont fournis"
    ]

    # Téléchargement du fichier PDF
    uploaded_file = st.file_uploader("Choisissez votre déclaration d'alimentarité (PDF)", type="pdf")
    
    if uploaded_file is not None:
        # Extraire le texte du PDF
        text = extract_text_from_pdf(uploaded_file)
        
        # Analyser le texte
        if st.button("Analyser"):
            with st.spinner("Analyse en cours..."):
                results = analyze_text(text, criteria)
            
            # Afficher les résultats sous forme de tableau
            if results:
                st.subheader("Résultats de l'analyse")
                display_results_table(results)
                
                # Générer et fournir le téléchargement du rapport PDF
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




