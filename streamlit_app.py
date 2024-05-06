import streamlit as st
import google.generativeai as genai

# Configure the API key using Streamlit secrets
api_key = st.secrets["api_key"]
genai.configure(api_key=api_key)

# Model setup
generation_config = {
    "temperature": 2,
    "top_p": 0.4,
    "top_k": 32,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

system_instruction = "Se référer en priorité aux documents qui ont été mis à disposition concernant IFSv8. Les bonnes pratiques de la reformulation de l'écart sont: doit être factuelle,doit être détaillée (référence de la procédure, zone /équipement, ….), doit justifier le choix de notation, en fonction du type de déviation/non-conformité, le risque produit doit être préciser en restant dans le contexte de l’exigence, ne doit pas être assimilable à du conseil, ne doit pas être rédigée sous forme de suggestions.La reformulation de l'écart doit de préférence inclure les 4 aspects suivants:1/ L’exigence exemple: La norme exige que ….. ou exigence interne 2/ Description de la défaillance : Les responsabilités, la méthode ou les informations documentées n’ont pas été prévues à ce sujet  OU Les dispositions prévues ne sont pas mises en œuvre OU Les dispositions prévues ne sont pas toujours mises en œuvre OU Les dispositions prévues et mises en œuvre ne sont pas toujours suffisamment efficaces à atteindre tel résultat prévu 3/ Preuve de la défaillance 4/ Conséquence / Impact de cet écart dans le contexte de l’exigence; toujours conclure en expliquant pour le risque est limité. Réaliser systématiquement les 2 reformulations ( toujours 1 en français et 1 en anglais) ne doivent pas inclure des conseils ou des recommandations dans la description du risque qui ne doit pas exagérer le danger. La reformulation doit être professionnelle sans citer les 4 étapes mais les rédigeant de manière harmonieuse et compréhensible"

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings=safety_settings
)

# Define a function for each page
def page_reformulation():
    st.title("Reformulation des Non-Conformités")
    user_input = st.text_area("Posez votre question ici:", height=200)  # Height is in pixels
    if st.button("Envoyer"):
        convo = model.start_chat(history=[{"role": "user", "parts": [user_input]}])
        with st.spinner('Attendez pendant que nous générons la réponse...'):
            response = convo.send_message(user_input)
            st.write(response.text)

def another_page():
    st.title("Another Page")
    st.write("Content for another page")

# Set up sidebar navigation
st.sidebar.title('Navigation')
option = st.sidebar.selectbox(
    'Choose a page:',
    ('Reformulation des Non-Conformités', 'Another Page')
)

if option == 'Reformulation des Non-Conformités':
    page_reformulation()
elif option == 'Another Page':
    another_page()

# Optionally, add a button to restart the app
if st.sidebar.button("Restart App"):
    st.experimental_rerun()
