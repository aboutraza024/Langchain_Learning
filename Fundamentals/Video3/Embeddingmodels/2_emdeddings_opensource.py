#we can also do that using inference api like chatmodel infernece api example

from langchain_huggingface import HuggingFaceEmbeddings

model=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
result=model.embed_query("islamabad is capital of pakistan")

# document=["MIAN ALI","KHOKHAR DON","SIAL SAAB"]
# result=model.embed_documents("islamabad is capital of pakistan")  # for multiple documents embeddings
print(str(result))