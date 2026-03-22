import os
from openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings

from transformers import pipeline


class RAGChatbot:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.db = None

        
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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",
            default_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title": "RAG Project"
            }
        )
#         self.llm = pipeline(
#             "text-generation",
#             model="google/flan-t5-base",
#             max_length=512
#       )

    def load_and_process(self):
        loader = PyPDFLoader(self.pdf_path)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_documents(docs)

        # ✅ HuggingFace embeddings (free)
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        self.db = FAISS.from_documents(chunks, embeddings)

    def ask(self, query):
        retriever = self.db.as_retriever(search_kwargs={"k": 3})

        # ✅ new method
        docs = retriever.invoke(query)

        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
        Answer only from the context below:
        {context}

        Question: {query}
        """

        # ✅ OpenRouter call
        response = self.client.chat.completions.create(
            model="nvidia/nemotron-3-super-120b-a12b:free",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content