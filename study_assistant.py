from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

topic = input("Enter a topic: ")

prompt = f"""
You are an AI Study Assistant.

Explain the topic: {topic}

Give the answer in this format:

1. Simple Explanation
2. Real-world Example
3. Three Important Points
4. One Quiz Question

Use very simple English for a beginner.
"""

print("\nAI Study Assistant")
print("Topic:", topic)

print("\nGenerated Prompt:")
print(prompt)