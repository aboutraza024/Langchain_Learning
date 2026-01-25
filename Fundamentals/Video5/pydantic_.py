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

class Message(BaseModel):
    summary:str=Field(..., description="A brief summary of the product review")   # we can also add annotation using annotated from typing which explain a bit about summary
    sentiment:str=Field(..., description="The overall sentiment of the review, e.g., positive")
    pros:Optional[List[str]]= Field(None, description="List of positive aspects of the product")
    cons:Optional[List[str]]= Field(None, description="List of negative aspects of the product")
    themes:Optional[List[str]]= Field(None, description="Key themes mentioned in the review")
    



model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",google_api_key=api_key)
structured_output= model.with_structured_output(Message)
response=structured_output.invoke("""
                                  This product does a few things well, but overall it feels unfinished for the price. The core functionality works as advertised, and the build quality is solid, but the experience is inconsistent and sometimes frustrating.

Pros:
• Sturdy construction — it doesn’t feel cheap and holds up with regular use.
• Setup was straightforward and didn’t require much troubleshooting.
• When it works properly, the performance is decent and reliable.

Cons:
• Performance drops noticeably after extended use, which is disappointing.
• The interface feels outdated and unintuitive, with poor labeling in key areas.
• Customer support was slow to respond and didn’t fully resolve the issue.

Specific issues:
• Battery life fell short of the advertised duration by a noticeable margin.
• Occasional lag and freezing occurred during basic operations.
• Instructions lacked clarity, especially for advanced features.

In its current state, this feels like a mid-tier product priced as a premium one. With better optimization and clearer support, it could be solid — but right now, I’d recommend considering alternatives unless these issues are addressed
                                  """)   

print(type(response))


print(response.summary,"\n\n")
print(response.sentiment,"\n\n")
print(response.pros,"\n\n") 
print(response.cons,"\n\n")
print(response.themes,"\n\n")       