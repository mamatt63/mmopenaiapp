# Import main libraries
import os
from dotenv import load_dotenv 
from openai import AzureOpenAI

# loading variables from .env file
load_dotenv() 

# Authenticate the client using your key and endpoint 
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version="2024-02-01"
)

# Interact with GPT-3.5-turbo deployment
response = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Answer like a pirate."},
        {"role": "user", "content": "Who were the founders of Microsoft?"}
    ]
)

print(response.choices[0].message.content)
