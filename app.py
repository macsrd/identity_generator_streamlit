import streamlit as st
from identity_generator_2_tkinter import generate_identity
from st_copy_to_clipboard import st_copy_to_clipboard

st.title("Polish Identity Generator")

# User selection
gender = st.radio("Select Gender:", ["Male", "Female"])
include_secondname = st.checkbox("Include Secondname")

# Generate identity on button click
if st.button("Generate Identity"):
    try:
        firstname, secondname, lastname, pesel = generate_identity(gender, include_secondname)
        st.session_state.identity = [
            ("Firstname", firstname),
            ("Lastname", lastname),
            ("PESEL", pesel)
        ]
        if include_secondname and secondname:
            st.session_state.identity.insert(1, ("Secondname", secondname))
    except ValueError as e:
        st.error(f"Error generating identity: {e}")

# Display identity information with value and copy button
if "identity" in st.session_state:
    for key, value in st.session_state.identity:
        col1, col2 = st.columns([3, 1])
        col1.write(f"**{key}:** {value}")
        col2.write(st_copy_to_clipboard(value, f"Copy {key}"))

st.info("Click on the 'Copy' button next to each value to copy it to your clipboard.")
