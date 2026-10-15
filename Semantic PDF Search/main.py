from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import warnings
import os

load_dotenv()
# To ignore pdf font warnings
warnings.filterwarnings('ignore', category=UserWarning)

embeddingModel = HuggingFaceEmbeddings(
    model='sentence-transformers/all-MiniLM-L6-v2',
    encode_kwargs={"batch_size": 64}
)

pdf_files = [
    "PDFs/Introduction_To_Algorithms.pdf",
    "PDFs/CompetitiveProgramming4Book2.pdf",
    "PDFs/Competitve_Programmers_Handbook.pdf",
    "PDFs/The_Algorithm_Design_Manual.pdf",
    "PDFs/Grokking_Algorithms.pdf",
]

DB_PATH = "faiss_algorithm_context_index"


if os.path.exists(DB_PATH):
    print("Loading existing FAISS index from disk...")
    vector_store = FAISS.load_local(
        DB_PATH, 
        embeddingModel, 
        # To allow loading untrusted vector db instead of allowing
        # to create new every time the script is run
        allow_dangerous_deserialization=True
    )
    print("Index loaded instantly from cache!")
else:
    print("Generating Embeddings...")
    vector_store = None
    for pdf in pdf_files:
        # Load file one by one
        loader = PyPDFLoader(pdf)
        docs = loader.load()
        total_pages = len(docs)
        number_of_pages = 50
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=300,
            length_function=len,
            separators=["\n\n", "\n", ".", " "]
        )
        for i in range(0, total_pages, number_of_pages):
            batch_pages = docs[i:i+number_of_pages]
            # splitting the batch pages into chunks
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