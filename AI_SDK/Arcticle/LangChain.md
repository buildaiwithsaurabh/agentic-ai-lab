# LangChain

## 🚀 Introduction

**LangChain** is an open-source framework for building applications powered by **Large Language Models (LLMs)**. It provides reusable components and abstractions for creating AI applications such as chatbots, RAG systems, AI agents, document question-answering systems, workflow automation, and multi-agent architectures.

Instead of calling an LLM API directly, LangChain helps developers orchestrate prompts, models, memory, tools, retrievers, vector databases, and agents into complete AI applications.

---

# Why LangChain?

Without LangChain:

```
Application

↓

Prompt

↓

LLM API

↓

Response
```

With LangChain:

```
Application

↓

Prompt Template

↓

LLM

↓

Tools

↓

Memory

↓

Retriever

↓

Output Parser

↓

Response
```

LangChain provides a structured way to build scalable AI applications.

---

# Key Features

- LLM Integration
- Prompt Templates
- Output Parsers
- Memory
- Chains
- Retrieval-Augmented Generation (RAG)
- Agents
- Tools
- Document Loaders
- Text Splitters
- Vector Store Integration
- Streaming
- Callbacks

---

# LangChain Architecture

```
User

↓

Application

↓

LangChain

↓

Prompt

↓

LLM

↓

Tools

↓

Memory

↓

Retriever

↓

Response
```

---

# Core Components

## 1. Models

Models are the brains of your application.

Supported Providers

- OpenAI
- Gemini
- Anthropic
- Groq
- Ollama
- Azure OpenAI
- Mistral
- Cohere
- Hugging Face

Example

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4.1"
)
```

---

## 2. Prompt Templates

Prompt templates help generate dynamic prompts.

Example

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Explain {topic}"
)
```

Output

```
Explain React Context API
```

---

## 3. Output Parsers

Output parsers convert AI responses into structured data.

Example

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
```

---

## 4. Chains

Chains combine multiple steps into a workflow.

Example

```
Prompt

↓

LLM

↓

Output Parser
```

Python

```python
chain = prompt | model | parser
```

---

## 5. Memory

Memory enables conversations across multiple messages.

Without Memory

```
User

↓

LLM

↓

Forget previous message
```

With Memory

```
User

↓

Conversation History

↓

LLM

↓

Response
```

---

## 6. Document Loaders

Load documents from various sources.

Supported Formats

- PDF
- DOCX
- TXT
- HTML
- Markdown
- CSV
- Websites
- YouTube
- Notion
- Google Drive

Example

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("book.pdf")

docs = loader.load()
```

---

## 7. Text Splitters

Large documents must be split before embedding.

Example

```
PDF

↓

Chunk 1

↓

Chunk 2

↓

Chunk 3
```

Python

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
```

---

## 8. Embeddings

Embeddings convert text into vectors.

```
Text

↓

Embedding Model

↓

Vector
```

Common Models

- OpenAI
- Gemini
- HuggingFace
- BGE
- Nomic
- Ollama

---

## 9. Vector Stores

Store embeddings for semantic search.

Popular Vector Databases

- Chroma
- Pinecone
- FAISS
- Weaviate
- Milvus
- Qdrant
- PGVector
- Supabase Vector

---

## 10. Retrievers

Retrieve relevant information from vector databases.

```
Question

↓

Retriever

↓

Relevant Documents

↓

LLM
```

---

## 11. Retrieval-Augmented Generation (RAG)

RAG combines retrieval with LLM reasoning.

Architecture

```
User

↓

Question

↓

Retriever

↓

Vector Database

↓

Relevant Context

↓

LLM

↓

Answer
```

Benefits

- Up-to-date information
- Lower hallucinations
- Domain-specific knowledge

---

## 12. Tools

Tools allow LLMs to interact with external systems.

Examples

- Calculator
- Search
- Weather API
- Database
- Email
- File System
- Python REPL
- SQL Database

---

## 13. Agents

Agents decide which tools to use.

```
User

↓

Agent

↓

Reasoning

↓

Tool

↓

Observation

↓

Final Answer
```

Popular Agent Types

- ReAct
- Tool Calling
- Function Calling
- Plan-and-Execute
- Multi-Agent

---

# LangGraph

LangGraph extends LangChain for building stateful AI workflows.

```
Start

↓

Agent

↓

Tool

↓

Memory

↓

Decision

↓

End
```

Use Cases

- AI Assistants
- Multi-Agent Systems
- Autonomous Workflows

---

# LangSmith

LangSmith is LangChain's observability platform.

Features

- Debugging
- Tracing
- Evaluation
- Prompt Management
- Monitoring

---

# LangChain Ecosystem

```
LangChain

├── LangGraph
├── LangSmith
├── LangServe
├── LangChain Community
├── LangChain Hub
└── LangChain CLI
```

---

# Common AI Workflows

## Simple Chatbot

```
User

↓

Prompt

↓

LLM

↓

Response
```

---

## Chat with Memory

```
User

↓

Memory

↓

LLM

↓

Response
```

---

## RAG

```
Question

↓

Retriever

↓

Vector Store

↓

LLM

↓

Answer
```

---

## AI Agent

```
User

↓

Agent

↓

Reasoning

↓

Tool

↓

Response
```

---

# Installation

```bash
pip install langchain
```

OpenAI

```bash
pip install langchain-openai
```

Groq

```bash
pip install langchain-groq
```

Google Gemini

```bash
pip install langchain-google-genai
```

Community Integrations

```bash
pip install langchain-community
```

Vector Database

```bash
pip install chromadb
```

Environment Variables

```env
OPENAI_API_KEY=

GROQ_API_KEY=

GOOGLE_API_KEY=

LANGCHAIN_API_KEY=
```

---

# Project Structure

```
langchain-project/

├── app.py
├── prompts/
├── chains/
├── agents/
├── tools/
├── retrievers/
├── vectorstore/
├── documents/
├── memory/
├── utils/
├── config.py
├── requirements.txt
└── README.md
```

---

# Advantages

- Modular architecture
- Supports multiple LLM providers
- Easy RAG implementation
- Agent framework
- Tool integration
- Production-ready ecosystem
- Excellent documentation
- Large community

---

# Limitations

- Learning curve
- Rapid API changes
- Can be overkill for simple applications
- Additional abstraction layer
- Requires understanding of LLM concepts

---

# Real-World Applications

- AI Chatbots
- Customer Support
- AI Assistants
- RAG Systems
- Document Q&A
- Resume Analyzer
- Code Assistant
- Research Assistant
- AI Search Engine
- Multi-Agent Systems
- Workflow Automation
- Knowledge Management

---

# Learning Roadmap

```
Python

↓

LLMs

↓

Prompt Engineering

↓

LangChain Basics

↓

Prompt Templates

↓

Models

↓

Chains

↓

Output Parsers

↓

Memory

↓

Document Loaders

↓

Text Splitters

↓

Embeddings

↓

Vector Databases

↓

Retrievers

↓

RAG

↓

Agents

↓

LangGraph

↓

LangSmith

↓

Production AI Applications
```

---

# Tech Stack

- Python
- LangChain
- LangGraph
- LangSmith
- OpenAI
- Groq
- Gemini
- ChromaDB
- FAISS
- Pinecone
- PostgreSQL
- FastAPI

---

# Resources

- Official Documentation: https://python.langchain.com/
- LangGraph: https://langchain-ai.github.io/langgraph/
- LangSmith: https://smith.langchain.com/

---

# Conclusion

LangChain is one of the most widely used frameworks for building **LLM-powered applications**. It provides reusable building blocks for creating chatbots, RAG pipelines, AI agents, and production AI systems.

Mastering LangChain gives you a strong foundation for developing scalable AI applications and integrating multiple LLM providers into real-world software.
