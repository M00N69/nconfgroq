import streamlit as st
import requests
from groq import Groq  # Import the Groq API client assuming this is a valid import

def get_groq_client():
    """Initialize and return a Groq client with the API key."""
    return groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    """Load documents from specified URLs and handle errors."""
    urls = [
        "https://raw.githubusercontent.com/m00n69/nconfgroq/main/ifs_food_v8_audit_checklist_guideline_v1_en_1706090430.txt"
    ]
    documents = []
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                documents.append(response.text)
            else:
                st.error(f"Failed to load document from: {url}. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Failed to load document from: {url}. Error: {e}")
    if not documents:
        st.error("No documents loaded successfully.")
    return documents

def generate_response(user_input, documents):
    """Generate a response to user query using Groq and loaded documents."""
    # Create a Groq client
    client = get_groq_client()

    # Configure request parameters
    system_instruction = """
    Utilisez exclusivement les informations du contexte fourni, en particulier les documents chargés, pour générer des réponses. Les réponses doivent être en français, basées uniquement sur les données fournies sans extrapolation. Aucun lien externe ou référence directe à des sources non incluses dans les documents ne doit être utilisé. Vérifiez la précision des clauses mentionnées par rapport au fichier ifsv8.txt en utilisant les autres documents comme références complémentaires.
    """

    # Create messages for Groq query
    messages = [
        {"role": "user", "content": user_input},
        {"role": "system", "content": system_instruction}
    ]
    # Add each document as a separate message
    for doc in documents:
        messages.append({"role": "assistant", "content": doc})

    # Send request to Groq
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192"  # Use an appropriate model
    )
    return chat_completion.choices[0].message.content

def main():
    """Streamlit UI for interacting with the chat system."""
    st.title("Question sur les normes IFS v8")
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
