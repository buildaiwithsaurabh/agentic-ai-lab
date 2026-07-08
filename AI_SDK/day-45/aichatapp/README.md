# Day 45 — Building an AI Chat Assistant with Next.js, AI SDK & Groq

## 🚀 Project

**AI Chat Assistant**

A modern AI chatbot built using **Next.js 16**, **Vercel AI SDK 5**, and **Groq**. This project demonstrates how to build a production-style AI application with streaming responses using the App Router.

---

# 🎯 Learning Objectives

Today's goal was to understand how modern AI applications are built using the Vercel AI SDK.

Topics Covered

- What is the AI SDK?
- Why use the AI SDK?
- Groq AI Provider
- Large Language Models (LLMs)
- Route Handlers
- Streaming Responses
- AI Messages
- Chat Interface
- React Components
- App Router
- Environment Variables

---

# 📁 Project Structure

```text
frontend-nextjs/
└── day-45/
    ├── app/
    │
    ├── api/
    │   └── chat/
    │       └── route.ts
    │
    ├── components/
    │   ├── Navbar.tsx
    │   ├── Chat.tsx
    │   ├── ChatInput.tsx
    │   ├── Message.tsx
    │   └── EmptyState.tsx
    │
    ├── lib/
    │   └── ai.ts
    │
    ├── globals.css
    ├── layout.tsx
    └── page.tsx
    │
    ├── .env.local
    ├── package.json
    └── README.md
```

---

# 🤖 What is the Vercel AI SDK?

The **Vercel AI SDK** is an open-source library that simplifies building AI-powered applications.

Instead of manually handling API requests, streaming, parsing responses, and provider-specific implementations, the SDK provides a unified interface for interacting with multiple AI models.

It supports providers such as:

- OpenAI
- Groq
- Google Gemini
- Anthropic
- Mistral
- xAI
- Azure OpenAI
- Together AI
- OpenRouter
- and many more.

---

# ❓ Why Use the AI SDK?

Without the AI SDK:

```
Frontend

↓

fetch()

↓

REST API

↓

Authentication

↓

Provider SDK

↓

LLM

↓

Response Parsing

↓

Frontend
```

With the AI SDK:

```
Frontend

↓

AI SDK

↓

Provider

↓

LLM

↓

Streaming Response
```

Benefits

- Less boilerplate
- Built-in streaming
- Multiple AI providers
- TypeScript support
- Production-ready
- Works perfectly with Next.js

---

# 🧠 What is Groq?

Groq is an AI inference platform optimized for extremely fast LLM inference.

Instead of training models, Groq focuses on delivering very low-latency responses.

Popular models available on Groq include:

- Llama 3.3
- Llama 4
- DeepSeek
- Qwen
- Kimi
- Gemma

---

# 🤖 Model Used

```
llama-3.3-70b-versatile
```

Why this model?

- Fast
- High quality
- Large context window
- Excellent reasoning
- Great for chat applications

---

# 🔑 Environment Variables

Create

```
.env.local
```

Add

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit this file.

---

# 📦 Installation

```bash
npm install ai

npm install @ai-sdk/react

npm install @ai-sdk/groq

npm install react-markdown

npm install remark-gfm

npm install react-syntax-highlighter

npm install lucide-react

npm install clsx
```

---

# 📂 Project Architecture

```
User

↓

Chat UI

↓

Route Handler

↓

AI SDK

↓

Groq

↓

LLM

↓

Streaming Response

↓

Browser
```

---

# 🧩 Components

## Navbar

Displays application branding.

---

## Chat

Manages

- Messages
- Chat State
- AI Responses

---

## ChatInput

Collects user prompts.

---

## Message

Displays

- User messages
- AI responses
- Markdown

---

## EmptyState

Shown when no conversation exists.

---

# 📂 lib/ai.ts

This file initializes the AI model.

Example

```ts
import { groq } from "@ai-sdk/groq";

export const model = groq(
    "llama-3.3-70b-versatile"
);
```

Keeping the model configuration separate makes it easy to switch providers later.

---

# 📂 Route Handler

```
app/api/chat/route.ts
```

Responsibilities

- Receive messages
- Call AI model
- Stream response
- Return result

---

# 🔄 Request Flow

```
User

↓

Chat Input

↓

POST

/api/chat

↓

route.ts

↓

streamText()

↓

Groq

↓

Streaming

↓

Browser
```

---

# 🌊 What is Streaming?

Traditional AI

```
User

↓

Wait...

↓

Entire response

↓

Browser
```

Streaming

```
User

↓

AI starts typing immediately

↓

More words...

↓

More words...

↓

Finished
```

Streaming improves:

- User experience
- Responsiveness
- Perceived speed

---

# 💬 Chat Messages

Every conversation consists of messages.

Example

```text
User

↓

What is React?

↓

Assistant

↓

React is a JavaScript library...
```

The AI SDK manages message history efficiently for conversational interactions.

---

# 📜 Markdown Rendering

AI responses often contain:

- Headings
- Bullet lists
- Tables
- Links
- Code blocks

Using

```
react-markdown
```

allows the chatbot to display formatted responses instead of plain text.

---

# 🎨 Styling

The interface includes:

- Responsive layout
- Chat bubbles
- Navbar
- Empty state
- Input area
- Modern card design

---

# 🔒 Security

Never expose:

```
GROQ_API_KEY
```

Always access the model through a Route Handler.

Incorrect

```
Browser

↓

Groq API
```

Correct

```
Browser

↓

Route Handler

↓

Groq API
```

---

# 🎯 Learning Outcome

Today I learned:

- AI SDK
- Groq
- AI Providers
- Route Handlers
- Streaming
- Chat Architecture
- Environment Variables
- AI Components
- Modern AI Development

---

# 🚀 Real-World Applications

The same architecture can be used to build:

- AI Chatbots
- Coding Assistants
- Resume Reviewers
- Interview Assistants
- AI Tutors
- Customer Support Bots
- AI Search
- AI Agents
- RAG Applications
- SaaS AI Products

---

# 📈 Current Learning Roadmap

```
FastAPI ✅

↓

React ✅

↓

TypeScript ✅

↓

Next.js ✅

↓

Route Handlers ✅

↓

Server Actions ✅

↓

AI SDK ✅

↓

Streaming

↓

Markdown

↓

Supabase

↓

Authentication

↓

RAG

↓

AI Agents

↓

Agentic AI

↓

Production AI SaaS
```

---

# 🛠️ Tech Stack

- Next.js 16
- React 19
- TypeScript
- AI SDK 5
- Groq
- App Router
- Route Handlers
- React Markdown
- Lucide Icons

---

# 📚 Key Concepts Summary

| Concept | Description |
|----------|-------------|
| AI SDK | Unified library for AI providers |
| Groq | Fast AI inference platform |
| Route Handler | Backend endpoint for AI requests |
| Streaming | Live token-by-token AI responses |
| Chat Messages | Conversation history between user and AI |
| Markdown | Rich text rendering for AI output |
| Environment Variables | Secure storage for API keys |

---

# 🔮 Next Day

## Day 46

### Streaming Chat with AI SDK

Topics

- AI SDK React Hooks
- Real-Time Streaming
- Loading State
- Typing Indicator
- Code Blocks
- Markdown Rendering

Project

**Production-Style Streaming AI Chat Assistant**

---

# 📦 Repository Commit

```bash
git add .

git commit -m "feat(day-45): build AI chat assistant using Next.js, AI SDK and Groq"

git push origin main
```

---

# 📌 Repository

GitHub

```
https://github.com/buildaiwithsaurabh/agentic-ai-lab.git
```