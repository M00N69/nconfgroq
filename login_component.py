# login_component.py

import streamlit as st
import bcrypt

def login(username, password):
    try:
        user_dict = st.secrets["users"]
        if username in user_dict and bcrypt.checkpw(password.encode('utf-8'), user_dict[username].encode('utf-8')):
            st.session_state.logged_in = True
            st.success("Access granted! Navigate to the menu.")
        else:
            st.error("Incorrect username or password")
    except KeyError:
        st.error("User credentials are not set up properly in secrets.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def login_page():
    st.title("Login to Visipilot App")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            login(username, password)
