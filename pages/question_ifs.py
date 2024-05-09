import streamlit as st
import requests
from groq import Groq

def get_groq_client():
    """Initialize and return a Groq client with the API key."""
    return groq(api_key=st.secrets["groq_api_key"])

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents(uploaded_documents):
    if uploaded_documents:
        return uploaded_documents
    else:
        urls = [
            "https://raw.githubusercontent.com/m00n69/nconfgroq/main/ifs_food_v8_audit_checklist_guideline_v1_en_1706090430.txt"
        ]
        documents = []
        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                documents.append(response.text)
            else:
                st.error(f"Failed to load document from: {url}. Status code: {response.status_code}")
        if not documents:
            st.error("No documents loaded successfully.")
        return documents

def generate_response(user_input, documents):
    # Implementation as before

def main():
    st.title("Question sur les normes IFS v8")

    uploaded_files = st.file_uploader("Upload document file", type=["txt"], accept_multiple_files=False)

    if uploaded_files is not None:
        uploaded_documents = [file.read().decode("utf-8") for file in uploaded_files]
        st.success("Document uploaded successfully.")
    else:
        uploaded_documents = None

    documents = load_documents(uploaded_documents)

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
