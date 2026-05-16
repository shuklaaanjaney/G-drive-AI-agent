from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq model
llm = ChatGroq(
   model="llama-3.3-70b-versatile"
)

def generate_query(user_message):

    prompt = f"""
    You are a Google Drive search assistant.

    Convert the user's request into a valid Google Drive API q query.

    Examples:

    User: Find resume PDFs
    Query:
    name contains 'resume' and mimeType='application/pdf'

    User: Find image files
    Query:
    mimeType contains 'image/'

    User: Find screenshots
    Query:
    name contains 'Screenshot'

    Only return the query.

    User request:
    {user_message}
    """

    response = llm.invoke(prompt)

    return response.content