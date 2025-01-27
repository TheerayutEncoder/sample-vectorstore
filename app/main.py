import os

import streamlit as st
from utils import process_message

st.set_page_config(page_title="AI Chat Portal", layout="wide")


# Ensure the src folder exists for saving uploaded files
os.makedirs("src", exist_ok=True)


def list_uploaded_files(folder="src"):
    """List files in the specified folder."""
    return os.listdir(folder)


def main():
    st.title("AI Chat Portal")
    st.markdown("---")

    # Initialize session state to store chat history and input
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    if "user_input" not in st.session_state:
        st.session_state["user_input"] = ""

    # Left Sidebar: File Upload and Display
    with st.sidebar:
        st.header("Uploaded Files")
        uploaded_file = st.file_uploader("Upload a file:", type=["txt", "pdf", "docx"])
        if uploaded_file:
            file_path = os.path.join("src", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"File saved: {uploaded_file.name}")

        st.subheader("Files in 'src' Folder:")
        uploaded_files = list_uploaded_files()
        if uploaded_files:
            for file in uploaded_files:
                st.markdown(f"- {file}")
        else:
            st.write("No files uploaded yet.")

    # Main chat layout
    chat_container = st.container()
    with chat_container:
        # Display chat history above the input box
        st.subheader("Chat History:")
        for user_message, ai_response in st.session_state["chat_history"]:
            st.markdown(f"**You:** {user_message}")
            st.markdown(f"**AI:** {ai_response}")
            st.markdown("---")

    # Chat Input and Response at the bottom
    input_container = st.container()
    with input_container:
        st.session_state["user_input"] = st.text_input("Enter your message:", st.session_state["user_input"])
        if st.button("Send"):
            if st.session_state["user_input"].strip():
                # Process the user message
                response = process_message(st.session_state["user_input"])

                # Append the chat history
                st.session_state["chat_history"].append((st.session_state["user_input"], response))

                # Clear the input box
                st.session_state["user_input"] = ""

            else:
                st.warning("Please enter a message.")

if __name__ == "__main__":
    main()