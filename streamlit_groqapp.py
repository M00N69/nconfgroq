import streamlit as st
from groq import Groq  # Import the Groq API client

# Initialize the Groq API client using an API key from Streamlit's secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Define a function for generating responses using the detailed instruction
def generate_response(user_input):
    # Define the system instruction for processing the user's input
    system_instruction = """
    Se référer en priorité aux documents qui ont été mis à disposition concernant IFSv8. La reformulation doit être réalisée en français puis ne anglais à chaque fois . Les bonnes pratiques de la reformulation de l'écart sont: doit être factuelle, doit être détaillée (référence de la procédure, zone /équipement, …), doit justifier le choix de notation, en fonction du type de déviation/non-conformité, le risque produit doit être préciser en restant dans le contexte de l’exigence, ne doit pas être assimilable à du conseil, ne doit pas être rédigée sous forme de suggestions. La reformulation de l'écart doit de préférence inclure les 4 aspects suivants: 1/ L’exigence exemple: La norme exige que … ou exigence interne 2/ Description de la défaillance: Les responsabilités, la méthode ou les informations documentées n’ont pas été prévues à ce sujet OU Les dispositions prévues ne sont pas mises en œuvre OU Les dispositions prévues ne sont pas toujours mises en œuvre OU Les dispositions prévues et mises en œuvre ne sont pas toujours suffisamment efficaces à atteindre tel résultat prévu 3/ Preuve de la défaillance 4/ Conséquence / Impact de cet écart dans le contexte de l’exigence; toujours conclure en expliquant pourquoi le risque est limité.
    """

    # Use Groq's API to create a chat completion with detailed instruction
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_input},
            {"role": "system", "content": system_instruction}  # Include the detailed instruction
        ],
        model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content

# Define a function for the Non-Conformities page
def page_reformulation():
    st.title("Reformulation des Non-Conformités")
    user_input = st.text_area("Posez votre question ici:", height=200)
    if st.button("Envoyer"):
        with st.spinner('Attendez pendant que nous générons la réponse...'):
            response = generate_response(user_input)
            st.write(response)

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
