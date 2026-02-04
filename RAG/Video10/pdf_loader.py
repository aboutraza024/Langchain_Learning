from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("data/dna article.pdf")
documents = loader.load()
# print(documents)
# print(len(documents))
# print(type(documents))
print(documents[0].page_content)
print(len(documents[0].page_content))
print(documents[0].metadata)