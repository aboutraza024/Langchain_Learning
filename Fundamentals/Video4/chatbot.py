from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.getenv("GOOGLE_GEMINI_KEY")
chat_history=[SystemMessage(content="You are a helpful AI assistant.")]
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",google_api_key=api_key)
while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break
    else:
        chat_history.append(HumanMessage(content=user_input))
        response=model.invoke(chat_history)
        chat_history.append(AIMessage(content=response.content))
print("AI:", chat_history)