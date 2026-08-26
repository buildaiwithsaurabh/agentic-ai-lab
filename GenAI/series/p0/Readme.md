# 🧠 GenAI & RAG Foundations (Series P0)

A comprehensive hands-on repository covering **Retrieval-Augmented Generation (RAG) pipelines**, **LangChain document processing**, **Vector Embeddings**, **Chroma Vector Database**, and **Agentic AI Workflows**.

---

## 📌 RAG Pipeline Overview

Retrieval-Augmented Generation (RAG) enhances LLMs by connecting them to external knowledge sources. This repository breaks down the full RAG lifecycle into modular, executable Jupyter Notebooks:

```text
┌────────────────┐     ┌──────────────────────┐     ┌────────────────────────┐
│  Data Ingestion│ ──► │  Text Chunking       │ ──► │  Vector Embeddings     │
│  (Doc Loader)  │     │  (Doc Splitter)      │     │  (Gemini Embeddings)   │
└────────────────┘     └──────────────────────┘     └────────────────────────┘
                                                                │
                                                                ▼
┌────────────────┐     ┌──────────────────────┐     ┌────────────────────────┐
│ Final Context  │ ◄── │  Similarity Search   │ ◄── │  Vector Storage        │
│ & LLM Response │     │  (Chroma Retrieval)  │     │  (Chroma DB)           │
└────────────────┘     └──────────────────────┘     └────────────────────────┘
```

---

## 📚 Completed RAG Modules

### 1. 📄 Document Ingestion (`Notebook/RAG_Doc_Loader.ipynb`)
Demonstrates how to extract and load data from heterogeneous sources into standard LangChain `Document` objects:
* **`TextLoader`**: Loads local unstructured files (e.g., `data/DBE.txt`) with custom encoding (`utf-8`).
* **`WebBaseLoader`**: Scrapes dynamic online articles and web pages using `BeautifulSoup4`.
* **`WikipediaLoader`**: Directly queries Wikipedia topics (e.g., *"Generative Artificial Intelligence"*) to extract structured background data.

```python
from langchain_community.document_loaders import TextLoader, WebBaseLoader, WikipediaLoader

# Example: Loading local text document
loader = TextLoader("../data/DBE.txt", encoding="utf-8")
documents = loader.load()
```

---

### 2. ✂️ Text Splitting & Chunking (`Notebook/RAG_Doc_Splitter.ipynb`)
Handles intelligent text segmentation to fit LLM context windows while preserving semantic context:
* **`RecursiveCharacterTextSplitter`**: Recursively splits by paragraphs (`\n\n`), lines (`\n`), and spaces (` `) to keep sentences intact.
* **Configurable Parameters**:
  * `chunk_size`: Maximum character count per chunk (e.g., `1000`).
  * `chunk_overlap`: Overlap between consecutive chunks (e.g., `200`) to prevent context slicing at borders.
* **Document Chunking**: Preserves source metadata (file path, tags) across all split chunk objects.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
text_chunks = splitter.split_documents(documents)
```

---

### 3. 🔮 Embeddings & Vector Database (`Notebook/RAG_Vector.ipynb`)
Converts split text into high-dimensional semantic representations and stores them for instant retrieval:
* **Google Gemini Embeddings**: Uses `GoogleGenerativeAIEmbeddings` with the `gemini-embedding-2-preview` model (producing **3,072-dimensional** vector embeddings).
* **Chroma Vector Store**: Vector database instance persisted locally to `./vector_db` using `langchain_chroma`.
* **Similarity Search**: Performs top-k vector cosine/Euclidean similarity queries (`k=2`) to fetch relevant text chunks based on user prompts.

```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# Generate Embeddings & Store in Chroma DB
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vector_store = Chroma.from_texts(
    texts=documents,
    embedding=embeddings,
    persist_directory="./vector_db"
)

# Querying the Vector Database
query = "semantic meaning"
results = vector_store.similarity_search(query=query, k=2)
```

---

## 📁 Repository Structure

```text
GenAI/series/p0/
│
├── Notebook/
│   ├── RAG_Doc_Loader.ipynb         # Document Loading (Text, Web, Wikipedia)
│   ├── RAG_Doc_Splitter.ipynb       # Chunking with RecursiveCharacterTextSplitter
│   ├── RAG_Vector.ipynb             # Gemini Embeddings, Chroma DB & Querying
│   ├── basic_agents.ipynb           # Intro to AI Agents
│   ├── basic_langchain_with_openai.ipynb # LangChain Open AI Basics
│   ├── groq_langchain.ipynb         # Groq LLM Inference
│   ├── search_agent.ipynb           # Streamlit & LangGraph Search Agent
│   └── vector_db/                   # Local Chroma Vector Database Store
│
├── data/
│   └── DBE.txt                      # Sample dataset for RAG processing
│
├── app/                             # Web research agent app
├── .env                             # Environment variables (API Keys)
├── .gitignore                       # Ignored files & environment binaries
├── requirements.txt                 # Project python dependencies
└── Readme.md                        # Project documentation
```

---

## 🛠️ Tech Stack & Dependencies

| Category | Component / Library | Purpose |
| :--- | :--- | :--- |
| **Language & Environment** | Python 3.13 / `.venv` | Execution environment |
| **Framework** | `langchain` & `langchain-community` | Pipeline orchestration & integrations |
| **Text Processing** | `langchain-text-splitters` | Chunking & text segmentation |
| **Embeddings** | `langchain-google-genai` | Google Gemini vector embeddings (`gemini-embedding-2-preview`) |
| **Vector Storage** | `langchain-chroma` | Persistent vector database (`Chroma`) |
| **Web Data Scrapers** | `beautifulsoup4`, `wikipedia` | Ingesting external web data |
| **Agent / UI** | `streamlit`, `langgraph` | Interactive user interfaces & state memory |
| **Env Management** | `python-dotenv` | Secure API key handling |

---

## ⚙️ Setup & Installation

### 1. Environment Setup

```bash
# Navigate to project directory
cd GenAI/series/p0

# Activate Virtual Environment (Windows)
.venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a `.env` file in `GenAI/series/p0/`:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 3. Running Notebooks

Launch Jupyter Lab or Jupyter Notebook:

```bash
jupyter notebook
```

Navigate to `Notebook/` and run `RAG_Doc_Loader.ipynb`, `RAG_Doc_Splitter.ipynb`, and `RAG_Vector.ipynb` sequentially.

---

## 👨‍💻 Author & Acknowledgments

**Saurabh Kumar**  
Built as part of the **Agentic AI & GenAI Lab** series exploring RAG, Vector Databases, and Agentic Systems.
