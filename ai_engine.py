from google import genai

client = genai.Client(api_key="AIzaSyDwgxGCk5vzhX5GxH11sk2EtTw8Gj2nn3U")


def generate_question(domain, level):
    prompt = f"""
    You are a professional interview panel.

    Ask one {level} level interview question for {domain}.
    Only ask the question.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


import json

def evaluate_answer(question, user_answer):
    prompt = f"""
You are an interview evaluator.

Question: {question}
Candidate Answer: {user_answer}

Respond ONLY in valid JSON format:
{{
  "score": number (0-10),
  "strengths": "text",
  "weaknesses": "text",
  "ideal_answer": "text"
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    return json.loads(response.text)