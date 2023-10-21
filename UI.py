import streamlit as st

from chatbot_main import chatbot_response

# Custom CSS to centralize content
st.markdown("""
    <style>
    .center {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Centralize the title
st.markdown('<div class="center"><h1>Med-Xplain</h1></div>', unsafe_allow_html=True)

# Add some space between the title and the logo
st.markdown('<div class="center" style="margin-top: 20px;">', unsafe_allow_html=True)
st.image("./images/MedXPlain_LOGO.png", width=200)
st.markdown('</div>', unsafe_allow_html=True)

user_input = st.text_input("How can we help you today?", "")
if st.button("Send"):
    response = chatbot_response(user_input)
    st.text_area("Chatbot:", response)

st.write(
    "Welcome to Med-Xplain, a patient informational tool. We aim to help you learn more about your treatment options post-diagnosis.")
