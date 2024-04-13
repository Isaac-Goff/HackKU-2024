from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

#System helps set the tone for the Assistant. It is optional
#User will provide requests or comments for the assistant to respond to. Kinda like the regular API 
#Assistant are model responses
        
env = load_dotenv(find_dotenv())
connect = OpenAI()
connect.api_key = os.getenv("OPENAI_API_KEY")
response = connect.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "system", "content": "You are a unbiased assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
  ]
)

print(response.choices[0].message.content)