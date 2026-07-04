import os
from groq import Groq
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def improve_bullet_point(bullet_text):
    """
    Takes a weak resume bullet point and returns an improved version.
    """
    prompt = f"""
You are a professional resume writer. Rewrite the following resume bullet point 
to be more impactful, using strong action verbs and quantifiable results where 
reasonable. Keep it to ONE line. Do not add fake numbers if none are implied — 
instead focus on clarity and impact.

Original bullet point: "{bullet_text}"

Return ONLY the improved bullet point, nothing else.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


# quick test
if __name__ == "__main__":
    weak_bullet = "Worked on project using Python and machine learning."
    improved = improve_bullet_point(weak_bullet)

    print("Original:", weak_bullet)
    print("Improved:", improved)