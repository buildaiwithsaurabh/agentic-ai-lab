# 🧠 Day XX – LLM Fundamentals

> Learn the core concepts behind Large Language Models (LLMs) before using frameworks like LangChain, Vercel AI SDK, or OpenAI SDK.

---

# 📚 Overview

Large Language Models (LLMs) are AI models trained on massive amounts of text data to understand and generate human-like language. Understanding how LLMs work is essential before building AI applications.

This project covers the fundamental concepts every AI Engineer should know.

---

# 🎯 Learning Objectives

By the end of this module, you will understand:

- What is a Large Language Model (LLM)?
- Tokens
- Context Window
- Temperature
- Top P (Nucleus Sampling)
- Prompt Engineering
- System Prompt
- User Prompt
- Structured Outputs
- Tool Calling (Function Calling)
- Streaming Responses

---

# 📖 Topics Covered

## 1. What is an LLM?

A Large Language Model (LLM) is a deep learning model trained on billions of words from books, articles, websites, and code repositories.

LLMs predict the **next token** based on previous tokens.

Examples:

- GPT-4.1
- GPT-4o
- Gemini 2.5 Pro
- Gemini 2.5 Flash
- Claude 4
- Llama 3
- Qwen 3
- DeepSeek

### How an LLM Works

```
Input Prompt
      │
      ▼
Tokenization
      │
      ▼
Transformer Model
      │
      ▼
Predict Next Token
      │
      ▼
Generated Response
```

---

# 2. Tokens

LLMs do not understand words directly.

They process text as **tokens**.

Example:

```
Hello World
```

may become

```
["Hello", "World"]
```

or

```
["Hel", "lo", "World"]
```

depending on the tokenizer.

### Why Tokens Matter

- Cost is based on tokens
- Context window uses tokens
- Response length is measured in tokens
- Prompt optimization depends on token usage

---

# 3. Context Window

The Context Window is the maximum number of tokens an LLM can remember during a conversation.

```
Prompt

+

Conversation History

+

Retrieved Documents

+

Model Response

≤ Context Window
```

Example:

```
Context Window = 128K Tokens
```

If the total exceeds the limit, older tokens are removed or truncated.

---

# 4. Temperature

Temperature controls the randomness of responses.

| Temperature | Behavior |
|-------------|----------|
| 0.0 | Very deterministic |
| 0.2 | Stable |
| 0.5 | Balanced |
| 0.8 | Creative |
| 1.0 | Highly creative |

### Use Cases

Low Temperature

- Coding
- SQL
- Math
- APIs

High Temperature

- Stories
- Brainstorming
- Marketing
- Creative writing

---

# 5. Top P (Nucleus Sampling)

Top P limits the pool of possible next tokens.

Example:

```
Top P = 0.9
```

The model chooses from the smallest group of tokens whose cumulative probability reaches 90%.

### Difference

Temperature controls randomness.

Top P controls the size of the candidate token pool.

---

# 6. Prompt Engineering

Prompt Engineering is the practice of designing effective prompts to get reliable outputs from LLMs.

Good prompts include:

- Role
- Task
- Context
- Constraints
- Output format
- Examples

Example

```
You are a Senior Backend Engineer.

Explain JWT authentication.

Use simple language.

Return markdown.
```

---

# 7. System Prompt

The System Prompt defines the AI's behavior and rules.

Example:

```
You are an expert Java backend engineer.

Always explain concepts using examples.

Never generate unsafe code.
```

The system prompt has higher priority than user instructions.

---

# 8. User Prompt

The User Prompt is the actual request made by the user.

Example:

```
Explain REST API authentication.
```

The LLM combines:

```
System Prompt

+

User Prompt

↓

Response
```

---

# 9. Structured Outputs

Instead of returning plain text, LLMs can return structured data.

Example JSON

```json
{
  "title": "JWT",
  "difficulty": "Intermediate",
  "topics": [
    "Authentication",
    "Authorization"
  ]
}
```

Benefits:

- Easy parsing
- Reliable APIs
- Automation
- Database storage

---

# 10. Tool Calling (Function Calling)

Modern LLMs can call external tools when needed.

Example Workflow

```
User

↓

LLM

↓

Tool Selection

↓

Execute Tool

↓

Return Result

↓

LLM Response
```

Examples:

- Weather API
- Database Query
- Calculator
- Email Service
- Search Engine
- File System

Tool Calling enables AI agents to interact with external systems instead of relying only on model knowledge.

---

# 11. Streaming Responses

Instead of waiting for the full response, the model sends tokens as they are generated.

Without Streaming

```
User

↓

Wait...

↓

Complete Response
```

With Streaming

```
User

↓

H

↓

He

↓

Hel

↓

Hello

↓

Complete Response
```

Benefits:

- Faster perceived response time
- Better user experience
- Real-time chat interfaces
- AI assistants

---

# 🏗 LLM Request Lifecycle

```
User Prompt
      │
      ▼
System Prompt
      │
      ▼
Tokenization
      │
      ▼
Context Window
      │
      ▼
LLM
      │
      ▼
Tool Calling (Optional)
      │
      ▼
Structured Output
      │
      ▼
Streaming Response
      │
      ▼
User
```

---

# 📂 Suggested Project Structure

```
llm-fundamentals/
│
├── README.md
├── notes/
│   ├── what-is-llm.md
│   ├── tokens.md
│   ├── context-window.md
│   ├── temperature.md
│   ├── top-p.md
│   ├── prompt-engineering.md
│   ├── system-prompt.md
│   ├── user-prompt.md
│   ├── structured-output.md
│   ├── tool-calling.md
│   └── streaming.md
│
└── examples/
    ├── prompts.md
    ├── json-output.md
    ├── tool-calling.md
    └── streaming.md
```

---

# 🛠 Tech Stack

- TypeScript
- Node.js
- OpenAI SDK
- Gemini API
- Groq API
- Vercel AI SDK

---

# 📈 Learning Roadmap

```
LLM Fundamentals
        │
        ▼
Prompt Engineering
        │
        ▼
Embeddings
        │
        ▼
Vector Databases
        │
        ▼
RAG
        │
        ▼
Tool Calling
        │
        ▼
AI SDK
        │
        ▼
LangChain
        │
        ▼
LangGraph
        │
        ▼
AI Agents
        │
        ▼
Production AI Systems
```

---

# 🎯 Key Takeaways

- Understand how LLMs generate text using tokens.
- Learn the importance of context windows and token limits.
- Control model behavior using Temperature and Top P.
- Write better prompts with Prompt Engineering.
- Use System and User Prompts effectively.
- Generate structured JSON outputs for reliable applications.
- Enable AI to interact with external systems through Tool Calling.
- Improve user experience with Streaming responses.

---

# 🚀 Next Step

After mastering LLM Fundamentals, continue with:

- Prompt Engineering (Advanced)
- Embeddings
- Vector Databases
- Retrieval-Augmented Generation (RAG)
- AI SDK (Vercel AI SDK)
- LangChain
- LangGraph
- Agentic AI
- Vertical AI SaaS Applications

---

## ⭐ If you found this helpful, consider starring the repository and following the learning journey!