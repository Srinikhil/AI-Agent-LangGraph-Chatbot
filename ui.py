import streamlit as st
import requests


st.set_page_config(page_title="LangGraph AI Agent Chatbot", page_icon="🤖", layout="centered")


API_URL = "http://127.0.0.1:8000/chat"

MODEL_NAMES = [
    "llama3-70b-8192",
    "distil-whisper-large-v3-en",
    "gemma2-9b-it",
    "mixtral-8x7b-32768"
]


st.title("LangGraph AI Agent Chatbot 🤖")
st.write("You can interact with selected model and LangGraph Agent here.")

agent_system_prompt = st.text_area("Define your AI Agent", height=10, placeholder="Example: You are a Data Scientist...")

selected_model = st.selectbox("Select Model", MODEL_NAMES)

user_input = st.text_area("Enter your message", height=150, placeholder="Type your message / question here...")


if st.button("Send"):
    if user_input.strip():
        try:
            payload = {"messages": [user_input], "model_name": selected_model, "system_prompt": agent_system_prompt}
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    model_responses = [
                        message.get("content", "")
                        for message in response_data.get("messages", [])
                        if message.get("type") == "ai"
                    ]

                    if model_responses:
                        st.subheader("AI Agent's Response")
                        st.markdown(f"{model_responses[-1]}")

                    else:
                        st.warning("Sorry, I couldn't understand your question, please try again.")

            else:
                st.error(f"Request failed with statis code {response.status_code}.")
        except Exception as e:
            st.error(f"An error occured while trying to request your prompt ({e})")
    else:
        st.warning("Your message/prompt is empty. Please type a message before sending it.")