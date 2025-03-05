import streamlit as st
from identity_generator_2_tkinter import generate_identity
from st_copy_to_clipboard import st_copy_to_clipboard

# Custom CSS to reduce spacing
st.markdown("""
<style>
.identity-row {
    margin-bottom: 5px; /* Adjust this value to control spacing */
}
.identity-label {
    font-weight: bold;
    margin-bottom: 0px;
    padding-bottom: 0px;
}
.identity-copy {
    margin-top: -10px; /* Negative margin to reduce space */
}
</style>
""", unsafe_allow_html=True)

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

# Display identity information with reduced spacing
if "identity" in st.session_state:
    for key, value in st.session_state.identity:
        # Combine label and button into a single row with reduced spacing
        st.markdown(f"""
        <div class="identity-row">
            <div class="identity-label">{key}:</div>
            <div class="identity-copy">{st_copy_to_clipboard(value, value)}</div>
        </div>
        """, unsafe_allow_html=True)

st.info("Click on the values to copy them to your clipboard.")