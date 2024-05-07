import streamlit as st
import bcrypt

# Assuming API_Client is the correct client class for your API
from your_api_client_library import API_Client

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

# Access the API key from secrets
api_key = st.secrets["api_keys"]["groq"]

# Initialize the API client
client = API_Client(api_key=api_key)

# Initialize Session State for Login Status
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Simple Login Function with secure password handling
def login(username, password):
    try:
        user_dict = st.secrets["users"]
        if username in user_dict and bcrypt.checkpw(password.encode('utf-8'), user_dict[username].encode('utf-8')):
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
    Reformulate each non-conformity in French and then in English, using the following instructions:
    Refer to the IFSv8 standard documents as a priority.
    Ensure that the reformulation is factual, detailed, and justifies the choice of notation. For this, mention the reference of the procedure, the area or equipment concerned, and specify the product risk while remaining in the context of the requirement.
    """
    chat_completion = client.chat_completions_create(
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
        with st.spinner('Generating response...'):
            response = generate_response(user_input)
            st.write(response)

# Main Application Logic
def main_app():
    st.sidebar.title('Navigation')
    option = st.sidebar.selectbox(
        'Choose a page:',
        ('Reformulation des Non-Conformités', 'Other Project')
    )

    if option == 'Reformulation des Non-Conformités':
        page_reformulation()
    elif option == 'Other Project':
        other_project_page()

def other_project_page():
    st.title("Other Project Page")
    st.write("Content coming soon.")

# App Routing based on login status
if not st.session_state.logged_in:
    login_page()
else:
    main_app()
