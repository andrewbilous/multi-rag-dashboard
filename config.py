import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    embedding_model_name = os.getenv("EMBED_MODEL", "thenlper/gte-small")
    llm_model_name = os.getenv("LLM_MODEL", "gpt-4")
    provider = os.getenv("LLM_PROVIDER", "openai")
    vectorstore_path = os.getenv("VECTORSTORE_PATH", "vectorstore/faiss_index")
    upload_folder = os.getenv("UPLOAD_FOLDER", "data/uploads")
    chunk_size = int(os.getenv("CHUNK_SIZE", 500))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", 50))
    temperature = float(os.getenv("TEMPERATURE", 0.2))
    top_p = float(os.getenv("TOP_P", 0.9))
    max_tokens = int(os.getenv("MAX_TOKENS", 1024))
    eval_threshold = float(os.getenv("EVAL_THRESHOLD", 0.7))
    openai_api_key = os.getenv("OPENAI_API_KEY","sk-proj")

settings = Settings()
