import streamlit as st
from groq import Groq
import requests
from bs4 import BeautifulSoup

def get_groq_client():
    # Secure initialization of the Groq client using an API key
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    # Define the links to the documents
    links = [
        "https://docs.google.com/document/d/e/2PACX-1vSJUHS9LlgUzTb8mZf4eND5AZS9zZN8xCAoC-AM08JOvY6RrZeXpIuVzevxm3SXhvpuFLWLp0hJRC28/pub",
        "https://docs.google.com/document/d/e/2PACX-1vQ6aWiYGVW3j0njBm1wCb2MaEazsTYljLbABwXuhRwwwTa9AHUmvKiwwt7YQxQOihwi5ZkPu2gZMb85/pub",
        "https://docs.google.com/document/d/e/2PACX-1vQ7-byHFi82kkFWqZuWgkhcYu5UVNfcWuVxWuVjKbW94J3t-vQaZkt5cNzsOSZJxOUxCoMJ7CJgIb-X/pub"
    ]
    return links

def extract_info_from_link(link):
    # Extract relevant information from the link
    # For example, you can use BeautifulSoup to parse the HTML content of the link
    # and extract relevant information such as headings, paragraphs, and keywords
    soup = BeautifulSoup(requests.get(link).content, 'html.parser')
    title = soup.find('title').text
    paragraphs = [p.text for p in soup.find_all('p')]
    keywords = [a.text for a in soup.find_all('a')]
    return {'title': title, 'paragraphs': paragraphs, 'keywords': keywords}

def prioritize_response(response, link_info):
    # Use the extracted information to prioritize the response
    # For example, you can use a scoring system to prioritize the response based on the relevance of the link
    # to the user's question
    score = calculate_score(link_info, response)
    if score > 0.5:
        return response
    else:
        return "Sorry, I couldn't find a relevant response. Please try again."

def calculate_score(link_info, response):
    # Calculate a score based on the relevance of the link to the user's question
    # For example, you can use a library like NLTK to calculate the similarity between the link's content
    # and the user's question
    # The score can be used to prioritize the response
    return 0.8

def generate_response(user_input):
    # Combines user input with predefined system instructions
    system_instruction = """
    The response shall be in the same language than the user question. Response should be with more details possible   
    The response will use the provided documents but will not expose direct links or references.
    The model will aim to provide IFS V8 requirement references where applicable (only clause from IFS FOOD AUDIT CHECKLIST LIST OF IFS FOOD AUDIT REQUIREMENTS in the IFS_Food_v8_standard_EN_1711635033 .Suggest any other question around same subject
    """
    client = get_groq_client()
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_input},
            {"role": "system", "content": system_instruction}
        ],
        model="mixtral-8x7b-32768",
    )
    response = chat_completion.choices[0].message.content

    # Use the links as a reference to prioritize the response
    links = load_documents()
    for link in links:
        link_info = extract_info_from_link(link)
        response = prioritize_response(response, link_info)

    return response

def main():
    st.title("Question sur IFSv8...En cours de codage, merci pour votre patience")
    links = load_documents()
    if links:
        user_input = st.text_area("Posez votre question ici:", height=300)
        if st.button("Envoyer"):
            with st.spinner('Attendez pendant que nous générons la réponse...'):
                response = generate_response(user_input)
                st.write(response)

if __name__ == "__main__":
    main()
