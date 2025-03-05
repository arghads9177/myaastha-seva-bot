import streamlit as st
from rag_pipeline import load_rag_pipeline

# Load RAG pipeline
rag_chain = load_rag_pipeline()

# Streamlit UI
st.title("Aastha Seva AI Bot")
st.write("Welcome to Aastha Co-operative Credit Society Ltd. is a leading financial institution in India.")
st.write("Ask me anything about our services!")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_query = st.text_input("Enter your question:")

if user_query:
    # Get response from the QA chain
    response = rag_chain.invoke(user_query)
    # Update chat history
    st.session_state.chat_history.append(f"User: {user_query}")
    st.session_state.chat_history.append(f"AI: {response['result']}")
    
    # Display chat history
    st.write("### Chat History")
    for message in st.session_state.chat_history:
        st.write(message)