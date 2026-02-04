from langchain_community.document_loaders import TextLoader
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
def load_text_file(file_path: str):
    """
    Load a text file and return its content.

    Args:
        file_path (str): The path to the text file.   """
    loader=TextLoader(file_path,encoding="utf-8")
    documents = loader.load()
    return documents



file_path='dummy_text.txt'
docs=load_text_file(file_path)


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7,google_api_key=os.getenv("GOOGLE_GEMINI_KEY1"))

template=PromptTemplate(template="Summarize the following text:\n\n{text}",input_variables=["text"])

parser=StrOutputParser()

chain=template|model|parser


print(docs[0].page_content)
print("Summary:")
print(chain.invoke({"text":docs[0].page_content}))


# print(docs)
#
# print(len(docs))
#
# print(type(docs))
#
# print(docs[0])
#
# print(docs[0].page_content)
#
# print(docs[0].metadata)