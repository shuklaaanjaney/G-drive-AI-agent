import streamlit as st
import requests

# Page title
st.title("📁 Drive AI Agent")

# Chat input
message = st.chat_input("Ask about your files...")

# If user sends message
if message:

    # Show user message
    with st.chat_message("user"):
        st.write(message)

    # Send request to FastAPI backend
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": message}
    )

    data = response.json()

    # Show assistant response
    with st.chat_message("assistant"):

        st.write("### Generated Query")
        st.code(data["generated_query"])

        st.write("### Files Found")

        if len(data["files"]) == 0:
            st.write("No files found.")

        for file in data["files"]:

            st.write(f"📄 {file['name']}")

            st.markdown(
                f"[Open File]({file['webViewLink']})"
            )