# Semantic search from uploaded or loaded pdfs
# knowledge base create karenge in form of embeddings will store them in vector db
# Will ask queries on the basis of that embeddings and match them with the query embedding
# Match cosine similarity whatever the fuck
# output results from that brain or knowledge base insteadd of hallucinating or own knowledge

# Task-1 Document ko load kaise karenge?
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import numpy as np
from langchain_community.vectorstores import FAISS

load_dotenv()
# embeddingModel = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')
embeddingModel = GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')

"""
Document Ingestion Pipeline
- Document Loader(PyPDFLoader)
- Text Splitter(Recursive Character Text Splitter)
- Embeddings Vector Databases(FAISS in this case)
"""
loader = PyPDFLoader("PDFs/Introduction_To_Algorithms.pdf")
docs = loader.load()
total_pages = len(docs)
batch_size = 50

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 300,
    length_function = len,
    separators = ["\n\n", "\n", ".", " "]
)

vector_store = None
for i in range(0, total_pages, batch_size):
    batch_pages = docs[i:i+batch_size]
    batch_chunk = splitter.split_documents(batch_pages)
    
    if vector_store == None:
        vector_store = FAISS.from_documents(batch_chunk, embeddingModel)
    else:
        vector_store.add_documents(batch_chunk)

query = 'What is Divide and Conquer?'
k_value = 3

result = vector_store.similarity_search(query, k_value)

print(type(result))
print(len(result))
for matchedResult in result:
    print(matchedResult)
