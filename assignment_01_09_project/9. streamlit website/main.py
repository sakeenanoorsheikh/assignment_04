import streamlit as st

st.set_page_config(page_title="Python website", page_icon= "🌏", layout="centered")
st.title("Welcome to my Python website! 🌏")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home")
    st.write("This is the home page of my Python website.")
    name = st.text_input("What's your name? ")
    if name:
        st.success(f"Hello, {name}! Welcome to my website.")

elif page == "About":
    st.header("About")
    st.write("This website is built entirely using Python and Streamlit in under 15 minutes!")

elif page == "Contact":
    st.header("Contact")
    email = st.text_input("Enter your email address: ")
    message = st.text_input("Enter your message: ")

    if st.button("Submit"):
        st.success("Thank you! we have received your message.")