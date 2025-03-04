import streamlit as st
from identity_generator_2_tkinter import generate_identity
from st_copy_to_clipboard import st_copy_to_clipboard

st.title("Polish Identity Generator")

# Custom CSS to reduce spacing between elements
st.markdown(
    """
    <style>
    .block-container {
        margin-bottom: 0rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

gender = st.radio("Select Gender:", ["Male", "Female"])
include_secondname = st.checkbox("Include Secondname")

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

if "identity" in st.session_state:
    for key, value in st.session_state.identity:
        st.markdown(f"**{key}:**")
        st_copy_to_clipboard(value, value)

st.info("Click on the values to copy them to your clipboard.")
