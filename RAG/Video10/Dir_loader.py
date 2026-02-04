from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    "data",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# documents=loader.load()
# print(f"Loaded {len(documents)} documents")
#
# print(documents[0].page_content,"\n\n\n")
#
# print(documents[0].metadata,"\n\n\n")
#
#
# print(documents[-1].page_content)
# print(documents[-1].metadata)

# this code is very slow brcause ut is loading all pdf once and it was taking times to load files. and also it would not be possible to load all file in memoery at once if we have 100000 file then ?
# solution is to use lazy loading


# documents=loader.load()       # it will take time to load all files and then start printing metadata
# for docs in documents:
#     print(docs.metadata)


documents=loader.lazy_load()     # it will not take time to load all files and start printing metadata as it loads one by one and start printing one by one
for docs in documents:
    print(docs.metadata)
