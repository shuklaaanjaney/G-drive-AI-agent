import streamlit as st
import requests


st.set_page_config(
    page_title="Drive AI Agent",
    page_icon="📁",
    layout="wide"
)


st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #020617;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background-color: #020617;
}

.hero {
    padding: 2.5rem;
    border-radius: 24px;
    background: linear-gradient(135deg, #111827, #1e293b);
    border: 1px solid #334155;
    margin-bottom: 2rem;
}

.hero-title {
    font-size: 3.5rem;
    font-weight: 800;
    color: white;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #cbd5e1;
    margin-top: 10px;
}

.query-box {
    background-color: #111827;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #334155;
    margin-top: 10px;
    margin-bottom: 20px;
    color: #22c55e;
    font-size: 16px;
}

.file-card {
    background: linear-gradient(135deg, #1e293b, #111827);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 18px;
    border: 1px solid #334155;
}

.file-name {
    font-size: 20px;
    font-weight: 700;
    color: white;
}

.file-type {
    color: #cbd5e1;
    margin-top: 8px;
    margin-bottom: 15px;
}

.footer {
    text-align: center;
    margin-top: 40px;
    color: #94a3b8;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)



with st.sidebar:

    st.title("⚡ Drive AI Agent")

    st.markdown("---")

    st.markdown("## 🚀 Features")

    st.markdown("""
    - AI-powered Google Drive Search
    - Natural Language Understanding
    - PDF & Image Discovery
    - FastAPI Backend
    - Streamlit Frontend
    - Groq LLM Integration
    """)

    st.markdown("---")

    st.markdown("## 💡 Example Queries")

    st.code("Find resume pdf")
    st.code("Find screenshots")
    st.code("Find image files")
    st.code("Find pdf documents")



st.markdown("""
<div class="hero">
    <div class="hero-title">📁 Drive AI Agent</div>
    <div class="hero-subtitle">
        Search Google Drive using natural language powered by AI.
    </div>
</div>
""", unsafe_allow_html=True)



if "messages" not in st.session_state:
    st.session_state.messages = []



for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

        if msg.get("query"):

            st.markdown("### 🧠 Generated Query")

            st.markdown(
                f'<div class="query-box">{msg["query"]}</div>',
                unsafe_allow_html=True
            )

        if msg.get("files"):

            st.markdown("### 📂 Files Found")

            for file in msg["files"]:

                st.markdown(
                    f"""
                    <div class="file-card">
                        <div class="file-name">📄 {file['name']}</div>
                        <div class="file-type">{file['mimeType']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.link_button(
                    "🔗 Open File",
                    file["webViewLink"]
                )


prompt = st.chat_input("Ask about your Google Drive files...")

if prompt:

   
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })


    with st.chat_message("user"):
        st.markdown(prompt)

    
    with st.chat_message("assistant"):

        with st.spinner("Searching Google Drive..."):

            try:

                response = requests.post(
                    "https://g-drive-ai-agent-production.up.railway.app/chat",
                    json={"message": prompt}
                )

                data = response.json()

                

                query_text = (
                    data.get("generated_query")
                    or data.get("query")
                    or "No query returned"
                )

                files = data.get("files", [])

              

                st.success("Search completed successfully!")

            
                st.markdown("### 🧠 Generated Query")

                st.markdown(
                    f'<div class="query-box">{query_text}</div>',
                    unsafe_allow_html=True
                )


                if len(files) == 0:

                    st.warning("No matching files found.")

                else:

                    st.markdown("### 📂 Files Found")

                    for file in files:

                        st.markdown(
                            f"""
                            <div class="file-card">
                                <div class="file-name">📄 {file['name']}</div>
                                <div class="file-type">{file['mimeType']}</div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        st.link_button(
                            "🔗 Open File",
                            file["webViewLink"]
                        )

            

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": "Search completed successfully!",
                    "query": query_text,
                    "files": files
                })

            except Exception as e:

                st.error(f"Error: {str(e)}")



st.markdown("""
<div class="footer">
    Built using FastAPI • Streamlit • Groq • Google Drive API
</div>
""", unsafe_allow_html=True)

