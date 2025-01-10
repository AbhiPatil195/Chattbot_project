import streamlit as st
import requests

# Title and description
st.title("🤖 Chatbot Assistant")
st.markdown("Welcome to your personal chatbot! 🚀 Ask questions about news, weather, and more.")
st.write("---")

# Sidebar
st.sidebar.title("About This App")
st.sidebar.markdown("""
This chatbot uses:
- **Flask** for the backend.
- **Streamlit** for the frontend.
- APIs for fetching news, weather, and Wikipedia information.
""")

# Instructions
st.markdown("""
### How to Use:
1. Type your question in the input box below.
2. Examples:
   - "What's the latest news?"
   - "Tell me about Python on Wikipedia."
   - "What's the weather in New York?"
3. Press the "Send" button to get a response.
""")
st.write("---")

# Input and response
user_input = st.text_input("Enter your message:")
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a valid message!")
    else:
        try:
           response = requests.post(
    "https://730e-103-97-242-255.ngrok-free.app/chat",
    json={"message": user_input}
)

            if response.status_code == 200:
                bot_response = response.json().get("response", "No response received.")
                st.markdown("### 🤖 Chatbot's Response:")
                st.write(bot_response)
            else:
                st.error(f"Error: Received status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Connection error: {e}")

# Footer
st.write("---")
st.write("Powered by Streamlit and Flask.")

