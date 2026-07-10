# 🤖 Multi-Model AI Chat — Day 47

A production-grade AI chat application built with **Next.js 15**, **Vercel AI SDK**, and support for **14 models** across **3 providers** — Groq, Google Gemini, and OpenAI — all switchable from a single UI dropdown.

---

## ✨ Features

- 🔀 **Multi-Provider Support** — Switch between Groq, Google Gemini, and OpenAI in one click
- 🧠 **14 AI Models** — From ultra-fast Llama to deep-reasoning Gemini 2.5 Pro and GPT-4o
- ⚡ **Real-time Streaming** — Token-by-token streaming responses using AI SDK's `streamText`
- 🎨 **Provider-Aware UI** — Color-coded tabs, speed badges, context window info, and tags per model
- 💬 **Suggestion Cards** — Empty state with clickable prompt suggestions to get started quickly
- 🔄 **Retry on Error** — Graceful error banner with one-click retry
- 📱 **Responsive Design** — Works on desktop and mobile
- 🌙 **Auto-scroll** — Chat auto-scrolls to latest message with smart user-message detection

---

## 🏗️ Architecture

```
app/
├── api/
│   └── chat/
│       └── route.ts          # POST /api/chat — resolves provider+model, streams response
├── components/
│   ├── Chat.tsx              # Root chat component — holds model state, renders selector + messages
│   ├── ModelSelector.tsx     # Provider tabs + model picker dropdown
│   ├── ChatInput.tsx         # Text input + send button
│   ├── Message.tsx           # Individual message bubble (user / assistant)
│   ├── EmptyState.tsx        # Landing suggestions when no messages
│   ├── TypingIndicator.tsx   # Animated dots while AI is responding
│   └── CodeBlock.tsx         # Syntax-highlighted code blocks in responses
├── lib/
│   ├── providers.ts          # Provider registry (Groq, Google, OpenAI) with model factories
│   ├── models.ts             # Full model catalog with metadata
│   └── ai.ts                 # Legacy single-model export (kept for reference)
├── hooks/
│   └── useAutoScroll.ts      # Auto-scroll hook tied to message/loading state
├── globals.css               # All styles — vanilla CSS, no Tailwind
├── layout.tsx                # Root layout with Navbar
└── page.tsx                  # Home page — renders <Chat />
```

### Data Flow

```
User selects model in ModelSelector
        │
        ▼
Chat.tsx holds selectedModel state
        │
        ▼
useChat({ body: { modelId, providerId } })
        │
        ▼ POST /api/chat
route.ts reads { messages, modelId, providerId }
        │
        ▼
getProviderModel(providerId, modelId)    ← providers.ts
        │
        ├── groq(modelId)    → @ai-sdk/groq
        ├── google(modelId)  → @ai-sdk/google
        └── openai(modelId)  → @ai-sdk/openai
        │
        ▼
streamText({ model, messages })  → streaming SSE response
        │
        ▼
useChat receives token stream → updates UI in real-time
```

---

## 🤖 Supported Models

### ⚡ Groq — Ultra-fast inference via custom LPU hardware

| Model | Context | Speed | Tags |
|-------|---------|-------|------|
| Llama 3.3 70B Versatile | 128k | Fast | Versatile, Popular |
| Llama 3.1 8B Instant | 128k | Fast | Fastest |
| Mixtral 8x7B | 32k | Fast | MoE |
| Gemma 2 9B | 8k | Fast | Google |

### ✦ Google Gemini — Multimodal reasoning with massive context

| Model | Context | Speed | Tags |
|-------|---------|-------|------|
| Gemini 2.5 Flash | 1M | Fast | Thinking, New |
| Gemini 2.5 Pro | 1M | Medium | Most Capable, Thinking |
| Gemini 2.0 Flash | 1M | Fast | Multimodal |
| Gemini 1.5 Pro | 2M | Medium | 2M Context |
| Gemini 1.5 Flash | 1M | Fast | Efficient |

### ◎ OpenAI — Industry-leading GPT and reasoning models

| Model | Context | Speed | Tags |
|-------|---------|-------|------|
| GPT-4o | 128k | Fast | Flagship, Multimodal |
| GPT-4o Mini | 128k | Fast | Affordable |
| GPT-4 Turbo | 128k | Medium | Vision |
| o1 Mini | 128k | Medium | Reasoning |
| o3 Mini | 200k | Medium | Reasoning, New |

---

## 🚀 Getting Started

### 1. Clone & Install

```bash
git clone <your-repo-url>
cd multimodel
npm install
```

### 2. Configure API Keys

Create a `.env.local` file in the root (or edit the existing one):

```env
# Groq — https://console.groq.com/keys
GROQ_API_KEY=your_groq_api_key_here

# Google Gemini — https://aistudio.google.com/apikey
GOOGLE_GENERATIVE_AI_API_KEY=your_google_api_key_here

# OpenAI — https://platform.openai.com/api-keys
OPENAI_API_KEY=your_openai_api_key_here
```

> You only need to add keys for the providers you want to use. Groq is free with generous limits.

### 3. Run the Dev Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| [Next.js 15](https://nextjs.org/) | React framework with App Router + Turbopack |
| [Vercel AI SDK](https://sdk.vercel.ai/) | Streaming AI responses (`streamText`, `useChat`) |
| [@ai-sdk/groq](https://sdk.vercel.ai/providers/ai-sdk-providers/groq) | Groq provider adapter |
| [@ai-sdk/google](https://sdk.vercel.ai/providers/ai-sdk-providers/google-generative-ai) | Google Gemini provider adapter |
| [@ai-sdk/openai](https://sdk.vercel.ai/providers/ai-sdk-providers/openai) | OpenAI provider adapter |
| [React 19](https://react.dev/) | UI framework |
| [Lucide React](https://lucide.dev/) | Icon library |
| Vanilla CSS | All styling — no Tailwind, full control |

---

## 📁 Key Files Explained

### `app/lib/providers.ts`
The **provider registry**. Each provider entry has an `id`, `name`, `icon`, `color`, and a `getModel(modelId)` factory function. The `getProviderModel()` utility resolves the correct SDK model instance at request time.

```ts
export const providers: Record<ProviderId, ProviderConfig> = {
  groq:   { getModel: (id) => groq(id)   },
  google: { getModel: (id) => google(id) },
  openai: { getModel: (id) => openai(id) },
};
```

### `app/lib/models.ts`
The **model catalog**. Each `ModelConfig` entry defines the model's `id` (used in API calls), `name` (display), `provider`, `contextWindow`, `speed`, `description`, and optional `tags`.

Adding a new model is as simple as adding one object to the `models` array.

### `app/api/chat/route.ts`
The **streaming API route**. Reads `modelId` and `providerId` from the request body, validates the model exists in the catalog, resolves the AI SDK model instance, and streams the response back using `streamText`.

### `app/components/ModelSelector.tsx`
The **model picker UI**. Renders a trigger button showing the current model, and a dropdown with three provider tabs. Each tab lists all models for that provider with speed badges, descriptions, context sizes, and tags.

---

## 🔧 Adding a New Model

1. Open `app/lib/models.ts`
2. Add a new entry to the `models` array:

```ts
{
  id: "gpt-4o-2024-11-20",       // exact model ID used by the provider's API
  name: "GPT-4o (Nov 2024)",     // display name shown in the UI
  description: "Latest snapshot of GPT-4o.",
  provider: "openai",             // "groq" | "google" | "openai"
  contextWindow: "128k",
  speed: "Fast",
  tags: ["Latest"],
}
```

That's it — the model will automatically appear in the selector dropdown under the correct provider tab.

---

## 🔧 Adding a New Provider

1. Install the AI SDK adapter: `npm install @ai-sdk/anthropic`
2. Add to `app/lib/providers.ts`:

```ts
import { anthropic } from "@ai-sdk/anthropic";

// Add to ProviderId union:
export type ProviderId = "groq" | "google" | "openai" | "anthropic";

// Add to providers record:
anthropic: {
  id: "anthropic",
  name: "Anthropic",
  icon: "◆",
  color: "#d97706",
  getModel: (modelId) => anthropic(modelId),
},
```

3. Add the provider's models to `app/lib/models.ts`
4. Add `ANTHROPIC_API_KEY` to `.env.local`
5. Add `"anthropic"` to `PROVIDER_ORDER` in `ModelSelector.tsx`

---

## 📦 Scripts

```bash
npm run dev      # Start dev server with Turbopack (hot reload)
npm run build    # Build production bundle
npm run start    # Start production server
npm run lint     # Run ESLint
```

---

## 📄 License

MIT — free to use, modify, and distribute.

---

> Built as part of the **Agentic AI Lab** learning series — Day 47.
