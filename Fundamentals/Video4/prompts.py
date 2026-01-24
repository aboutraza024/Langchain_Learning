from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
prompt = ChatPromptTemplate.from_messages([
    ("system","you are an help ful ai assitant. your name is {name}"),
    ("human","what is the weather like in {location}?")
])
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",google_api_key=os.getenv("GOOGLE_GEMINI_KEY"))
name=input("Enter bot name:")
location=input("Enter location:")
prompt1=prompt.invoke({"name":name,"location":location})

res=model.invoke(prompt1)
print(res.content)
