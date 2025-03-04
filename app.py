import streamlit as st
from identity_generator_2_tkinter import *  # Import your function

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f0f0;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .identity-info {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Polish Identity Generator")
st.header("Generate a Polish Identity")
st.subheader("Please select the options below:")

# User selection
gender = st.radio("Select Gender:", ["Male", "Female"])
include_secondname = st.checkbox("Include Surname")

# Generate identity on button click
if st.button("Generate Identity"):
    try:
        # firstname, secondname, lastname, pesel, probability = generate_identity(gender, include_secondname)
        firstname, secondname, lastname, pesel = generate_identity(gender, include_secondname)
        
        st.text(f"Firstname: {firstname}")
        if include_secondname and secondname:
            st.text(f"Secondname: {secondname}")
        st.text(f"Lastname: {lastname}")
        st.text(f"PESEL: {pesel}")
        # st.markdown(f"<div class='identity-info'>**Probability:** {probability}</div>")
    except ValueError as e:
        st.error(f"Error generating identity: {e}")