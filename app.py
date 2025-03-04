import streamlit as st
from identity_generator_2_tkinter import generate_identity
from st_copy_to_clipboard import st_copy_to_clipboard

st.set_page_config(page_title="Polish Identity Generator", layout="wide")

# Custom CSS for reduced spacing and button styling
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        text-align: left;
        height: 30px;
        padding: 0 10px;
        margin: 0;
    }
    .identity-row {
        margin-bottom: 5px;
    }
    .identity-label {
        font-weight: bold;
        margin-bottom: 2px;
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
        <div class="identity-row">
            <div class="identity-label">{key}:</div>
            {st_copy_to_clipboard(value, value)}
        </div>
        """, unsafe_allow_html=True)

st.info("Click on the values to copy them to your clipboard.")