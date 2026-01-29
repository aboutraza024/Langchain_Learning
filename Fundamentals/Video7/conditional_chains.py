from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Optional,Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch,RunnableLambda
import os
load_dotenv()
class Feedback(BaseModel):
    feedback:Literal['positive','negative']=Field(description='Type of feedback is only positive or negative')

model1=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7,google_api_key=os.getenv("GOOGLE_GEMINI_KEY2"))
parser=PydanticOutputParser(pydantic_object=Feedback)

prompt1= PromptTemplate(template='give the feed back to this {text} \n {format_instructions}', input_variables=['text'], partial_variables={'format_instructions': parser.get_format_instructions()})


chain=prompt1|model1|parser
# result=chain.invoke({'text':'The product was excellent and met all my expectations.'})
# print(result.feedback)

prompt2=PromptTemplate(template="write the appropriate response to this  feedback \n feedback: {feedback}", input_variables=['feedback'])
parser2=StrOutputParser()

response_chain=RunnableBranch(
    (lambda x:x.feedback=='positive',prompt2|model1|parser2),(lambda x:x.feedback=='negative',prompt2|model1|parser2),
    RunnableLambda(lambda x:"No valid feedback provided.")
)

final_chain=chain|response_chain
output=final_chain.invoke({'text':'The product was terrible and broke after one use.'})
print(output)

final_chain.get_graph().print_ascii()


