import streamlit as st

from chatbot_main import initial_chatbot_response


def main():
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
        loading_text = st.empty()
        loading_text = st.text("Generating response...")
        # time.sleep(4)
        response = initial_chatbot_response(user_input)
        loading_text.empty()
        st.text_area("Chatbot:",
                     response, disabled=True)

    st.write(
        "Welcome to Med-Xplain, a patient informational tool. We aim to help you learn more about your treatment options post-diagnosis.")


if __name__ == "__main__":
    main()
