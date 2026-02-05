from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_GEMINI_KEY1")

embeddings=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001',api_key=api_key)

text_splitter= SemanticChunker(embeddings=embeddings,breakpoint_threshold_type="percentile",breakpoint_threshold_amount=99)

text = """
Technology has transformed the way people work and communicate, making tasks faster and collaboration easier across long distances.
At the same time, education has evolved through online platforms, giving learners access to knowledge anytime and anywhere.

Health is equally important, as maintaining physical and mental well-being helps people stay productive and enjoy a better quality of life.
Regular exercise, balanced nutrition, and adequate rest play a major role in achieving this balance
"""

docs=text_splitter.create_documents([text])

for i,doc in enumerate(docs):
    print(f"--- Document {i+1} ---")
    print(doc.page_content)
    print(f"Metadata: {doc.metadata}")
