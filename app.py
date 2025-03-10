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

# Custom CSS to style the layout
st.markdown("""
<style>
.identity-row {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
.identity-key {
    font-weight: bold;
    margin-right: 5px; /* Reduced margin */
}
.stButton > button {
    height: 30px;
    padding: 0 10px;
    line-height: 30px;
}
</style>
""", unsafe_allow_html=True)

# Display identity information with key and copy button
if "identity" in st.session_state:
    for key, value in st.session_state.identity:
        col1, col2 = st.columns([1, 2]) # Adjusted column widths
        with col1:
            st.markdown(f'<div class="identity-key">{key}:</div>', unsafe_allow_html=True)
        with col2:
            st_copy_to_clipboard(value, value)

st.info("Click on the button next to each key to copy its value to your clipboard.")
