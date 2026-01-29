from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=1,api_key=os.getenv("GOOGLE_GEMINI_KEY1"))

prompt=PromptTemplate(template='Create 5 facts about {topic}', input_variables=['topic'])

parser=StrOutputParser()

chain=prompt|model|parser
result=chain.invoke({'topic':'cricket'})
print(result)
chain.get_graph().print_ascii()  # to visualize the chain structure
