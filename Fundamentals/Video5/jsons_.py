# from pydantic import BaseModel,EmailStr,Field,conint
# from typing import List,Optional


# class User(BaseModel):
#     name:str='ali raza'
#     age:Optional[conint(gt=0, lt=150)] = None  # age must be between 0 and 150
#     email:EmailStr
#     cgpa: float = Field(..., ge=0.0, le=4.0, description="cgpa is score of student")  # cgpa must be between 0.0 and 4.0
    

# student={"name": "ali", "age": 25, "email": "itsaaliraza@gmail.com", "cgpa": 3.3}
# new_student=User(**student)
# print(type(new_student))
# print(new_student)








# from typing import TypedDict, Optional


# class output():
#     name:str
#     age:int
    
# dict:output= {'name':'ali','age':25}  #if we use age as string it will work but this typed dict help other colleborter to know the type of value
# print(dict)

from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, List, Optional,Annotated
import os
from pydantic import BaseModel,Field
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GOOGLE_GEMINI_KEY1")

schema = {
    "title": "StudentsData",
    "description": "this is the schema for student data",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "The name of the student"
        },
        "age": {
            "type": "number",
            "description": "The age of the student"
        }
    },
    "required": ["name"]
}
    
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",google_api_key=api_key)
structured_output= model.with_structured_output(schema)
response=structured_output.invoke("""
The student data includes a name and an age. The name is required and must be a text value, while the age is optional and is a number                                  
""")   

print(type(response))
print(response)     



# this was not workding because gemini models does not support json schema yet or langchain cant send json scheme to gemini models.