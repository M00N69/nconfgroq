import streamlit as st
import requests
from groq import Groq
import bcrypt

# Configuration
MAX_CONTEXT_RADIUS = 200  # Nombre de caractères autour du mot clé pour le contexte

# Placeholder for additional document content
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

@st.cache(allow_output_mutation=True, ttl=86400)
def load_documents():
    """Charge les documents à partir des URLs fournies."""
    urls = [
        "https://raw.githubusercontent.com/M00N69/nconfgroq/main/IFSV8.txt"
    ]
    documents = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            documents.append(response.text)
        else:
            st.error(f"Échec du chargement du document depuis: {url}. Code d'état: {response.status_code}")
    if not documents:
        st.error("Aucun document chargé avec succès.")

    # Ajout du contenu textuel supplémentaire
    documents.append(long_text_placeholder)

    return "\n".join(documents)  # Retourner un seul texte combiné

def extract_keywords_from_groq(client, user_input):
    """Utilise l'API Groq pour extraire les mots clés de la question de l'utilisateur."""
    response = client.keywords.extract(text=user_input)
    return response['keywords']

def find_context_in_documents(documents, keywords):
    """Trouve le contexte autour des mots clés dans le document."""
    context_snippets = []
    for keyword in keywords:
        start_idx = documents.lower().find(keyword.lower())
        if start_idx != -1:
            start = max(0, start_idx - MAX_CONTEXT_RADIUS)
            end = min(len(documents), start_idx + len(keyword) + MAX_CONTEXT_RADIUS)
            context_snippets.append(documents[start:end])
    return context_snippets

def generate_response(user_input, documents):
    """Génère une réponse à la requête de l'utilisateur."""
    client = get_groq_client()

    # Étape 1 : Extraire les mots clés
    keywords = extract_keywords_from_groq(client, user_input)
    
    # Étape 2 : Rechercher les mots clés dans les documents
    context_snippets = find_context_in_documents(documents, keywords)
    
    # Étape 3 : Demander à Groq de générer une réponse basée sur le contexte trouvé
    if context_snippets:
        combined_context = "\n".join(context_snippets)
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input},
                {"role": "system", "content": combined_context}
            ],
            model="llama-3.1-8b-instant"  # Choisir un modèle adapté à la taille du contexte
        )
        return response.choices[0].message.content
    else:
        return "Aucun contexte pertinent trouvé pour les mots clés extraits."

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
