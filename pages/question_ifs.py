import streamlit as st
import requests
from groq import Groq

def get_groq_client():
    """Initialise et retourne un client Groq avec la clé API."""
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    """Charge les documents à partir des URLs spécifiées et gère les erreurs."""
    urls = [
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFS_Food_v8_audit_checklist_guideline_v1_EN_1706090430.txt"
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
    """Génère une réponse à la requête de l'utilisateur en utilisant Groq et les documents chargés."""
    # Créer un client Groq
    client = get_groq_client()

    # Configurer les paramètres de la requête
    system_instruction = """
    Utiliser exclusivement les informations du contexte fourni, en particulier les documents chargés, pour générer des réponses. Les réponses doivent être en français, basées uniquement sur les données fournies sans extrapolation. Aucun lien externe ou référence directe à des sources non incluses dans les documents ne doit être utilisé. Vérifier la précision des clauses mentionnées par rapport au fichier IFSV8.txt en utilisant les autres documents comme références complémentaires.
    """

    # Créer les messages pour la requête Groq
    messages = [
        {"role": "user", "content": user_input},
        {"role": "system", "content": system_instruction}
    ]
    # Ajouter chaque document comme un message séparé
    for doc in documents:
        messages.append({"role": "assistant", "content": doc})

    # Envoyer la requête à Groq
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192"  # Ou un autre modèle approprié
    )
    return chat_completion.choices[0].message.content

def main():
    """Interface utilisateur Streamlit pour l'interaction avec le système de chat."""
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
