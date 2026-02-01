from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0,api_key=os.getenv("GOOGLE_GEMINI_KEY2"))

prompt1=PromptTemplate(
    input_variables=["topic"],
    template="Give me a small creative tweet for a twitter post about {topic}.")
prompt2=PromptTemplate(
    input_variables=["title"],
    template="Write a small post based on the title for linkedin : {topic}.")

parser=StrOutputParser()

par=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin post':RunnableSequence(prompt2,model,parser)
}
)

result = par.invoke({"topic": "AI"})

print("\n--- TWEET ---\n")
print(result["tweet"])

print("\n--- LINKEDIN POST ---\n")
print(result["linkedin post"])

