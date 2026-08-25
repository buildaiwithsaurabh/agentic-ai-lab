# 🌐 Web Research Agent

A professional **AI-powered web research assistant** built with **Streamlit, LangChain, LangGraph, and Groq**. The application can maintain conversational context and use web search to retrieve current information before generating responses.

The project demonstrates how to build a practical **agentic AI application** where an LLM can dynamically decide when to use external tools instead of relying solely on its internal knowledge.

---

## ✨ Features

* 🤖 **AI Research Agent** powered by Groq LLM
* 🔍 **Web Search Integration** for current and up-to-date information
* 🧠 **Conversational Memory** using LangGraph's `MemorySaver`
* 💬 **Interactive Chat Interface** built with Streamlit
* ⚡ **Streaming Responses** for a real-time user experience
* 🛠️ **Custom LangChain Tool** for web search
* 🔄 **Persistent Conversation Thread** during the user session
* 🧹 **Clean Tool Handling** that hides raw tool outputs from users

---

## 🏗️ Architecture

The application follows an **Agent + Tool + Memory** architecture:

```text
User
  │
  ▼
Streamlit Chat Interface
  │
  ▼
LangChain Agent
  │
  ├──────────────► Groq LLM
  │
  ├──────────────► Web Search Tool
  │
  ▼
LangGraph Memory Checkpointer
  │
  ▼
Streaming Response to User
```

### How It Works

1. The user submits a question through the Streamlit chat interface.
2. The query is sent to the LangChain agent.
3. The LLM analyzes the request and determines whether web search is required.
4. For current or time-sensitive information, the agent calls the `web_search` tool.
5. Search results are provided back to the LLM.
6. The LLM generates a natural-language response.
7. The response is streamed to the Streamlit interface.
8. LangGraph memory maintains the conversation state using a unique thread ID.

---

## 🛠️ Tech Stack

| Technology          | Purpose                                  |
| ------------------- | ---------------------------------------- |
| **Python**          | Core programming language                |
| **Streamlit**       | Web interface                            |
| **LangChain**       | Agent and tool orchestration             |
| **LangGraph**       | Conversation memory and state management |
| **Groq**            | High-speed LLM inference                 |
| **Serpdive Search** | Web search capability                    |
| **Python-dotenv**   | Environment variable management          |

---

## 📁 Project Structure

```text
web-research-agent/
│
├── app.py                 # Main Streamlit application
├── .env                   # Environment variables
├── .gitignore             # Files excluded from Git
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd web-research-agent
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory of the project.

```env
GROQ_API_KEY=your_groq_api_key
```

Add any additional API keys required by your configured search provider.

> **Security Note:** Never commit your `.env` file or API keys to a public GitHub repository.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser, typically at:

```text
http://localhost:8501
```

---

## 🧠 Agent Behavior

The agent is configured with a system prompt that defines its role as a **web research agent**.

For questions involving:

* Current events
* Recent news
* Live information
* Information that may have changed over time

the agent is instructed to use the web search tool before generating an answer.

This approach helps reduce the risk of providing outdated information and demonstrates an important principle in **agentic AI systems: tool augmentation for knowledge beyond the model's static training data**.

---

## 🔍 Custom Web Search Tool

The project wraps the search functionality inside a LangChain tool:

```python
@tool
def web_search(query: str) -> str:
    """Search the web for current and up-to-date information."""
    return search.run(query)
```

This allows the AI agent to invoke web search dynamically based on the user's query.

---

## 🧠 Conversation Memory

Conversation state is managed using LangGraph's `MemorySaver`.

```python
if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver()
```

Each conversation uses a configurable thread ID:

```python
config = {
    "configurable": {
        "thread_id": "user_1"
    }
}
```

This architecture makes it possible to extend the application later with:

* Multiple users
* Persistent database-backed memory
* Authentication
* User-specific conversation threads
* Long-term memory systems

---

## 📡 Streaming Responses

The application uses streaming to display responses progressively rather than waiting for the complete response.

Only AI-generated content is displayed to the user, while internal tool outputs remain hidden.

This provides a cleaner and more responsive chat experience.

---

## 🚀 Future Improvements

Potential improvements for the project include:

* [ ] Add source links and citations
* [ ] Support multiple search providers
* [ ] Add authentication and user management
* [ ] Store conversations in a database
* [ ] Add chat history management
* [ ] Implement follow-up research capabilities
* [ ] Add document upload and RAG support
* [ ] Add research report generation
* [ ] Add agent observability and tracing
* [ ] Deploy the application to Streamlit Cloud or another cloud platform

---

## 🎯 Learning Outcomes

This project demonstrates practical understanding of:

* Building AI agents with LangChain
* Tool calling and agent workflows
* Integrating LLMs with external data sources
* Managing conversational state with LangGraph
* Streaming LLM responses
* Building AI applications with Streamlit
* Managing API keys securely using environment variables

---

## ⚠️ Important Note

Web search results may contain incomplete or inaccurate information. The agent's responses should therefore be treated as research assistance rather than a replacement for verifying critical information from authoritative sources.

---

## 📄 License

This project is intended for educational and portfolio purposes. You may add an appropriate open-source license, such as the MIT License, if you plan to make the repository publicly available.

---

## 👨‍💻 Author

**Saurabh Kumara**

Built as a hands-on project for learning **Generative AI, AI Agents, LangChain, LangGraph, and LLM application development**.

---

### ⭐ If You Found This Project Useful

Consider giving the repository a star and sharing your feedback!
