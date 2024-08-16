import os
import io
import time
import requests
import PyPDF2
from fpdf import FPDF
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
API_URL = "https://api-inference.huggingface.co/models/typeform/distilbert-base-uncased-mnli"

# Agent pour l'extraction de texte
class TextExtractionAgent(Agent):
    def run(self, inputs):
        file = inputs.get('file')
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text

# Agent pour l'analyse de texte
class TextAnalysisAgent(Agent):
    def run(self, inputs):
        text = inputs.get('text')
        criteria = inputs.get('criteria')
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        results = []
        for criterion in criteria:
            hypothesis = f"{criterion}"
            payload = {
                "inputs": {"premise": text, "hypothesis": hypothesis},
                "parameters": {"candidate_labels": ["Entailment", "Neutral", "Contradiction"]}
            }
            try:
                time.sleep(2)
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status()
                result = response.json()
                entailment_score = result['scores'][0]
                results.append((criterion, "Entailment" if entailment_score > 0.5 else "Contradiction", entailment_score))
            except requests.exceptions.RequestException as e:
                results.append((criterion, "Erreur", 0))
        return results

# Agent pour la génération de rapport PDF
class ReportGenerationAgent(Agent):
    def run(self, inputs):
        results = inputs.get('results')
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
        pdf.output(pdf_output, 'S').encode('latin1')
        pdf_output.seek(0)
        return pdf_output

# Définir les tâches
text_extraction_task = Task(
    description="Extraire le texte d'un PDF",
    agent=TextExtractionAgent(),
    expected_output="Texte extrait"
)

text_analysis_task = Task(
    description="Analyser le texte extrait par rapport aux critères donnés",
    agent=TextAnalysisAgent(),
    expected_output="Résultats de l'analyse"
)

report_generation_task = Task(
    description="Générer un rapport PDF basé sur les résultats de l'analyse",
    agent=ReportGenerationAgent(),
    expected_output="Rapport PDF"
)

# Définir le crew
crew = Crew(
    agents=[TextExtractionAgent(), TextAnalysisAgent(), ReportGenerationAgent()],
    tasks=[text_extraction_task, text_analysis_task, report_generation_task],
    process=Process.sequential
)

def main():
    st.set_page_config(page_title="Analyseur de Déclaration d'Alimentarité", page_icon="🍽️", layout="wide")
    st.title("Analyseur de Déclaration d'Alimentarité")
    criteria = [
        "Le titre indique clairement qu'il s'agit d'une Déclaration de conformité",
        "L'identité et l'adresse de l'émetteur sont indiquées",
        "L'identité et l'adresse du destinataire sont indiquées",
        "Des documents de validation du travail de conformité sont fournis"
    ]
    uploaded_file = st.file_uploader("Choisissez votre déclaration d'alimentarité (PDF)", type="pdf")
    
    if uploaded_file is not None:
        if st.button("Analyser"):
            with st.spinner("Analyse en cours..."):
                result = crew.kickoff(inputs={'file': uploaded_file, 'criteria': criteria})
                pdf_report = result.get('Rapport PDF')
                st.download_button(
                    label="Télécharger le rapport PDF",
                    data=pdf_report,
                    file_name="rapport_analyse.pdf",
                    mime="application/pdf"
                )

if __name__ == "__main__":
    main()





