from google import genai
from google.genai import types
client = genai.Client()
response = client.models.generate_content(
    model='gemma-4-26b-a4b-it',
    config=types.GenerateContentConfig(
        system_instruction='You are a patient tutor. Answer in under 3 sentences.'
    ),
    contents='What is a pull request?',
)
print(response.text)