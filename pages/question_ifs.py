import streamlit as st
import pandas as pd
from collections import Counter
from groq import Groq
import bcrypt

# URL of the CSV file from GitHub
CSV_URL = "https://raw.githubusercontent.com/M00N69/Action-planGroq/main/Guide%20Checklist_IFS%20Food%20V%208%20-%20CHECKLIST.csv"

# Liste simple de mots vides (à adapter selon vos besoins)
STOPWORDS = set(["a", "and", "the", "is", "in", "it", "of", "for", "on", "with", "as", "to", "at", "by"])

@st.cache(allow_output_mutation=True)
def load_csv_data(url):
    """Load the CSV data from the provided URL."""
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Erreur lors du chargement des données CSV: {str(e)}")
        return None

def identify_theme_without_nltk(question, top_n=5):
    """Identify main themes without using NLTK."""
    # Tokenize by splitting the string by spaces
    words = question.lower().split()
    
    # Remove stopwords
    filtered_words = [word for word in words if word.isalnum() and word not in STOPWORDS]
    
    # Count word frequencies
    word_counts = Counter(filtered_words)
    
    # Get the top N keywords
    keywords = [word for word, count in word_counts.most_common(top_n)]
    
    return keywords

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

        # Afficher les noms des colonnes pour le débogage
        st.write("Noms des colonnes disponibles dans le CSV:")
        st.write(df.columns.tolist())

        # Get user input
        question = st.text_input("Posez votre question:")

        if question:
            with st.spinner("Identification du thème et recherche dans la base de données..."):
                themes = identify_theme_without_nltk(question)
                
                # Vérifier si la colonne 'IFS Requirements' existe
                if 'IFS Requirements' not in df.columns:
                    st.error("La colonne 'IFS Requirements' n'existe pas dans le fichier CSV.")
                else:
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

