from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser


load_dotenv()



model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0,api_key=os.getenv("GOOGLE_GEMINI_KEY2"))

prompt1=PromptTemplate(
    input_variables=["topic"],
    template="Give me a creative title for a blog post about {topic}.")
prompt2=PromptTemplate(
    input_variables=["title"],
    template="Write a detailed blog post based on the title: {title}.")

parser=StrOutputParser()

seq=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(seq.invoke({"topic":"The future of AI in healthcare"}))
