import streamlit as st
from identity_generator_2_tkinter import generate_identity
from st_copy_to_clipboard import st_copy_to_clipboard

# Custom CSS to reduce spacing
st.markdown("""
<style>
div.stMarkdown {
    margin-bottom: 0rem;
    padding-bottom: 0rem;
}
div.row-widget.stButton {
    margin-top: 0rem;
    padding-top: 0rem;
}
</style>
""", unsafe_allow_html=True)

st.title("Polish Identity Generator")

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
        st.markdown(f"""
        <div style="margin-bottom: 0px; padding-bottom: 0px;">
            <strong>{key}:</strong><br>
        </div>
        """, unsafe_allow_html=True)
        # The copy button will appear immediately below with minimal spacing
        st_copy_to_clipboard(value, value)

st.info("Click on the values to copy them to your clipboard.")