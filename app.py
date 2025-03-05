import streamlit as st
from identity_generator_2_tkinter import generate_identity
from st_copy_to_clipboard import st_copy_to_clipboard

# Custom CSS for styling the copy icon
st.markdown("""
<style>
.copy-icon {
    cursor: pointer;
    color: #4CAF50;
    font-size: 18px;
    margin-left: 10px;
}
.copy-icon:hover {
    color: #45a049;
}
.identity-row {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
.identity-value {
    font-weight: bold;
    margin-right: 10px;
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

# Display identity information with value and copy icon
if "identity" in st.session_state:
    for key, value in st.session_state.identity:
        # Create a row with the value and a copy icon
        st.markdown(f"""
        <div class="identity-row">
            <div class="identity-value">{key}: {value}</div>
            <div class="copy-icon" onclick="navigator.clipboard.writeText('{value}'); alert('Copied {key}!');">📋</div>
        </div>
        """, unsafe_allow_html=True)

st.info("Click on the copy icon next to each value to copy it to your clipboard.")
