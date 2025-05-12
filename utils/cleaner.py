import re
from typing import List
from langchain_core.documents import Document

def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\S\r\n]+", " ", text)
    return text.strip()

def clean_documents(docs: List[Document]) -> List[Document]:
    cleaned = []
    for doc in docs:
        doc.page_content = clean_text(doc.page_content)
        cleaned.append(doc)
    return cleaned
