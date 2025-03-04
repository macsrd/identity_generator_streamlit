import streamlit as st
from identity_generator_2_tkinter import *  # Import your function

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
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# JavaScript for copying text to clipboard and showing a message
copy_js = """
<script>
function copyToClipboard(text) {
    var tempInput = document.createElement("input");
    tempInput.style.position = "absolute";
    tempInput.style.left = "-9999px";
    tempInput.value = text;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);
    alert("Copied to clipboard: " + text);
}
</script>
"""

st.markdown(copy_js, unsafe_allow_html=True)

st.title("Polish Identity Generator")

# User selection
gender = st.radio("Select Gender:", ["Male", "Female"])
include_secondname = st.checkbox("Include Secondname")

# Generate identity on button click
if st.button("Generate Identity"):
    try:
        # firstname, secondname, lastname, pesel, probability = generate_identity(gender, include_secondname)
        firstname, secondname, lastname, pesel = generate_identity(gender, include_secondname)
        
        st.markdown(f"<div class='identity-info' onclick='copyToClipboard(\"{firstname}\")'>**Firstname:** {firstname}</div>", unsafe_allow_html=True)
        if include_secondname and secondname:
            st.markdown(f"<div class='identity-info' onclick='copyToClipboard(\"{secondname}\")'>**Secondname:** {secondname}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='identity-info' onclick='copyToClipboard(\"{lastname}\")'>**Lastname:** {lastname}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='identity-info' onclick='copyToClipboard(\"{pesel}\")'>**PESEL:** {pesel}</div>", unsafe_allow_html=True)
        # st.markdown(f"<div class='identity-info' onclick='copyToClipboard(\"{probability}\")'>**Probability:** {probability}</div>", unsafe_allow_html=True)
    except ValueError as e:
        st.error(f"Error generating identity: {e}")