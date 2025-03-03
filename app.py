import streamlit as st
from identity_generator_2_tkinter import *  # Import your function

st.title("Polish Identity Generator")

# User selection
gender = st.radio("Select Gender:", ["Male", "Female"])
include_secondname = st.checkbox("Include Surname")

# Generate identity on button click
if st.button("Generate Identity"):
    firstname, secondname, lastname, pesel, probability = generate_identity(gender, include_secondname)
    
    st.write("**Firstname:**", firstname)
    if include_secondname:
        st.write("**Secondname:**", secondname)
    st.write("**Lastname:**", lastname)
    st.write("**PESEL:**", pesel)
    st.write("**Probability:**", probability)