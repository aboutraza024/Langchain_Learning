from langchain_community.document_loaders import CSVLoader
loader=CSVLoader(file_path='sample_data.csv',encoding='utf-8')

docs=loader.load()
print(len(docs))


print(docs[0].page_content,"\n\n\n")
print(docs[0].metadata)