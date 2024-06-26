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
    reformuler chaque non-conformité en langue française puis en langue anglaise, en utilisant les instructions suivantes :
    Référez-vous aux documents de la norme IFSv8 en priorité.
    Assurez-vous que la reformulation soit factuelle, détaillée et justifie le choix de la notation. Pour ce faire, mentionnez la référence de la procédure, la zone ou l'équipement concerné, et précisez le risque produit tout en restant dans le contexte de l'exigence.
    Évitez de formuler la reformulation sous forme de conseils ou de suggestions. Elle doit simplement décrire la non-conformité constatée.
    La reformulation doit idéalement inclure les quatre aspects suivants :
    L’exigence exemple: "La norme exige que ….." dasn ce cas bien s'assurer que la référence à l'exigenc de la norme est la bonne ens e référant aux documents de la normes IFSv8  ou exigence interne "Pour cela l’entreprise a prévu de ….". Il faut également ajouté des élément confirmons que dans l'ensemble l'exigence est remplie exemple : Les déchets sont correctement  gérés au niveau du site  ou Les sols sont conçus et adaptés aux process... 
    La description de la défaillance : précisez les responsabilités, la méthode ou les informations documentées qui n'ont pas été prévues ou mises en œuvre, ou qui ne sont pas suffisamment efficaces pour atteindre le résultat prévu.
    La preuve de la défaillance : fournissez des éléments concrets qui prouvent la non-conformité.
    La conséquence/l'impact de cette défaillance dans le contexte de l'exigence : concluez en expliquant pourquoi le risque est limité.
    Exemple de reformulation pour la langue française : La norme IFSv8 exige que les procédures de nettoyage soient documentées et mises en œuvre pour assurer la salubrité des équipements de production. Cependant, nous avons constaté que la procédure de nettoyage de la ligne de production n°1 n'était pas suivie correctement. En effet, les opérateurs ne respectent pas les fréquences de nettoyage prévues et n'utilisent pas les produits de nettoyage adéquats. Cette défaillance a été constatée lors de l'inspection visuelle des équipements et confirmée par les enregistrements de nettoyage. Cette non-conformité peut entraîner une contamination croisée des produits et un risque pour la sécurité alimentaire. Toutefois, le risque est limité car la ligne de production n°1 est dédiée à un seul type de produit et que des contrôles microbiologiques réguliers sont effectués.
    English version : The IFSv8 standard requires that cleaning procedures be documented and implemented to ensure the cleanliness of production equipment. However, we observed that the cleaning procedure for production line #1 was not being followed correctly. Specifically, operators do not follow the scheduled cleaning frequencies and do not use the appropriate cleaning products. This failure was observed during a visual inspection of the equipment and confirmed by cleaning records. This non-conformity may result in cross-contamination of products and a risk to food safety. However, the risk is limited as production line #1 is dedicated to a single product type and regular microbiological controls are performed.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_input},
            {"role": "system", "content": system_instruction}
        ],
        model="llama3-8b-8192",
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

