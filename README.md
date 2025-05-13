# 📚 RAG Search with Evaluation Dashboard

This tool allows you to upload PDF documents, ask questions about them, and receive answers generated using Retrieval-Augmented Generation (RAG). It also evaluates the quality of each response using faithfulness and relevance metrics.

---

## 🚀 Features

- 📥 Upload multiple PDF files
- 🧠 Chunk and embed the documents
- 🔍 Ask natural language questions
- 🤖 Receive answers powered by LLMs + document context
- 📈 Visualize monthly evaluation metrics
- 📊 Faithfulness & Relevance score charts
- 🔐 Paste your own OpenAI API key securely
- 📬 Logs stored for later analysis

---

## 🧩 Tech Stack

- **Frontend/UI**: Streamlit
- **Backend AI**: OpenAI API (configurable key)
- **Embeddings**: FAISS Vector Store + LangChain
- **Evaluation**: Custom evaluator logic
- **Charts**: Altair
- **PDF Parsing**: LangChain-compatible loaders

---

## 🛠 Installation

```bash
git clone https://github.com/yourusername/rag-eval-dashboard.git
cd rag-eval-dashboard
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## ⚙️ Usage

```bash
streamlit run app.py
```

Then open your browser to: [http://localhost:8501](http://localhost:8501)

---

## 🔐 API Key Required

To use the app, you’ll need an OpenAI API key. You can get it here:  
👉 https://platform.openai.com/account/api-keys

Paste the key into the input field at the top of the app.

---

## 📦 Folder Structure

```
.
├── app.py
├── chunking.py
├── config.py
├── embedding_utils.py
├── evaluator.py
├── rag_chain.py
├── utils/
│   └── parser.py
├── data/uploads/
├── vectorstore/
└── eval_results/
```
