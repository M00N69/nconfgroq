import streamlit as st
import pandas as pd
from groq import Groq
import bcrypt
import spacy

# URL of the CSV file from GitHub
CSV_URL = "https://raw.githubusercontent.com/M00N69/Action-planGroq/main/Guide%20Checklist_IFS%20Food%20V%208%20-%20CHECKLIST.csv"

# Load the spaCy model for NLP processing
nlp = spacy.load("en_core_web_sm")

@st.cache(allow_output_mutation=True)
def load_csv_data(url):
    """Load the CSV data from the provided URL."""
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Erreur lors du chargement des données CSV: {str(e)}")
        return None

def identify_theme(question):
    """Identify the main theme of the question using spaCy."""
    doc = nlp(question)
    # Extract the main nouns and proper nouns as potential themes
    themes = [chunk.text for chunk in doc.noun_chunks]
    return themes

def find_context_in_csv(themes, df):
    """Find relevant rows in the CSV based on identified themes."""
    # Search the "IFS Requirement" column for any of the themes
    matching_rows = df[df['IFS Requirement'].apply(lambda x: any(theme.lower() in str(x).lower() for theme in themes))]
    return matching_rows

def get_groq_client():
    """Initialize and return a Groq client with the API key."""
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_response_with_groq(client, question, context_snippets):
    """Generate a response using the Groq API based on the context from the CSV."""
    if not context_snippets.empty:
        combined_context = context_snippets.to_string(index=False)
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": question},
                {"role": "system", "content": combined_context}
            ],
            model="llama-3.1-8b-instant"  # Adapt the model to your needs
        )
        return response.choices[0].message.content
    else:
        return "Aucun contexte pertinent trouvé dans la base de données pour répondre à cette question."

def login(username, password):
    """Authenticate the user with bcrypt."""
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
    """Display the secure page for logged-in users."""
    st.title("Questions IFS v8 - Recherche et Réponse Automatisée")

    # Load CSV data
    df = load_csv_data(CSV_URL)

    if df is not None:
        st.write("Base de données IFSv8 chargée:")
        st.dataframe(df)

        # Get user input
        question = st.text_input("Posez votre question:")

        if question:
            with st.spinner("Identification du thème et recherche dans la base de données..."):
                themes = identify_theme(question)
                context_snippets = find_context_in_csv(themes, df)
                
                st.write("Contextes trouvés dans la base de données:")
                st.dataframe(context_snippets)

                if not context_snippets.empty:
                    # Initialize Groq client
                    client = get_groq_client()

                    # Generate the response using Groq API
                    response = generate_response_with_groq(client, question, context_snippets)
                    st.write("Réponse générée par Groq:")
                    st.write(response)
                else:
                    st.warning("Aucun contexte pertinent trouvé pour les thèmes extraits.")
    else:
        st.error("Impossible de charger la base de données CSV.")

def main():
    """Main function of the Streamlit app."""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        # Login section
        st.subheader("Section de connexion:")
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        if st.button("Connexion"):
            login(username, password)
    else:
        # Secure page
        secure_page()

if __name__ == "__main__":
    main()

