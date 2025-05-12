from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from config import settings
import uuid

print('Settings',settings)
embedding_model = OpenAIEmbeddings(settings.openai_api_key)

def embed_and_store(chunks: list[str]):
    docs = [
        Document(page_content=chunk.page_content, metadata={"id": str(uuid.uuid4()), **chunk.metadata})
        for chunk in chunks
    ]
    vectorstore = FAISS.from_documents(docs, embedding_model)
    vectorstore.save_local(settings.vectorstore_path)
    print(f"✅ Stored {len(docs)} chunks in vector DB")

def load_vectorstore():
    if not os.path.exists(settings.vectorstore_path):
        raise ValueError("Vector store not found. Run embed_and_store() first.")
    return FAISS.load_local(settings.vectorstore_path, embeddings=embedding_model, allow_dangerous_deserialization=True)

def retrieve_similar_chunks(query: str, k: int = 4) -> list:
    vectorstore = load_vectorstore()
    return vectorstore.similarity_search(query, k=k)
