import streamlit as st
import requests

st.set_page_config(
    page_title="Drive AI Agent",
    page_icon="📁",
    layout="wide"
)

st.markdown(
    """
    <style>

    .main {
        background-color: #0f172a;
        color: white;
    }

    .hero {
        padding: 2rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #111827, #1e293b);
        border: 1px solid #334155;
        margin-bottom: 2rem;
        box-shadow: 0px 0px 25px rgba(0,0,0,0.3);
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: white;
    }

    .hero-subtitle {
        font-size: 1.1rem;
        color: #cbd5e1;
        margin-top: 10px;
    }

    .query-box {
        background-color: #111827;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #374151;
        margin-top: 10px;
        margin-bottom: 20px;
        font-size: 16px;
        color: #22c55e;
    }

    .file-card {
        background: linear-gradient(135deg, #1e293b, #111827);
        padding: 20px;
        border-radius: 16px;
        margin-bottom: 18px;
        border: 1px solid #334155;
        transition: 0.3s;
    }

    .file-card:hover {
        transform: scale(1.01);
        border: 1px solid #3b82f6;
    }

    .file-name {
        font-size: 20px;
        font-weight: 700;
        color: white;
        margin-bottom: 8px;
    }

    .file-type {
        color: #cbd5e1;
        margin-bottom: 15px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        color: #94a3b8;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.title("⚡ Drive AI Agent")

    st.markdown("---")

    st.markdown("### 🚀 Features")

    st.markdown("""
    - AI-powered Google Drive search
    - Natural language understanding
    - PDF & image discovery
    - FastAPI backend
    - Streamlit frontend
    - Groq LLM integration
    """)

    st.markdown("---")

    st.markdown("### 💡 Example Queries")

    st.code("Find resume pdf")
    st.code("Find screenshots")
    st.code("Find image files")
    st.code("Find pdf documents")


st.markdown(
    """
    <div class="hero">
        <div class="hero-title">📁 Drive AI Agent</div>
        <div class="hero-subtitle">
            Search Google Drive using natural language powered by AI.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


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
                "https://g-drive-ai-agent-production.up.railway.app",
                json={"message": prompt}
                )
            

                data = response.json()

                st.success("Search completed successfully!")

                
                st.markdown("### 🧠 Generated Query")

                st.markdown(
                    f'<div class="query-box">{data["generated_query"]}</div>',
                    unsafe_allow_html=True
                )

                files = data["files"]

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
                    "content": "Search completed",
                    "query": data["generated_query"],
                    "files": files
                })

            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown(
    """
    <div class="footer">
        Built using FastAPI • Streamlit • Groq • Google Drive API
    </div>
    """,
    unsafe_allow_html=True
)

