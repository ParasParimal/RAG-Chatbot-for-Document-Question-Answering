# 📄 RAG-Based PDF Chatbot (LLM + FAISS + Streamlit)

## 🚀 Overview

This project is an **end-to-end Retrieval-Augmented Generation (RAG) chatbot** that allows users to upload PDF documents and ask questions based on their content.
It uses **vector embeddings + similarity search + LLMs** to provide accurate, context-aware answers.

---

## 🧠 How It Works

1. 📄 User uploads a PDF
2. ✂️ Document is split into smaller chunks
3. 🔢 Chunks are converted into embeddings (vector representation)
4. 🗂️ Stored in a FAISS vector database
5. 🔍 Relevant chunks are retrieved based on user query
6. 🤖 LLM generates answer using retrieved context

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **FAISS (Vector Database)**
* **HuggingFace Embeddings**
* **OpenRouter (LLM API)**
* **Streamlit (UI)**

---

## 📁 Project Structure

```
RAG/
│
├── rag_pipeline.py   # Core RAG logic
├── app.py            # Streamlit UI
├── test.py           # CLI testing (optional)
├── temp.pdf          # Temporary uploaded file
```

---

## ⚙️ Installation


### 1. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 2. Install Dependencies

```bash
pip install openai langchain langchain-community langchain-text-splitters faiss-cpu pypdf sentence-transformers streamlit
```

---

## 🔑 Setup API Key (OpenRouter)

### Set environment variable:

```powershell
setx OPENROUTER_API_KEY "your_api_key_here"
```

⚠️ Restart VS Code after setting the key

---

## ▶️ Run the Application

### 🔹 Streamlit UI

```bash
streamlit run app.py
```

### 🔹 CLI Mode (optional)

```bash
python test.py
```

---

## 💡 Features

* 📄 Upload and query PDF documents
* 🔍 Context-aware answers using RAG
* ⚡ Fast similarity search with FAISS
* 🤖 LLM-powered response generation
* 🌐 Interactive Streamlit UI

---

## 🎯 Use Cases

* Document Question Answering
* Research Paper Analysis
* Resume / Report Analysis
* Knowledge Base Chatbots

---

## 🧠 Key Concepts Used

* Retrieval-Augmented Generation (RAG)
* Vector Embeddings
* Semantic Search
* Large Language Models (LLMs)

---

## 📌 Future Improvements

* Multiple PDF support
* Source citation (showing document references)
* Chat memory
* Deployment (Streamlit Cloud / HuggingFace Spaces)

---

## 🧑‍💻 Author

**Paras Parimal**

---

