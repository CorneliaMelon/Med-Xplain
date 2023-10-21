import streamlit as st

# Define a function to simulate the chatbot responses
def chatbot_response(user_input):
    # In a real chatbot, you would implement the logic to generate responses here.
    # For this example, let's just echo the user's input.
    return f"You said: {user_input}"

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
st.image("/Users/bhallaa/Documents/DevDoc/OxAI/MedXPlain_LOGO.png", width=200)
st.markdown('</div>', unsafe_allow_html=True)


user_input = st.text_input("How can we help you today?", "")
if st.button("Send"):
    response = chatbot_response(user_input)
    st.text_area("Chatbot:", response)

st.write("Welcome to Med-Xplain, a patient informational tool. We aim to help you learn more about your treatment options post-diagnosis.")
