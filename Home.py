# Home.py
import streamlit as st
from app.db import get_connection
from app.users import add_user, get_user, hash_password

conn = get_connection()  # SQLite connection

st.title("Welcome to the Home Page")

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = None

tab_login, tab_register = st.tabs(["Log In", "Register"])


with tab_login:
    st.header("Log In")
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log In"):
        user = get_user(conn, login_username)
        if user and user[2] == hash_password(login_password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = login_username
            st.success(f"Logged in successfully as {login_username}!")
        else:
            st.error("Invalid username or password")
with tab_register:
    st.header("Register")
    register_username = st.text_input("Choose a Username", key="register_username")
    register_password = st.text_input("Choose a Password", type="password", key="register_password")

    if st.button("Register"):
        hashed_pw = hash_password(register_password)
        add_user(conn, register_username, hashed_pw)
        st.success("Registration successful! You can now log in.")
    
if st.session_state['logged_in']:
    st.info(f"Logged in as {st.session_state['username']}")
    if st.button("Log Out"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.info("You have been logged out.")
if st.button("Load Cyber Incidents CSV"):
    migrate_cyber_incidents(conn)
    st.success("Cyber incidents loaded!")

if st.button("Show Cyber Incidents"):
    df = get_all_cyber_incidents(conn)
    st.dataframe(df)
    
conn.close()

