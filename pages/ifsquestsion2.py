import streamlit as st
import requests
from groq import Groq
import bcrypt
import tiktoken
from fuzzywuzzy import fuzz
from cachetools import TTLCache

# Configuration
MAX_CONTEXT_CHUNKS = 3  # Nombre maximum de chunks à inclure dans le contexte
MAX_TOKENS_PER_CHUNK = 2000
CACHE_TTL = 86400  # Durée de vie du cache en secondes (1 jour)

# Placeholder pour document textuel supplémentaire
long_text_placeholder = """
1 Governance and commitment
1.1 Policy
1.1.1* The senior management shall develop, implement and maintain a corporate policy, which shall
include, at a minimum:
• food safety, product quality, legality and authenticity
• customer focus
• food safety culture
• sustainability.
This corporate policy shall be communicated to all employees and shall be broken down into
specific objectives for the relevant departments.
Objectives about food safety culture shall include, at a minimum, communication about food safety
policies and responsibilities, training, employee feedback on food safety related issues and performance measurement.
"""

# Cache pour les documents
document_cache = TTLCache(maxsize=10, ttl=CACHE_TTL)

def login(username, password):
    """Authentifie l'utilisateur avec bcrypt."""
    try:
        user_dict = st.secrets["users"]
        if username in user_dict and bcrypt.checkpw(password.encode('utf-8'), user_dict[username].encode('utf-8')):
            st.session_state["logged_in"] = True
            st.success("Accès autorisé! Vous pouvez accéder à la page.")
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")
    except KeyError:
        st.error("Les informations d'identification de l'utilisateur ne sont pas correctement configurées dans les secrets.")
    except Exception as e:
        st.error(f"Une erreur s'est produite: {str(e)}")

def secure_page():
    """Affiche la page sécurisée pour les utilisateurs connectés."""
    st.title("Questions IFS - Page sécurisée")
    if st.session_state.get("logged_in"):
        st.write("Vous êtes connecté!")
        st.warning("Contenu sécurisé ici.")

        documents = load_documents()

        if documents:
            user_input = st.text_area("Posez votre question ici:", height=300)
            if st.button("Envoyer"):
                with st.spinner('Génération de la réponse en cours...'):
                    response = generate_response(user_input, documents)
                    st.write(response)
        else:
            st.error("Échec du chargement des documents, impossible de continuer.")

    else:
        st.warning("Veuillez vous connecter pour accéder à cette page.")

def get_groq_client():
    """Initialise et renvoie un client Groq avec la clé API."""
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

@st.cache(allow_output_mutation=True, ttl=CACHE_TTL)
def load_documents():
    """Charge les documents à partir des URLs fournies."""
    urls = [
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFSV8.txt",
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFS_Food_v8_audit_checklist_guideline_v1_EN_1706090430.txt"
    ]
    documents = []
    for url in urls:
        try:
            if url in document_cache:
                document = document_cache[url]
            else:
                response = requests.get(url)
                response.raise_for_status()  # Vérification du code d'état
                document = response.text
                document_cache[url] = document
            documents.append(document)
        except requests.exceptions.RequestException as e:
            st.error(f"Échec du chargement du document depuis: {url}. Erreur: {str(e)}")

    # Ajout du contenu textuel supplémentaire
    documents.append(long_text_placeholder)
    return documents

def chunk_text(text, max_tokens=MAX_TOKENS_PER_CHUNK):
    """Découpe le texte en chunks avec un nombre maximum de tokens."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokens = encoding.encode(text)
    chunks = []
    current_chunk = []

    for token in tokens:
        current_chunk.append(token)
        if len(current_chunk) >= max_tokens:
            chunks.append(encoding.decode(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(encoding.decode(current_chunk))
    return chunks

def generate_response(user_input, documents):
    """Génère une réponse à la requête de l'utilisateur."""
    client = get_groq_client()

    system_instruction = """
    Utilisez exclusivement les informations du contexte fourni, en particulier les documents chargés, pour générer des réponses. Les réponses doivent être en français, basées uniquement sur les données fournies sans extrapolation. Aucun lien externe ou référence directe à des sources non incluses dans les documents ne doit être utilisé. Vérifiez la précision des clauses mentionnées par rapport au fichier ifsv8.txt en utilisant les autres documents comme références complémentaires.
    """

    # Recherche des documents pertinents
    relevant_documents = search_relevant_documents(user_input, documents)

    # Construction du contexte
    messages = [
        {"role": "user", "content": user_input},
        {"role": "system", "content": system_instruction}
    ]
    for _, doc in relevant_documents:
        messages.append({"role": "assistant", "content": doc})

    total_tokens = 0
    for message in messages:
        total_tokens += len(tiktoken.encoding_for_model("gpt-3.5-turbo").encode(message['content']))

    # Choix du modèle en fonction du nombre de tokens
    model_id = "mixtral-8x7b-32768" if total_tokens <= 32000 else "llama3-8b-8192"

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model_id
    )

    return chat_completion.choices[0].message.content

def search_relevant_documents(question, documents):
    """Recherche les documents les plus pertinents à l'aide de fuzzywuzzy."""
    scores = []
    for doc in documents:
        score = fuzz.ratio(question, doc)
        scores.append((score, doc))

    # Trier les documents par score de similarité décroissant
    scores.sort(key=lambda x: x[0], reverse=True)
    return scores[:MAX_CONTEXT_CHUNKS]

def main():
    """Fonction principale de l'application Streamlit."""
    st.title("Question sur les normes IFS v8")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        # Section de connexion
        st.subheader("Section de connexion:")
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        if st.button("Connexion"):
            login(username, password)
    else:
        # Page sécurisée
        secure_page()

if __name__ == "__main__":
    main()
