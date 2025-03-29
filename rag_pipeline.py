# Import libraries
from langchain.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY").strip()

def calculate_interest(principal, rate, time):
    """Calculates the interest for deposit schemes."""
    return (principal * rate * time) / 100

def load_rag_pipeline(vector_db_path="vector_store", model_name="GroqLlama"):
    """Loads the RAG pipeline with vector database and Groq’s LLaMA model."""
    # embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    vector_db = Chroma(persist_directory=vector_db_path, embedding_function=embeddings)
    llm = ChatGroq(model_name="llama-3.1-8b-instant")  # Replace with the correct Groq model name
    retriever = vector_db.as_retriever()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        memory=memory
    )
    return rag_chain
