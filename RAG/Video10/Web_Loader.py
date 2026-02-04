from langchain_community.document_loaders import TextLoader,WebBaseLoader
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
def load_text_file():
    """
    Load a text file and return its content.

    Args:
        file_path (str): The path to the text file.   """
    urls=['https://www.olx.com.pk/item/macbook-air-pro-m1-m2-m3-m4-13-14-16inch-lush-condition-iid-1065072085'] # also we can use list of url's
    loader=WebBaseLoader(urls)
    documents = loader.load()
    return documents



data=load_text_file()


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7,google_api_key=os.getenv("GOOGLE_GEMINI_KEY1"))

template=PromptTemplate(template="Give me the answer of following {question} from this {text}",input_variables=["question","text"])

parser=StrOutputParser()

chain=template|model|parser


print(data[0].page_content)
print("Summary:")
print(chain.invoke({"question":"Name and price of product","text":data[0].page_content}))


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