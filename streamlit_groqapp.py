import streamlit as st
from groq import Groq

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

# Access the GROQ API key from secrets
api_key = st.secrets["api_keys"]["groq"]

# Initialize the Groq API client
client = Groq(api_key=api_key)

# Initialize Session State for Login Status
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Simple Login Function (Plaintext Passwords - INSECURE)
def login(username, password):
    try:
        user_dict = st.secrets["users"]
        if username in user_dict and user_dict[username] == password:
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Incorrect username or password")
    except KeyError:
        st.error("User credentials not set up properly in the secrets configuration.")

# Login Page
def login_page():
    st.title("Login to VisiPilot App")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            login(username, password)

# Define a function for generating responses using detailed instructions
def generate_response(user_input):
    system_instruction = """
    reformuler chaque non-conformité en langue française puis en langue anglaise, en utilisant les instructions suivantes :
    Référez-vous aux documents de la norme IFSv8 en priorité.
    Assurez-vous que la reformulation soit factuelle, détaillée et justifie le choix de la notation. Pour ce faire, mentionnez la référence de la procédure, la zone ou l'équipement concerné, et précisez le risque produit tout en restant dans le contexte de l'exigence.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_input},
            {"role": "system", "content": system_instruction}
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

# Main Application Logic
def main_app():
    st.sidebar.title('Navigation')
    option = st.sidebar.selectbox(
        'Choix de page:',
        ('Reformulation des Non-Conformités', 'Autre projet')
    )

    if option == 'Reformulation des Non-Conformités':
        page_reformulation()
    elif option == 'Autre projet':
        Page_Autre_projet()

def Page_Autre_projet():
    st.title("Page Autre projet")
    st.write("Contenu à venir")

# App Routing based on login status
if not st.session_state.logged_in:
    login_page()
else:
    main_app()


