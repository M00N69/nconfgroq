import streamlit as st
import requests
from groq import Groq

def get_groq_client():
    # Initialisation sécurisée du client Groq avec une clé API
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    urls = [
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFS_Food_v8_audit_checklist_guideline_v1_EN_1706090430.txt",
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFS_Food_v8_doctrine_v1_EN_1687965517%20(2).txt",
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFS_Food_v8_standard_FR_1681804144%20(2).txt",
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFSV8.txt"
    ]
    documents = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            documents.append(response.text)
        else:
            st.error(f"Failed to load document from: {url}")
            return None
    return documents

def generate_response(user_input, documents):
    # Charger les documents
    documents_text = "\n".join(documents)

    # Créer un client Groq
    client = get_groq_client()

    # Configurer les paramètres de la requête
    system_instruction = "La réponse doit être en français sauf demande contraire. Fournir des réponses détaillées. En cas de références aux clauses de la norme utiliser uniquement le fichier IFSV8.txt. Utiliser les documents fournis mais ne pas exposer de liens directs ou de références."
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_input},
            {"role": "system", "content": system_instruction}
        ],
        model="mixtral-8x7b-32768"
    )
    return chat_completion.choices[0].message.content

def main():
    st.title("Question sur les normes IFS V8...En cours de codage, merci pour votre patience")
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
