import streamlit as st
from identity_generator_2_tkinter import generate_identity  # Import your function
from st_copy_to_clipboard import st_copy_to_clipboard

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
        width: 100%;
        text-align: left;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    .identity-info {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Polish Identity Generator")

# User selection
gender = st.radio("Select Gender:", ["Male", "Female"])
include_secondname = st.checkbox("Include Secondname")

# Generate identity on button click
if st.button("Generate Identity"):
    try:
        firstname, secondname, lastname, pesel = generate_identity(gender, include_secondname)
        
        # Store generated values in session state
        st.session_state.identity = {
            "Firstname": firstname,
            "Lastname": lastname,
            "PESEL": pesel
        }
        if include_secondname and secondname:
            st.session_state.identity["Secondname"] = secondname
    except ValueError as e:
        st.error(f"Error generating identity: {e}")

# Display and create copy buttons for stored values
if "identity" in st.session_state:
    for key, value in st.session_state.identity.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"**{key}:**")
        with col2:
            st_copy_to_clipboard(value, value)  # Use the value as the button text

# Add a note about copying
st.info("Click on the values to copy them to your clipboard.")
