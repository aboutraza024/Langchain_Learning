from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import  load_dotenv
from sympy.codegen.fnodes import dimension

load_dotenv()

model=GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001')
#result=model.embed_query("HI ALI I HOPE YOU ARE DOING WELL")  # for single query


document=["MIAN ALI","KHOKHAR DON","SIAL SAAB"]
result=model.embed_documents(document)  # for multiple query or text

print(len(str(result)))
print(str(result))
