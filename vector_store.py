# Import libraries
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

# Load environment variables
load_dotenv()
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY")

def store_embeddings(data_path="data", vector_db_path="vector_store"):
    """Loads text data from multiple files, splits, and stores embeddings in ChromaDB."""
    # embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    all_docs = []
    for file in os.listdir(data_path):
        file_path = os.path.join(data_path, file)
        loader = TextLoader(file_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        docs = text_splitter.split_documents(documents)
        all_docs.extend(docs)
    
    vector_db = Chroma.from_documents(all_docs, embeddings, persist_directory=vector_db_path)
    print("Vector database created successfully.")

if not os.path.exists("vector_store"):
    store_embeddings()