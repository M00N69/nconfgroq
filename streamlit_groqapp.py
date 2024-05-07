import streamlit as st
from groq import Groq  # Import the Groq API client

# Setting page configuration to hide the hamburger menu
st.set_page_config(
    page_title="VisiPilot App",  # Add your app title here
    page_icon="🚀",  # You can use an emoji or a path to an image file
    layout="wide",  # "wide" or "centered"
    initial_sidebar_state="expanded",  # "expanded" or "collapsed"
    menu_items={
        'Get Help': None,  # Optional: Add a URL to a help page
        'Report a bug': None,  # Optional: Add a URL to report bugs
        'About': "This is a sample Streamlit app using Groq API.",  # Optional: Information about the app or the developer
        'show_menu': False  # Hiding the hamburger menu
    }
)

# Initialize the Groq API client using an API key from Streamlit's secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Define a function for generating responses using the detailed instruction
def generate_response(user_input):
    system_instruction = """
    reformuler chaque non-conformité en langue française puis en langue anglaise, en utilisant les instructions suivantes :
    Référez-vous aux documents de la norme IFSv8 en priorité.
    Assurez-vous que la reformulation soit factuelle, détaillée et justifie le choix de la notation. Pour ce faire, mentionnez la référence de la procédure, la zone ou l'équipement concerné, et précisez le risque produit tout en restant dans le contexte de l'exigence.
    Évitez de formuler la reformulation sous forme de conseils ou de suggestions. Elle doit simplement décrire la non-conformité constatée.
    La reformulation doit idéalement inclure les quatre aspects suivants :
    L'exigence : par exemple, 'La norme exige que...' ou 'L'exigence interne est de...'
    La description de la défaillance : précisez les responsabilités, la méthode ou les informations documentées qui n'ont pas été prévues ou mises en œuvre, ou qui ne sont pas suffisamment efficaces pour atteindre le résultat prévu.
    La preuve de la défaillance : fournissez des éléments concrets qui prouvent la non-conformité.
    La conséquence/l'impact de cette défaillance dans le contexte de l'exigence : concluez en expliquant pourquoi le risque est limité.
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
    image_path = 'https://raw.githubusercontent.com/M00N69/Gemini-Knowledge/main/visipilot%20banner.PNG'
    st.image(image_path, use_column_width=True)
    
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
