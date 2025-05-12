from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from config import settings

llm = ChatOpenAI(
    api_key=settings.openai_api_key,
    temperature=0,
    model_name="gpt-4"
)

def generate_answer(question: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)
    prompt = f"Answer the question based only on the following context:\n{context}\n\nQuestion: {question}"
    response = llm.predict(prompt)
    return response
