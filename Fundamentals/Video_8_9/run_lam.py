from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def word_count(text: str) -> int:
    return len(text.split())

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0,api_key=os.getenv("GOOGLE_GEMINI_KEY2"))


prompt=PromptTemplate(
    input_variables=["topic"],
    template="Give me a joke about {topic}.")
parser=StrOutputParser()

joke_runnable=RunnableSequence(prompt,model,parser)

#lambda Runnable

parallel_runnable=RunnableParallel({
    'joke':joke_runnable,
    'word_count':RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_runnable,parallel_runnable)

result=final_chain.invoke({"topic":"chickens"})
print(result)