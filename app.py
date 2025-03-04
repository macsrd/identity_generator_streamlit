import streamlit as st
from identity_generator_2_tkinter import *  # Import your function

# Add this JavaScript function
st.markdown("""
<script>
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        console.log('Copying to clipboard was successful!');
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}
</script>
""", unsafe_allow_html=True)

st.title("Polish Identity Generator")


# User selection
gender = st.radio("Select Gender:", ["Male", "Female"])
include_secondname = st.checkbox("Include Secondname")

# Generate identity on button click
if st.button("Generate Identity"):
    try:
        firstname, secondname, lastname, pesel = generate_identity(gender, include_secondname)
        
        st.markdown(f"""
        **Firstname:** <span onclick="copyToClipboard('{firstname}')" style="background-color: lightblue; cursor: pointer;">{firstname}</span>
        """, unsafe_allow_html=True)
        
        if include_secondname and secondname:
            st.markdown(f"""
            **Secondname:** <span onclick="copyToClipboard('{secondname}')" style="background-color: lightblue; cursor: pointer;">{secondname}</span>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
        **Lastname:** <span onclick="copyToClipboard('{lastname}')" style="background-color: lightblue; cursor: pointer;">{lastname}</span>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        **PESEL:** <span onclick="copyToClipboard('{pesel}')" style="background-color: lightblue; cursor: pointer;">{pesel}</span>
        """, unsafe_allow_html=True)
    except ValueError as e:
        st.error(f"Error generating identity: {e}")