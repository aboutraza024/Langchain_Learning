from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("dummy.pdf")
document=loader.load()
splitter=CharacterTextSplitter(chunk_size=100,chunk_overlap=0,separator="")
result=splitter.split_documents(document)

print(len(result))

print(result[0].metadata,"\n\n\n")
print(result[0].page_content)

