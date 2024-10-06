import streamlit as st
import requests
from pocketgroq import GroqProvider

# Initialize Groq Client
def get_groq_client():
    """Initialize and return a Groq client with the API key."""
    return GroqProvider(api_key=st.secrets["GROQ_API_KEY"])

# Fetch available models from Groq API
def fetch_available_models():
    """Fetch the available models from Groq API."""
    url = "https://api.groq.com/openai/v1/models"
    headers = {
        "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    models = response.json().get('data', [])
    return [model['id'] for model in models]

# Generate standard food safety-specific questions
def get_food_safety_questions():
    """Return a list of standard questions related to food safety for root cause analysis."""
    return [
        "Est-ce que les procédures standardisées (SOP) sont bien suivies par le personnel ?",
        "Y a-t-il des écarts de formation dans l'équipe sur la sécurité alimentaire ?",
        "Les contrôles préventifs et correctifs sont-ils bien en place et documentés ?",
        "Les audits internes sont-ils réalisés régulièrement ?",
        "La communication entre les départements est-elle suffisante pour détecter les non-conformités rapidement ?"
    ]

# Ask Groq to generate questions based on user's input
def ask_groq_for_questions(prompt: str, model: str):
    """Generate context-specific questions dynamically using the Groq model."""
    groq_client = get_groq_client()
    # Formuler la requête pour le modèle Groq
    request_prompt = (
        f"L'utilisateur a décrit le problème suivant : {prompt}. "
        f"Génère des questions spécifiques pour analyser et comprendre plus en détail ce problème."
    )
    # Appel à l'API Groq pour générer les questions
    response = groq_client.generate(
        prompt=request_prompt,
        model=model,
        temperature=0.5,  # Ajuste la créativité de la génération
        max_tokens=500
    )
    
    # On suppose que le modèle renvoie une liste de questions dans le texte de la réponse
    questions = response.split('\n')  # Diviser la réponse par lignes pour obtenir les questions
    return [question for question in questions if question]  # Filtrer les lignes vides

# Ask Groq for root cause analysis and recommendations
def ask_groq_for_analysis(problem_description: str, answers: list, model: str):
    """Analyze the problem and propose corrective actions based on answers and situation."""
    groq_client = get_groq_client()
    questions_and_answers = "\n".join([f"Question: {q}\nRéponse: {r}" for q, r in answers])
    prompt = f"Situation décrite : {problem_description}. \nRéponses aux questions : \n{questions_and_answers}\n Propose une analyse des causes racines avec des actions correctives."
    return groq_client.generate(prompt, model=model, temperature=0.7, max_tokens=1500)

# Main application function
def main():
    st.title("Analyse de Cause Source - Sécurité Alimentaire")

    # Fetch models if not already done
    if 'available_models' not in st.session_state:
        st.session_state.available_models = fetch_available_models()

    # Select the Groq model
    model = st.selectbox("Choisissez un modèle Groq:", st.session_state.available_models, key='selected_model')

    # User's problem input
    st.write("Présentez votre problématique, non-conformité ou situation.")
    problem_description = st.text_area("Décrivez la situation ici...")

    # Step 5: Dynamic Questions
    if problem_description:
        if 'questions' not in st.session_state:
            # Initialize the questions with domain-specific ones
            st.session_state.questions = get_food_safety_questions()
            st.session_state.answers = []

        # Display and gather responses to questions
        for i, question in enumerate(st.session_state.questions):
            answer = st.text_input(f"Question {i+1}: {question}", key=f"answer_{i}")
            if answer and len(st.session_state.answers) == i:  # Ensure answers are collected in order
                st.session_state.answers.append(answer)
                
                # Ask Groq to generate additional questions based on user input
                if len(st.session_state.answers) == len(st.session_state.questions):
                    additional_question = ask_groq_for_questions(problem_description, model)
                    st.session_state.questions.append(additional_question)

        # Step 6: Perform root cause analysis
        if st.button("Analyser la cause source"):
            if len(st.session_state.answers) >= 1:  # Ensure at least one answer has been given
                analysis_response = ask_groq_for_analysis(problem_description, list(zip(st.session_state.questions, st.session_state.answers)), model)
                st.write(analysis_response)

                # Step 7: Generate the cause and action table with metrics and priorities
                causes_and_actions = [
                    {"Cause": "Manque de formation", "Action Proposée": "Organiser une formation sur les bonnes pratiques", "Gravité": 8, "Probabilité": 7, "Priorité": "Haute"},
                    {"Cause": "Processus mal défini", "Action Proposée": "Mettre à jour les SOPs et effectuer des audits réguliers", "Gravité": 9, "Probabilité": 6, "Priorité": "Très Haute"},
                    {"Cause": "Communication insuffisante", "Action Proposée": "Améliorer la communication entre les équipes et les services", "Gravité": 6, "Probabilité": 5, "Priorité": "Moyenne"}
                ]
                
                # Display table with metrics and priorities
                st.table(causes_and_actions)
            else:
                st.warning("Veuillez répondre aux questions avant de procéder à l'analyse.")

# Launch the application
if __name__ == "__main__":
    main()

