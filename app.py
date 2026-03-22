import streamlit as st
from rag_pipeline import RAGChatbot

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("📄 RAG PDF Chatbot 🤖")

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    # Save file
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")

    # Initialize bot (only once)
    if "bot" not in st.session_state:
        st.session_state.bot = RAGChatbot("temp.pdf")
        st.session_state.bot.load_and_process()

    # Chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Input
    query = st.text_input("Ask something about your PDF:")

    if query:
        with st.spinner("Thinking... 🤔"):
            answer = st.session_state.bot.ask(query)

        st.session_state.chat_history.append(("You", query))
        st.session_state.chat_history.append(("Bot", answer))

    # Display chat
    for role, text in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**🧑 {role}:** {text}")
        else:
            st.markdown(f"**🤖 {role}:** {text}")