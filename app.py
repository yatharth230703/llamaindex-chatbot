import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "ENTER YOUR KEY"


# Initialize OpenAI LLM
llm = OpenAI()

# Load data
data = SimpleDirectoryReader(input_dir="C:/Users/yatharth/Desktop/desktop1/AI/ComputerHub/CORPUS").load_data()

# Create an index
index = VectorStoreIndex.from_documents(data)

# Create a chat engine
chat_engine = index.as_chat_engine(chat_mode="react", llm=llm, verbose=True)

# Streamlit app
st.title("LlamaIndex Chatbot")
st.write("Enter 'STOP' to end the conversation.")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.text_input("Enter prompt", key="input")

if st.button("Send"):
    if user_input:
        if user_input.lower() == "stop":
            st.write("Conversation ended.")
        else:
            response = chat_engine.chat(user_input)
            st.session_state["chat_history"].append((user_input, response))
            st.text_area("Chat History", value="\n".join([f"User: {q}\nBot: {a}" for q, a in st.session_state["chat_history"]]), height=400)

