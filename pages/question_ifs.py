import streamlit as st
import requests
from groq import Groq  # Import the Groq API client assuming this is a valid import

def get_groq_client():
    # Initialisation sécurisée du client Groq avec une clé API
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    # Définition des URL directs vers les fichiers .txt sur GitHub
    urls = [
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFS_Food_v8_audit_checklist_guideline_v1_EN_1706090430.txt",
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFS_Food_v8_doctrine_v1_EN_1687965517%20(2).txt",
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFS_Food_v8_standard_FR_1681804144%20(2).txt"
    ]
    documents = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            documents.append(response.text)
        else:
            st.error("Failed to load document from: " + url)
            documents.append("")  # Append an empty string in case of failure
    return documents

def prioritize_response(response, documents):
    # Simplified for demonstration
    return response  # Utiliser des critères de priorisation basés sur le contenu des documents

def generate_response(user_input):
    # Instruction système simplifiée
    system_instruction = """
    La réponse doit être en français sauf demande contraire. Fournir des réponses détaillées.
    Utiliser les documents fournis mais ne pas exposer de liens directs ou de références.
    Viser à fournir des références aux exigences IFS V8 où applicable, vérifier soigneusement que les numéro de clauses correspondent bien dans le standard IFSv8.
    """
    client = get_groq_client()
    documents = load_documents()
    # Simplification de la logique de réponse pour cette démonstration
    response = "Réponse basée sur l'analyse des documents chargés."
    return prioritize_response(response, documents)

def main():
    st.title("Question sur les normes IFS V8")
    if load_documents():
        user_input = st.text_area("Posez votre question ici:", height=300)
        if st.button("Envoyer"):
            with st.spinner('Génération de la réponse en cours...'):
                response = generate_response(user_input)
                st.write(response)

if __name__ == "__main__":
    main()
