import streamlit as st
import requests
from groq import Groq

# Initialize the Groq API client using an API key from Streamlit's secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def configure_model(document_text):
    # Assume the Groq model does not require explicit configuration before each use
    # Placeholder for any specific configuration steps, if necessary
    return document_text

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    links = [
        "https://docs.google.com/document/d/e/2PACX-1vSJUHS9LlgUzTb8mZf4eND5AZS9zZN8xCAoC-AM08JOvY6RrZeXpIuVzevxm3SXhvpuFLWLp0hJRC28/pub",
        "https://docs.google.com/document/d/e/2PACX-1vQ79Mh2s7Fn1e8PDWzcEmZe9BlrsB97M_WZt-wy9zT4-mHrhNCvVdHYnZj1gC-sK6Kdqc2-YuSyEDb3/pub",
        "https://docs.google.com/document/d/e/2PACX-1vQ7-byHFi82kkFWqZuWgkhcYu5UVNfcWuVxWuVjKbW94J3t-vQaZkt5cNzsOSZJxOUxCoMJ7CJgIb-X/pub"
    ]
    return links

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
    st.title("Question sur IFSv8...En cours de codage , merci pour votre patience")
    links = load_documents()
    if links is not None:
        user_input = st.text_area("Posez votre question ici:", height=300)
        if st.button("Envoyer"):
            with st.spinner('Attendez pendant que nous générons la réponse...'):
                response = generate_response(user_input, " ".join(links))
                st.write(response)
    else:
        st.error("Error loading documents. Unable to proceed without document data.")

if __name__ == "__main__":
    main()
