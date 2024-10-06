import streamlit as st
import requests
from pocketgroq import GroqProvider
import base64

# CSS pour personnaliser le style de l'application
def add_custom_css():
    st.markdown("""
        <style>
        .main {
            max-width: 1200px;
            margin: 0 auto;
        }
        .stTextInput label {
            font-size: 20px;
            font-weight: bold;
        }
        .stTextInput input {
            font-size: 20px;
        }
        .custom-question {
            font-size: 28px;
            font-weight: bold;
            color: #333;
        }
        </style>
        """, unsafe_allow_html=True)

# Initialize Groq Client
def get_groq_client():
    """Initialize and return a Groq client with the API key."""
    return GroqProvider(api_key=st.secrets["GROQ_API_KEY"])

# Ask Groq to generate questions based on user's input
def ask_groq_for_questions(prompt: str):
    """Generate context-specific questions dynamically using the Groq model."""
    groq_client = get_groq_client()
    request_prompt = (
        f"L'utilisateur a décrit le problème suivant : {prompt}. "
        f"Génère des questions spécifiques pour analyser et comprendre plus en détail ce problème."
    )
    response = groq_client.generate(
        prompt=request_prompt,
        model="llama-3.1-70b-versatile",  # Modèle utilisé par défaut
        temperature=0.5,  
        max_tokens=500
    )
    questions = response.split('\n')
    filtered_questions = [q.strip() for q in questions if '?' in q]
    return filtered_questions[:5]  # Limiter à 5 questions

# Ask Groq for root cause analysis and recommendations
def ask_groq_for_analysis(problem_description: str, answers: list):
    """Analyze the problem and propose corrective actions based on answers and situation."""
    groq_client = get_groq_client()
    questions_and_answers = "\n".join([f"Question: {q}\nRéponse: {r}" for q, r in answers])
    prompt = f"Situation décrite : {problem_description}. \nRéponses aux questions : \n{questions_and_answers}\n Propose une analyse des causes racines avec des actions correctives."
    return groq_client.generate(prompt, model="llama-3.1-70b-versatile", temperature=0.7, max_tokens=1500)

# Générer un fichier téléchargeable au format .txt
def generate_download_button(content: str, filename: str):
    """Generate a download link for the analysis and action plan in a text file."""
    b64_content = base64.b64encode(content.encode()).decode()  # Convertir le contenu en base64
    href = f'<a href="data:file/txt;base64,{b64_content}" download="{filename}">Télécharger l\'analyse et le plan d\'action</a>'
    st.markdown(href, unsafe_allow_html=True)

# Main application function
def main():
    st.set_page_config(layout="wide")  # Activer le mode "wide"
    add_custom_css()  # Appliquer le CSS personnalisé

    st.title("Analyse de Cause Source - Sécurité des denrées alimentaires")

    # Explication pour l'utilisateur
    with st.expander("Comment utiliser cette application ?", expanded=True):
        st.write("""
        1. Décrivez votre problématique en lien avec la sécurité des denrées alimentaires.
        2. L'application générera automatiquement des questions spécifiques pour vous aider à approfondir l'analyse.
        3. Répondez aux questions posées.
        4. Cliquez sur le bouton "Soumettre" pour générer une analyse des causes racines et un plan d'action.
        5. Vous pourrez télécharger votre analyse sous forme de fichier texte après soumission.
        """)

    # User's problem input
    st.write("Présentez votre problématique, non-conformité ou situation en lien avec la sécurité des denrées alimentaires.")
    problem_description = st.text_area("Décrivez la situation ici...")

    # Bouton pour soumettre la description de la situation avant de générer des questions
    if st.button("Soumettre la situation"):
        if problem_description:
            # Step 1: Generate Dynamic Questions
            if 'questions' not in st.session_state:
                st.session_state.questions = ask_groq_for_questions(problem_description)
                st.session_state.answers = []
        else:
            st.warning("Veuillez décrire la situation avant de soumettre.")

    # Si la situation a été soumise, afficher les questions
    if 'questions' in st.session_state:
        st.write("Répondez aux questions ci-dessous pour affiner l'analyse :")
        for i, question in enumerate(st.session_state.questions):
            answer = st.text_input(f"Question {i+1}: {question}", key=f"answer_{i}")
            if answer and len(st.session_state.answers) == i:
                st.session_state.answers.append(answer)

        # Step 2: Submit button
        if st.button("Soumettre l'analyse"):
            if len(st.session_state.answers) == len(st.session_state.questions):
                # Step 3: Perform root cause analysis
                analysis_response = ask_groq_for_analysis(problem_description, list(zip(st.session_state.questions, st.session_state.answers)))
                st.write("### Analyse des causes racines et Plan d'action")
                st.write(analysis_response)

                # Step 4: Action Plan and download option
                causes_and_actions = [
                    {"Cause": "Manque de formation", "Action Proposée": "Organiser une formation sur les bonnes pratiques", "Gravité": 8, "Probabilité": 7, "Priorité": "Haute"},
                    {"Cause": "Processus mal défini", "Action Proposée": "Mettre à jour les SOPs et effectuer des audits réguliers", "Gravité": 9, "Probabilité": 6, "Priorité": "Très Haute"},
                    {"Cause": "Communication insuffisante", "Action Proposée": "Améliorer la communication entre les équipes et les services", "Gravité": 6, "Probabilité": 5, "Priorité": "Moyenne"}
                ]

                st.table(causes_and_actions)

                # Convert the analysis and action plan to text and create a download button
                full_analysis = f"Analyse des causes racines:\n{analysis_response}\n\nPlan d'action:\n" + "\n".join(
                    [f"Cause: {item['Cause']} - Action Proposée: {item['Action Proposée']} (Gravité: {item['Gravité']}, Probabilité: {item['Probabilité']}, Priorité: {item['Priorité']})" for item in causes_and_actions]
                )
                generate_download_button(full_analysis, "analyse_cause_source_et_plan_action.txt")
            else:
                st.warning("Veuillez répondre à toutes les questions avant de soumettre l'analyse.")

# Launch the application
if __name__ == "__main__":
    main()

