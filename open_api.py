from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

env = load_dotenv(find_dotenv())
connect = OpenAI()
connect.api_key = os.getenv("OPENAI_API_KEY")

#System helps set the tone for the Assistant. It is optional
#User will provide requests or comments for the assistant to respond to. Kinda like the regular API 
#Assistant are model responses

response = connect.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

#print(response.choices[0].message.content)