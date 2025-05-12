from langchain.chat_models import ChatOpenAI
from config import settings

llm = ChatOpenAI(api_key=settings.openai_api_key, temperature=0)

def evaluate_response(query: str, answer: str, context_chunks: list[str]) -> dict:
    context = "\n\n".join(context_chunks)
    eval_prompt = f"""
Evaluate the following answer to a user query based on the given context.
Respond only with a JSON object like {{"faithfulness": 0.0–1.0, "relevance": 0.0–1.0}}.

Query: {query}
Answer: {answer}
Context: {context}
"""
    response = llm.predict(eval_prompt)
    try:
        return eval(response)
    except:
        return {"faithfulness": 0.0, "relevance": 0.0}
