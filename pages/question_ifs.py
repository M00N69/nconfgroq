import streamlit as st
import requests
from groq import Groq  # Assumant que cette importation est valide

def get_groq_client():
    # Initialisation sécurisée du client Groq avec une clé API
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
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
            st.error(f"Failed to load document from: {url}")
            return None  # Return None to indicate failure
    return documents

def generate_response(user_input, documents):
    # Combine user input with the loaded documents for processing
    combined_text = "\n".join(documents) + "\nUser Question: " + user_input
    system_instruction = """
    La réponse doit être en français sauf demande contraire. Fournir des réponses détaillées.
    Utiliser les documents fournis mais ne pas exposer de liens directs ou de références.
    Viser à fournir des références aux exigences IFS V8 où applicable, vérifier soigneusement que les numéro de clauses correspondent bien dans le standard IFSv8.
    """
    client = get_groq_client()
    # Assuming 'process_input' is a valid method for your Groq client; adjust as necessary
    response = client.process_input(combined_text, system_instruction)
    return response

def main():
    st.title("Question sur les normes IFS V8")
    documents = load_documents()
    if documents:
        user_input = st.text_area("Posez votre question ici:", height=300)
        if st.button("Envoyer"):
            with st.spinner('Génération de la réponse en cours...'):
                response = generate_response(user_input, documents)
                st.write(response)
    else:
        st.error("Document loading failed, cannot proceed.")

if __name__ == "__main__":
    main()
