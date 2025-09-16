from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import  load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()
model=GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001')
cricketers = [
    "Imran Khan guided Pakistan to their first-ever World Cup triumph in 1992 and is remembered as one of the game’s greatest leaders.",
    "Wasim Akram earned worldwide fame as the Sultan of Swing for his unmatched fast bowling skills.",
    "Shahid Afridi thrilled fans with his explosive batting and became a crowd favorite for his fearless style.",
    "Babar Azam is admired as a modern batting maestro, known for his elegance and consistency.",
    "Shaheen Afridi has emerged as a fearsome left-arm pacer who often provides Pakistan with crucial early wickets."
]
query="tell me about shahid Afridi"
emdeb_data=model.embed_documents(cricketers)
emdeb_query=model.embed_query(query)

similarity=cosine_similarity([emdeb_query],emdeb_data)
import numpy as np
score=similarity.flatten()
index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print("the answer is : ",cricketers[index])