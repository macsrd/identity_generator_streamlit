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
    navigator.clipboard.writeText(text).then(function() {
        var message = document.createElement("div");
        message.innerText = "Copied to clipboard: " + text;
        message.style.color = "green";
        message.style.fontWeight = "bold";
        document.body.appendChild(message);
        setTimeout(function() {
            document.body.removeChild(message);
        }, 2000);
    }, function(err) {
        console.error("Could not copy text: ", err);
    });
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