from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import List

from pyexpat.errors import messages

load_dotenv()

api_key=os.getenv("GOOGLE_GEMINI_KEY1")

class Person(BaseModel):
    name: str = Field(...,description="Name of the person")
    age:int=Field(gt=18,description='age of the person must be greater than 18')
    city: str = Field(...,description="City where the person lives")

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite',google_api_key=api_key)
parser=PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(template="give me the dummy information of person of this {place} \n {format_instructions}",input_variables=['place'],
                          partial_variables={"format_instructions":parser.get_format_instructions()})

# result=template.invoke({'place':'Pakistan'})
# output=llm.invoke(result)
# parsed_output=parser.parse(output.content)

chain=template | llm | parser
parsed_output=chain.invoke({'place':'Pakistan'})

print(parsed_output)

