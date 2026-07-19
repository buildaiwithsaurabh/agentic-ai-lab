# 🚀 Vercel AI SDK + Streaming + Structured Outputs

> Learn how to build modern AI applications using the **Vercel AI SDK** with **Streaming Responses** and **Structured Outputs**. This project demonstrates how to create fast, type-safe, and production-ready AI features using multiple LLM providers.

---

# 📚 Overview

The **Vercel AI SDK** is an open-source TypeScript SDK for building AI-powered applications. It provides a unified API for multiple AI providers, making it easy to add chat, streaming, structured outputs, tool calling, and AI agents to your applications.

Instead of integrating each provider separately, you can switch between providers with minimal code changes while maintaining a consistent developer experience.

---

# 🎯 Learning Objectives

By the end of this project, you will understand:

- What is the Vercel AI SDK?
- AI SDK Architecture
- Multi-Provider Support
- Streaming Responses
- Structured Outputs
- Zod Schema Validation
- Type-Safe AI Responses
- Route Handlers
- AI Chat Applications
- Production Best Practices

---

# 🏗 AI SDK Architecture

```
Frontend (React / Next.js)

        │

        ▼

API Route

        │

        ▼

Vercel AI SDK

        │

        ▼

AI Provider

(OpenAI / Groq / Gemini)

        │

        ▼

Streaming Response

        │

        ▼

Frontend UI
```

---

# ✨ Features

- Unified API
- Streaming Responses
- Structured Outputs
- Multi-Provider Support
- Tool Calling
- TypeScript First
- Edge Runtime Support
- React Hooks
- Type Safety
- Production Ready

---

# 📦 Installation

Install the AI SDK

```bash
npm install ai
```

Install React Hooks

```bash
npm install @ai-sdk/react
```

Install Providers

OpenAI

```bash
npm install @ai-sdk/openai
```

Groq

```bash
npm install @ai-sdk/groq
```

Google Gemini

```bash
npm install @ai-sdk/google
```

Install Zod

```bash
npm install zod
```

---

# 🔑 Environment Variables

```env
OPENAI_API_KEY=

GROQ_API_KEY=

GOOGLE_GENERATIVE_AI_API_KEY=
```

---

# 📖 Topics Covered

## 1. What is the Vercel AI SDK?

The Vercel AI SDK is a TypeScript library that simplifies building AI-powered applications.

It provides a unified interface for:

- Text Generation
- Chat
- Streaming
- Structured Outputs
- Tool Calling
- Multi-Provider AI

---

## 2. Multi-Provider Support

The same API works with different providers.

Supported Providers

- OpenAI
- Groq
- Google Gemini
- Anthropic
- xAI
- Mistral
- Together AI
- DeepSeek (compatible providers)

Example

```
Application

↓

AI SDK

↓

Provider

↓

Response
```

---

## 3. Text Generation

Generate plain text responses.

```ts
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

const { text } = await generateText({
  model: openai("gpt-4.1"),
  prompt: "Explain JWT authentication."
});

console.log(text);
```

---

# 🌊 Streaming Responses

## What is Streaming?

Instead of waiting for the complete response, tokens are sent to the client as they are generated.

---

## Without Streaming

```
User

↓

Wait...

↓

Complete Response
```

---

## With Streaming

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

---

## Benefits

- Better UX
- Faster perceived speed
- Real-time updates
- Lower latency experience
- Professional chat interfaces

---

## Streaming Flow

```
User Prompt

↓

LLM

↓

Generate Tokens

↓

Send Tokens

↓

Frontend Updates
```

---

## Streaming Example

```ts
import { streamText } from "ai";
import { openai } from "@ai-sdk/openai";

const result = streamText({
  model: openai("gpt-4.1"),
  prompt: "Explain React."
});

return result.toUIMessageStreamResponse();
```

---

# 🎯 Structured Outputs

## What are Structured Outputs?

Instead of generating plain text, the AI returns data that matches a predefined schema.

Example

Instead of

```
This recipe contains...
```

Return

```json
{
  "title": "Pasta",
  "ingredients": [
    "Pasta",
    "Tomato"
  ]
}
```

---

## Why Structured Outputs?

- Reliable APIs
- Type Safety
- Database Friendly
- Easy Parsing
- Automation
- Predictable Responses

---

# Zod Schema

```ts
import { z } from "zod";

const recipeSchema = z.object({
  title: z.string(),
  ingredients: z.array(z.string()),
  cookTime: z.string(),
  difficulty: z.enum([
    "Easy",
    "Medium",
    "Hard"
  ])
});
```

---

# Generate Structured Object

```ts
import { generateObject } from "ai";

const { object } = await generateObject({
  model: openai("gpt-4.1"),
  schema: recipeSchema,
  prompt: "Generate a pasta recipe."
});
```

---

# Example Output

```json
{
  "title": "Pasta",
  "ingredients": [
    "Pasta",
    "Tomato",
    "Garlic"
  ],
  "cookTime": "20 min",
  "difficulty": "Easy"
}
```

---

# 📱 AI Chat UI

Typical chat flow

```
User

↓

Input Box

↓

API Route

↓

AI SDK

↓

Streaming

↓

Messages

↓

Chat UI
```

---

# Project Structure

```
vercel-ai-sdk/

│

├── app/
│   ├── api/
│   │   └── chat/
│   │       └── route.ts
│   ├── layout.tsx
│   └── page.tsx
│
├── components/
│   ├── Chat.tsx
│   ├── ChatInput.tsx
│   ├── Message.tsx
│   ├── CodeBlock.tsx
│   └── TypingIndicator.tsx
│
├── lib/
│   ├── ai.ts
│   └── providers.ts
│
├── types/
│
├── .env.local
├── package.json
└── README.md
```

---

# AI SDK Request Lifecycle

```
User

↓

React UI

↓

API Route

↓

AI SDK

↓

Provider

↓

Streaming

↓

Frontend

↓

User
```

---

# Common Use Cases

- AI Chatbots
- Code Assistants
- Resume Review
- AI Forms
- AI Content Generation
- SQL Generator
- JSON Generator
- AI Search
- Customer Support
- Documentation Assistant

---

# Advantages

- Unified API
- Excellent TypeScript Support
- Easy Provider Switching
- Production Ready
- Streaming Support
- Structured Outputs
- Tool Calling
- Great Developer Experience
- React Integration

---

# Best Practices

- Stream responses for chat applications.
- Use Structured Outputs for APIs.
- Validate responses with Zod.
- Store API keys in environment variables.
- Handle provider errors gracefully.
- Keep prompts focused and specific.
- Choose the appropriate model for each task.

---

# Learning Roadmap

```
LLM Fundamentals

↓

Prompt Engineering

↓

Vercel AI SDK

↓

Streaming

↓

Structured Outputs

↓

Tool Calling

↓

Chat Applications

↓

Multi-Model AI

↓

RAG

↓

AI Agents

↓

LangChain

↓

LangGraph

↓

Production AI Applications
```

---

# Tech Stack

- TypeScript
- Next.js
- React
- Vercel AI SDK
- OpenAI
- Groq
- Google Gemini
- Zod

---

# Resources

- Vercel AI SDK Documentation: https://sdk.vercel.ai/
- OpenAI Platform: https://platform.openai.com/
- Google AI Studio: https://aistudio.google.com/
- Groq Cloud: https://console.groq.com/

---

# 🎯 Key Takeaways

- Build AI applications using a unified SDK.
- Stream responses for a better user experience.
- Generate structured JSON with schema validation.
- Switch AI providers with minimal code changes.
- Build scalable, production-ready AI applications using TypeScript and Next.js.

---

# 🚀 Next Step

After mastering the Vercel AI SDK, continue with:

- Multi-Model AI
- Tool Calling
- AI Agents
- Retrieval-Augmented Generation (RAG)
- LangChain
- LangGraph
- Model Context Protocol (MCP)
- Production AI SaaS Applications

---

## ⭐ If you found this project helpful, consider starring the repository and following the journey as I learn AI Engineering in public!