import streamlit as st
from identity_generator_2_tkinter import *  # Import your function
import pyperclip

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
    .copyable {
        background-color: lightblue;
        cursor: pointer;
        padding: 2px 5px;
        border-radius: 3px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Polish Identity Generator")

# User selection
gender = st.radio("Select Gender:", ["Male", "Female"])
include_secondname = st.checkbox("Include Secondname")

# Function to copy text to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)
    st.success(f"Copied to clipboard: {text}")

# Generate identity on button click
if st.button("Generate Identity"):
    try:
        firstname, secondname, lastname, pesel = generate_identity(gender, include_secondname)
        st.session_state.identity = {
            "firstname": firstname,
            "secondname": secondname,
            "lastname": lastname,
            "pesel": pesel
        }
    except ValueError as e:
        st.error(f"Error generating identity: {e}")

if "identity" in st.session_state:
    for key, value in st.session_state.identity.items():
        if key != "secondname" or (include_secondname and value):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**{key.capitalize()}:**")
            with col2:
                if st.button(value, key=f"copy_{key}"):
                    pyperclip.copy(value)
                    st.success(f"Copied to clipboard: {value}")
