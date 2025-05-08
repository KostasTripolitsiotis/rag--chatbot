import streamlit as st
import time
from ipynb.fs.full.retriever import *

st.markdown(
    """
    <style>
        .st-emotion-cache-janbn0 {
            flex-direction: row-reverse;
            text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def response_generator(answer):
    # Simulate a streaming response by yielding each word with a delay
    for word in answer.split():
        yield word + " "
        time.sleep(0.02)

st.title("RAG Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# Accept user input
if prompt := st.chat_input("Ask your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        
    response = ask(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        full_response = ""
        
        for chunk in response:
            # Display the response in chunks
            chunk = st.write_stream(response_generator(chunk))
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": chunk})
    
    
