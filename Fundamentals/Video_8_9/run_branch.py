from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableBranch,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from pyexpat.errors import messages

load_dotenv()



model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0,api_key=os.getenv("GOOGLE_GEMINI_KEY1"))

prompt1=PromptTemplate(template='give me report on this {topic}',input_variables=['topic'])
prompt2=PromptTemplate(template='summarize this report on {topic}',input_variables=['topic'])

parser=StrOutputParser()

seq1=RunnableSequence(prompt1,model,parser)

chain_2=RunnableBranch(
    (lambda x:len(x.strip())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(seq1,chain_2)

print(final_chain.invoke({"topic":"COmputer science"}))