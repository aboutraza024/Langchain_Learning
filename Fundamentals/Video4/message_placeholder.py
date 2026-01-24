from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.getenv("GOOGLE_GEMINI_KEY1")

chat_history=[]
with open("D:\PythonProject\LANGCHAIN\Fundamentals\Video4\history.txt","r") as file:
    chat_history.extend(file.readlines())
    
print(chat_history)


chat_template = ChatPromptTemplate.from_messages(
    [
        ('system',"You are a helpful Customer Support."),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human',"what's about my {query}.")
    ]
)

prompt=chat_template.invoke({"chat_history": chat_history,'query':"refund"})
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",google_api_key=api_key)
response=model.invoke(prompt)  # check this prompt
print(response.content) 