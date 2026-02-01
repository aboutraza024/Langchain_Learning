from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=1,api_key=os.getenv("GOOGLE_GEMINI_KEY2"))

prompt1=PromptTemplate(
    input_variables=["topic"],
    template="Give me  small 1-2 line joke about {topic}.")

prompt2=PromptTemplate(
    input_variables=["title"],
    template="Write a detailed (5-6 lines) of this joke: {topic}.")

parser=StrOutputParser()
seq=RunnableSequence(prompt1,model,parser)

parallel=RunnableParallel({
    "Joke":RunnablePassthrough(),
    "Explanation":RunnableSequence(prompt2,model,parser)
})


final_runnable=RunnableSequence(
    seq,
    parallel
)

result=final_runnable.invoke({"topic":"cricket"})

print(result['Joke'],"\n\n\n\n\n")

print("\n\n\n\n\n",result['Explanation'])
