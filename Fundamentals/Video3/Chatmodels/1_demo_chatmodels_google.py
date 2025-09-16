import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=os.getenv("GOOGLE_GEMINI_KEY"))
response = model.invoke("CAPITAL OF PAKISTAN")
print(response.content)
