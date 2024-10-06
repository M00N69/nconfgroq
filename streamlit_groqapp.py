import streamlit as st
import bcrypt
from groq import Groq  # Import the Groq API client assuming this is a valid import
from login_component import login_page

# Setting page configuration
st.set_page_config(
    page_title="VisiPilot App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "This is a sample Streamlit app using Groq API."
    }
)

# Initialize the Groq API client using an API key from Streamlit's secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Initialize Session State for Login Status
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Simple Login Function with secure password handling
def login(username, password):
    try:
        user_dict = st.secrets["users"]
        if username in user_dict and bcrypt.checkpw(password.encode('utf-8'), user_dict[username].encode('utf-8')):
            st.session_state.logged_in = True
            st.success("Accès accordé! Allez dans le menu ")
        else:
            st.error("Incorrect username or password")
    except KeyError:
        st.error("User credentials are not set up properly in secrets.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Login Page
def login_page():
    st.title("Login to VisiPilot App")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            login(username, password)

# Define a function for generating responses using the detailed instruction
def generate_response(user_input):
    # Detailed instructions for generating responses
    system_instruction = """
    Reformulez chaque non-conformité en français puis en anglais, en suivant les consignes ci-dessous :
    
    1. **Référence à la norme ou aux exigences internes** : 
       Faites référence aux documents de la norme IFSv8 ou à des exigences internes précises. Mentionnez l'exigence correspondante (ex : 'La norme IFSv8 exige que…' ou 'L'entreprise a prévu de…'), en précisant le respect général de l'exigence, si applicable (ex : 'Les déchets sont correctement gérés…').
    
    2. **Description de la défaillance** : 
       Identifiez la responsabilité, la méthode ou l'information manquante ou inadéquate, qui empêche de répondre à l'exigence. Décrivez factuellement l'écart observé, sans formuler de conseils ou de suggestions.
    
    3. **Preuve de la défaillance** : 
       Fournissez des éléments concrets prouvant la non-conformité, basés sur des observations ou des documents vérifiables (ex : enregistrements, contrôles visuels).
    
    4. **Conséquence/Impact de la défaillance** : 
       Évaluez l'impact de cette non-conformité sur le produit ou le process, en lien avec le risque produit et le contexte de l'exigence (ex : risque pour la sécurité alimentaire), tout en soulignant les éléments qui atténuent ce risque.
    
    Exemple en français :
    La norme IFSv8 exige que les équipements soient régulièrement contrôlés pour garantir leur conformité sanitaire. Cependant, il a été observé que les enregistrements de maintenance préventive de la ligne de production n°3 ne sont pas à jour. En effet, plusieurs interventions prévues n'ont pas été réalisées dans les délais prescrits. Cette défaillance a été confirmée par la consultation des registres de maintenance. Elle peut entraîner un risque accru de panne ou de contamination, bien que ce risque soit limité par la mise en place de contrôles de qualité réguliers sur cette ligne.
    
    Exemple en anglais :
    The IFSv8 standard requires that equipment be regularly inspected to ensure sanitary compliance. However, it was observed that the preventive maintenance records for production line #3 are not up to date. Specifically, several scheduled interventions were not carried out within the required timeframe. This failure was confirmed through the review of maintenance logs. It may increase the risk of breakdowns or contamination, although this risk is mitigated by regular quality checks on this line.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_input},
            {"role": "system", "content": system_instruction}
        ],
        model="llama-3.1-70b-versatile",
    )
    return chat_completion.choices[0].message.content

# Define a function for the Non-Conformities page
def page_reformulation():
    image_path = 'https://raw.githubusercontent.com/M00N69/Gemini-Knowledge/main/visipilot%20banner.PNG'
    st.image(image_path, use_column_width=True)
    st.title("Reformulation des Non-Conformités")
    user_input = st.text_area("Posez votre question ici:", height=200)
    if st.button("Envoyer"):
        with st.spinner('Attendez pendant que nous générons la réponse...'):
            response = generate_response(user_input)
            st.write(response)

# Main application logic and sidebar navigation
def main_app():
    st.sidebar.title('Navigation')
    option = st.sidebar.selectbox(
        'Choose a page:',
        ('Reformulation des Non-Conformités', 'Other Project')
    )
    if option == 'Reformulation des Non-Conformités':
        page_reformulation()
    elif option == 'Other Project':
        another_page()

def another_page():
    st.title("Other Project Page")
    st.write("Content to come.")

# App routing based on login status
if not st.session_state.logged_in:
    login_page()
else:
    main_app()

# Optionally, add a button to restart the app
if st.sidebar.button("Restart App"):
    st.experimental_rerun()

