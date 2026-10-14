from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import warnings
import os

warnings.filterwarnings('ignore', category=UserWarning)

load_dotenv()

embeddingModel = HuggingFaceEmbeddings(
    model='sentence-transformers/all-MiniLM-L6-v2',
    encode_kwargs={"batch_size": 64}
)

DB_PATH = "faiss_algorithm_index"

if os.path.exists(DB_PATH):
    print("Loading existing FAISS index from disk...")
    vector_store = FAISS.load_local(
        DB_PATH, 
        embeddingModel, 
        allow_dangerous_deserialization=True
    )
    print("Index loaded instantly from cache!")
else:
    print("Index not found. Processing and embedding PDF in batches...")
    loader = PyPDFLoader("PDFs/Introduction_To_Algorithms.pdf")
    docs = loader.load()
    total_pages = len(docs)
    batch_size = 50

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=300,
        length_function=len,
        separators=["\n\n", "\n", ".", " "]
    )

    vector_store = None
    for i in range(0, total_pages, batch_size):
        batch_pages = docs[i:i+batch_size]
        batch_chunk = splitter.split_documents(batch_pages)
        
        if vector_store is None:
            vector_store = FAISS.from_documents(batch_chunk, embeddingModel)
        else:
            vector_store.add_documents(batch_chunk)

    vector_store.save_local(DB_PATH)
    print("Batch ingestion complete and index saved locally!")


query = 'What is dynamic programming?'
k_value = 3

result = vector_store.similarity_search(query, k=k_value)

print(type(result))
print(len(result))
for matchedResult in result:
    print(matchedResult)