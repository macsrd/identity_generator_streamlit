import streamlit as st
from identity_generator_2_tkinter import generate_identity  # Import your function

st.title("Polish Identity Generator")

# User selection
gender = st.radio("Select Gender:", ["Male", "Female"])
include_secondname = st.checkbox("Include Surname")

# Generate identity on button click
if st.button("Generate Identity"):
    identity = generate_identity(gender, include_secondname)
    st.success(f"Generated Identity: **{identity}**")