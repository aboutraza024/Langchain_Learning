from langchain_text_splitters import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("dummy.pdf")
document=loader.load()
splitter=RecursiveCharacterTextSplitter(chunk_size=350,chunk_overlap=0)
result=splitter.split_text("""
Imran Khan is a prominent Pakistani politician, former cricketer, and philanthropist. Born in 1952 in Lahore, he gained international fame as the captain of Pakistan’s cricket team, leading them to their first and only Cricket World Cup victory in 1992. After retiring from cricket, he focused on social work and founded the Shaukat Khanum Memorial Cancer Hospital & Research Centre, providing free cancer treatment to thousands of patients.

In 1996, Imran Khan entered politics by establishing the Pakistan Tehreek-e-Insaf (PTI) party. Over the years, he became a significant political figure in Pakistan, known for advocating anti-corruption reforms, education, and healthcare improvements. In 2018, he became the 22nd Prime Minister of Pakistan, promising to bring transparency and development to the country
""")

print(len(result))

for r in result:
    print(r)
    print("------")

