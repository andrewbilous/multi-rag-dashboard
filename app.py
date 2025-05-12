import streamlit as st
from utils.parser import parse_file
from chunking import recursive_chunk
from embedding_utils import embed_and_store, retrieve_similar_chunks
from rag_chain import generate_answer
from evaluator import evaluate_response
import os
import pandas as pd
import altair as alt

st.set_page_config(page_title="RAG Search with Eval", layout="wide")
st.title("📚 RAG Search with Evaluation Dashboard")

with st.sidebar:
    view_logs = st.checkbox("📈 Show Evaluation Logs")

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join("data/uploads", uploaded_file.name)

        if uploaded_file.type != "application/pdf" or not uploaded_file.name.endswith(".pdf"):
            st.error(f"❌ Skipping {uploaded_file.name}: not a valid PDF.")
            continue

        max_size_mb = 10
        file_size_mb = len(uploaded_file.getbuffer()) / (1024 * 1024)
        if file_size_mb > max_size_mb:
            st.warning(f"⚠️ Skipping {uploaded_file.name}: size {file_size_mb:.2f}MB > {max_size_mb}MB.")
            continue

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ Uploaded: {uploaded_file.name}")

        with st.spinner(f"🔍 Extracting & chunking: {uploaded_file.name}"):
            documents = parse_file(file_path)

            if not documents or all(not doc.page_content.strip() for doc in documents):
                st.error(f"❌ Could not extract any usable text from {uploaded_file.name}")
                continue

            chunks = recursive_chunk(documents)

            for chunk in chunks:
                chunk.metadata = {"source": uploaded_file.name}

            st.info(f"📄 {uploaded_file.name}: Split into {len(chunks)} chunks")

            embed_and_store(chunks)
            st.success(f"🧠 {uploaded_file.name}: Embeddings created and stored!")


st.markdown("---")
st.subheader("🔎 Ask a question")

query = st.text_input("Enter your question below")

if query:
    with st.spinner("🤖 Generating answer..."):
        context_chunks = retrieve_similar_chunks(query)

        texts = [doc.page_content for doc in context_chunks]

        answer = generate_answer(query, texts)
        eval_score = evaluate_response(query, answer, texts)

    st.markdown("### 💬 Answer")
    st.success(answer)

    st.markdown("### 📚 Context Chunks Used")
    for i, doc in enumerate(context_chunks):
        with st.expander(f"Chunk #{i+1} — Source: {doc.metadata.get('source', 'unknown')}"):
            st.write(doc.page_content)

    st.markdown("### 📏 Evaluation")
    st.metric("Faithfulness", value=eval_score["faithfulness"])
    st.metric("Relevance", value=eval_score["relevance"])

if view_logs:
    st.markdown("## 📊 Evaluation Logs")
    try:
        df = pd.read_csv("eval_results/log.csv")
        st.dataframe(df.sort_values("timestamp", ascending=False), use_container_width=True)

        st.markdown("### 🔵 Faithfulness Distribution")
        chart1 = alt.Chart(df).mark_bar().encode(
            alt.X("faithfulness:Q", bin=True),
            y='count()',
        )
        st.altair_chart(chart1, use_container_width=True)

        st.markdown("### 🟢 Relevance Distribution")
        chart2 = alt.Chart(df).mark_bar().encode(
            alt.X("relevance:Q", bin=True),
            y='count()',
        )
        st.altair_chart(chart2, use_container_width=True)

    except Exception as e:
        st.warning(f"⚠️ Could not load logs: {e}")
