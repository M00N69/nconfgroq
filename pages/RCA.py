import streamlit as st
import requests
from pocketgroq import GroqProvider
import base64

# CSS pour personnaliser le style de l'application, incluant une plus grande police pour les questions
def add_custom_css():
    st.markdown("""
        <style>
        .main {
            max-width: 1200px;
            margin: 0 auto;
        }
        .stTextInput label {
            font-size: 16px;
            font-weight: bold;
        }
        .stTextInput input {
            font-size: 14px;
        }
        .custom-question {
            font-size: 18px;  /* Augmentation de la taille de la police pour les questions */
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
    try:
        groq_client = get_groq_client()
        request_prompt = f"L'utilisateur a décrit le problème suivant : {prompt}. Génère des questions spécifiques pour analyser et comprendre plus en détail ce problème."
        response = groq_client.generate(prompt=request_prompt, model="llama-3.1-70b-versatile", temperature=0.5, max_tokens=500)
        questions = response.split('\n')
        filtered_questions = [q.strip() for q in questions if '?' in q]
        return filtered_questions[:5]  # Limiter à 5 questions
    except Exception as e:
        st.error(f"Une erreur s'est produite lors de la génération des questions : {e}")
        return []

# Ask Groq to identify root causes based on answers
def ask_groq_for_causes(problem_description: str, answers: list):
    try:
        groq_client = get_groq_client()
        questions_and_answers = "\n".join([f"Question: {q}\nRéponse: {r}" for q, r in answers])
        prompt = f"Situation décrite : {problem_description}. \nRéponses aux questions : \n{questions_and_answers}\n Identifie les causes racines de ce problème."
        return groq_client.generate(prompt, model="llama-3.1-70b-versatile", temperature=0.7, max_tokens=500)
    except Exception as e:
        st.error(f"Une erreur s'est produite lors de l'identification des causes : {e}")
        return ""

# Get action for cause
def get_action_for_cause(cause: str):
    cause_action_mapping = {
        "Manque de formation": {"Action Proposée": "Organiser une formation sur les bonnes pratiques", "Gravité": 8, "Probabilité": 7, "Priorité": "Haute"},
        "Processus mal défini": {"Action Proposée": "Mettre à jour les SOPs et effectuer des audits réguliers", "Gravité": 9, "Probabilité": 6, "Priorité": "Très Haute"},
        "Communication insuffisante": {"Action Proposée": "Améliorer la communication entre les équipes et les services", "Gravité": 6, "Probabilité": 5, "Priorité": "Moyenne"},
        # Ajoutez ici d'autres causes et actions selon le contexte spécifique
    }
    
    return cause_action_mapping.get(cause, {"Action Proposée": "Action à déterminer", "Gravité": 5, "Probabilité": 5, "Priorité": "Moyenne"})

# Ask Groq for action plan based on causes
def ask_groq_for_action_plan(problem_description: str, causes: list):
    try:
        groq_client = get_groq_client()
        causes_str = "\n".join([f"- {cause}" for cause in causes])
        prompt = f"Situation décrite : {problem_description}. \nCauses identifiées : \n{causes_str}\n Propose un plan d'action pour résoudre ces causes."
        return groq_client.generate(prompt, model="llama-3.1-70b-versatile", temperature=0.7, max_tokens=1500)
    except Exception as e:
        st.error(f"Une erreur s'est produite lors de la génération du plan d'action : {e}")
        return ""

# Générer un fichier téléchargeable au format .txt
def generate_download_button(content: str, filename: str):
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
            with st.spinner("Génération des questions..."):
                if 'questions' not in st.session_state:
                    st.session_state.questions = ask_groq_for_questions(problem_description)
                    st.session_state.answers = []
        else:
            st.warning("Veuillez décrire la situation avant de soumettre.")

    # Si la situation a été soumise, afficher les questions
    if 'questions' in st.session_state:
        st.write("Répondez aux questions ci-dessous pour affiner l'analyse :")
        for i, question in enumerate(st.session_state.questions):
            st.markdown(f"<p class='custom-question'>Question {i+1}: {question}</p>", unsafe_allow_html=True)  # Appliquer la classe custom-question pour une police plus grande
            answer = st.text_input(f"Réponse à la Question {i+1}", key=f"answer_{i}")
            if answer and len(st.session_state.answers) == i:
                st.session_state.answers.append(answer)

        # Step 2: Submit button
        if st.button("Soumettre l'analyse"):
            if len(st.session_state.answers) == len(st.session_state.questions):
                with st.spinner("Analyse des causes et génération du plan d'action..."):
                    # Step 3: Perform root cause analysis
                    causes = ask_groq_for_causes(problem_description, list(zip(st.session_state.questions, st.session_state.answers)))
                    causes_identified = causes.split('\n')
                    
                    # Générer le plan d'action basé sur les causes
                    action_plan = ask_groq_for_action_plan(problem_description, causes_identified)
                    st.write("### Causes identifiées et Plan d'action")
                    st.write(action_plan)

                    # Convert the analysis and action plan to text and create a download button
                    full_analysis = f"Analyse des causes racines:\n{causes}\n\nPlan d'action:\n{action_plan}"
                    generate_download_button(full_analysis, "analyse_cause_source_et_plan_action.txt")
            else:
                st.warning("Veuillez répondre à toutes les questions avant de soumettre l'analyse.")

# Launch the application
if __name__ == "__main__":
    main()

