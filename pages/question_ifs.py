import streamlit as st
import requests
from groq import Groq  # Assuming this is the correct import based on your Groq setup

# Initialize the Groq API client using an API key from Streamlit's secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def configure_model(document_text):
    # Assume the Groq model does not require explicit configuration before each use
    # Placeholder for any specific configuration steps, if necessary
    return document_text

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    url = "https://raw.githubusercontent.com/M00N69/nconfgroq/main/guideIFSV8.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        documents_text = response.text
    except requests.exceptions.HTTPError as e:
        st.error(f"Failed to download the document: {str(e)}")
        return None
    return documents_text

def generate_response(user_input, system_instruction):
    # Generating chat response using Groq API with detailed instruction
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_input},
            {"role": "system", "content": system_instruction}
        ],
        model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content

def main():
    st.title("Question sur IFSv8")
    document_text = load_documents()
    if document_text is not None:
        configure_model(document_text)

        user_input = st.text_area("Posez votre question ici:", height=300)
        if st.button("Envoyer"):
            with st.spinner('Attendez pendant que nous générons la réponse...'):
                response = generate_response(user_input, document_text)
                st.write(response)
    else:
        st.error("Error loading documents. Unable to proceed without document data.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

