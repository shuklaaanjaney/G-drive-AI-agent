from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_query(user_input):

    try:
        prompt = f"""
        Convert the following request into a Google Drive search query.

        Request: {user_input}

        Examples:
        - Find resume pdf
        -> name contains 'resume' and mimeType='application/pdf'

        - Find screenshots
        -> name contains 'Screenshot'

        Only return the query.
        """

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        query = response.choices[0].message.content.strip()

        return query

    except Exception as e:
        print("ERROR:", e)
        return ""