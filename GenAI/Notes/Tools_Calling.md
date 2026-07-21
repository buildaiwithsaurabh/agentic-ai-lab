# 🛠️ Tool Calling with Vercel AI SDK

> Learn how AI models invoke external tools to fetch real-time data, perform calculations, query databases, and execute actions using the **Vercel AI SDK**.

---

# 📚 Overview

Large Language Models (LLMs) are powerful, but they only know what they've been trained on. They cannot access real-time information or interact with external systems on their own.

**Tool Calling** (also known as **Function Calling**) allows an LLM to request the execution of external functions. The application executes the requested tool, returns the result to the model, and the model generates the final response.

This capability enables AI applications to perform real-world tasks such as checking the weather, querying databases, sending emails, calculating values, and interacting with APIs.

---

# 🎯 Learning Objectives

By the end of this project, you will understand:

- What is Tool Calling?
- Function Calling
- Tool Definitions
- Tool Schema
- Zod Validation
- Tool Execution
- Multi-Step Conversations
- Streaming Tool Results
- Vercel AI SDK Tool API
- Production Best Practices

---

# 🏗️ Tool Calling Architecture

```
User

↓

Prompt

↓

LLM

↓

Tool Selection

↓

Application

↓

Execute Tool

↓

Tool Result

↓

LLM

↓

Final Response
```

---

# Why Tool Calling?

Without Tool Calling

```
User

↓

LLM

↓

"I don't know the current weather."
```

With Tool Calling

```
User

↓

LLM

↓

Weather Tool

↓

Weather API

↓

Current Temperature

↓

LLM

↓

Final Answer
```

---

# 📖 Topics Covered

## 1. What is Tool Calling?

Tool Calling allows an AI model to invoke predefined functions instead of relying only on its internal knowledge.

Examples

- Weather API
- Calculator
- Database Query
- Email Service
- Search Engine
- File System
- Payment Gateway
- CRM Integration

---

# 2. Function Calling

The model decides when a tool should be executed.

Example

User

```
What's the weather in Delhi?
```

Model

```
Call getWeather(city="Delhi")
```

Application

```
Execute Weather API
```

Model

```
Today's temperature is 34°C.
```

---

# 3. Tool Definition

Each tool describes:

- Name
- Description
- Parameters
- Validation Rules

Example

```ts
const weatherTool = {
  description: "Get current weather",
  parameters: {
    city: "string"
  }
}
```

---

# 4. Zod Validation

Vercel AI SDK uses **Zod** to validate tool inputs.

Example

```ts
import { z } from "zod";

const weatherSchema = z.object({
  city: z.string(),
});
```

Benefits

- Type Safety
- Input Validation
- Better Error Handling
- Reliable APIs

---

# 5. Tool Execution

Workflow

```
LLM

↓

Tool Call

↓

Execute Function

↓

Return Data

↓

LLM

↓

Final Answer
```

---

# Example Tool

```ts
const weatherTool = tool({
  description: "Get weather by city",
  inputSchema: z.object({
    city: z.string(),
  }),

  execute: async ({ city }) => {
    return {
      city,
      temperature: "32°C",
      condition: "Sunny",
    };
  },
});
```

---

# 6. Multi-Step Conversations

AI can call multiple tools in a single conversation.

Example

```
User

↓

Find my order

↓

Database Tool

↓

Order Found

↓

Shipping Tool

↓

Delivery Status

↓

LLM Response
```

---

# 7. Streaming Tool Results

The Vercel AI SDK supports streaming while tools execute.

```
User

↓

LLM

↓

Tool Execution

↓

Streaming Updates

↓

Final Response
```

Benefits

- Better UX
- Lower perceived latency
- Real-time feedback

---

# 8. AI SDK Tool API

Example

```ts
import { streamText } from "ai";

const result = streamText({
  model,
  tools: {
    weather: weatherTool,
  },
  prompt: "What's the weather in Mumbai?",
});

return result.toUIMessageStreamResponse();
```

---

# Tool Lifecycle

```
User Prompt

↓

LLM

↓

Reasoning

↓

Tool Selection

↓

Parameter Generation

↓

Validation

↓

Execution

↓

Result

↓

LLM

↓

Final Response
```

---

# Example Use Cases

## Calculator

```
User

↓

"What is 125 × 34?"

↓

Calculator Tool

↓

4250

↓

LLM
```

---

## Weather

```
User

↓

Weather Tool

↓

Weather API

↓

Current Forecast
```

---

## Database

```
User

↓

Database Tool

↓

SQL Query

↓

Results

↓

LLM
```

---

## Email

```
User

↓

Email Tool

↓

SMTP/API

↓

Email Sent
```

---

## Search

```
User

↓

Search Tool

↓

Web Search

↓

Relevant Results

↓

LLM
```

---

# Project Structure

```
tool-calling/

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
│   ├── ToolResult.tsx
│   └── LoadingIndicator.tsx
│
├── lib/
│   ├── tools/
│   │   ├── weather.ts
│   │   ├── calculator.ts
│   │   ├── database.ts
│   │   └── search.ts
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

# Common Tools

- Weather
- Calculator
- SQL Database
- Search Engine
- File System
- Email
- Calendar
- Payment Gateway
- CRM
- GitHub
- Slack
- Notion

---

# Production Use Cases

- AI Customer Support
- AI Assistants
- Booking Systems
- Travel Planner
- Banking Assistant
- Medical Assistant
- CRM Automation
- DevOps Copilot
- AI Coding Assistant
- HR Assistant

---

# Best Practices

- Validate inputs with Zod.
- Keep tools focused on a single responsibility.
- Handle execution errors gracefully.
- Return structured data.
- Avoid exposing sensitive credentials.
- Log tool executions for debugging.
- Stream responses for better user experience.

---

# Advantages

- Real-time information
- External system integration
- Reliable automation
- Type-safe execution
- Better user experience
- Extensible architecture
- Production-ready workflows

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

Multi-Step AI Workflows

↓

RAG

↓

AI Agents

↓

LangChain

↓

LangGraph

↓

Model Context Protocol (MCP)

↓

Production AI Applications
```

---

# Tech Stack

- TypeScript
- Next.js
- React
- Vercel AI SDK
- Zod
- OpenAI
- Groq
- Google Gemini

---

# Resources

- Vercel AI SDK: https://sdk.vercel.ai/
- OpenAI Function Calling: https://platform.openai.com/docs/guides/function-calling
- Zod: https://zod.dev/

---

# 🎯 Key Takeaways

- Tool Calling enables AI models to interact with external systems.
- The LLM decides **when** a tool should be used.
- Applications execute the tool and return results to the model.
- Zod provides type-safe validation for tool parameters.
- Streaming improves the user experience while tools execute.
- Tool Calling is the foundation for building AI agents and intelligent workflows.

---

# 🚀 Next Step

After mastering Tool Calling, continue with:

- Multi-Tool Agents
- Model Context Protocol (MCP)
- Retrieval-Augmented Generation (RAG)
- LangChain
- LangGraph
- AI Agents
- Multi-Agent Systems
- Production AI SaaS Applications

---

## ⭐ If you found this project helpful, consider starring the repository and following the journey as I learn AI Engineering in public!