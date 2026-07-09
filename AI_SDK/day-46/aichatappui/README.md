# 🤖 AI Chat Assistant - Day 46

A premium, modern AI Chat Assistant application built with **Next.js 16 (App Router)**, the **Vercel AI SDK 5**, and the **Groq Llama 3.3** model. This project demonstrates high-performance text streaming, responsive design system patterns, clean markdown parsing, and robust state management.

---

## 🌟 Key Features

*   **⚡ Real-Time Streaming Responses**: Responses stream word-by-word instantly from the Groq API.
*   **📖 Markdown & Table Rendering**: Fully supports rich markdown parsing (including lists, headers, code, inline code, and GFM tables).
*   **💻 Code Highlighting**: Elegant Prism syntax highlighting with a custom VS-Code-like dark theme (`vscDarkPlus`).
*   **📋 Individual Code Copy State**: Each code block maintains its own independent copy-to-clipboard state, preventing visual conflicts.
*   **🧠 Smart Auto-Scroll Hook**: Custom viewport scrolling hook that automatically snaps downward on new responses *only* if the user is already at the bottom or sent a message, preserving scroll state if they scroll up to read history.
*   **💬 Modern Typing Animation**: Clean, active, animated typing bubbles combined with a modern bot avatar.
*   **♻️ Smart Loading & Error Handling**: Beautiful error banners with inline retry capabilities and disabled state indicators.

---

## 📂 Folder & File Architecture

The codebase has been refactored to match a clean, modular structure. Below is the file mapping showing the new architecture and refactored components:

```text
aichatappui/
├── app/
│   ├── api/
│   │   └── chat/
│   │       └── route.ts         # Serverless API streaming controller
│   ├── components/
│   │   ├── Chat.tsx             # Main chat window coordinator
│   │   ├── ChatInput.tsx        # User input text bar
│   │   ├── EmptyState.tsx       # Initial suggestions grid
│   │   ├── Message.tsx          # Render wrapper for user & bot dialogue bubbles
│   │   ├── CodeBlock.tsx        # [NEW] Code rendering, copying, and syntax highlighting
│   │   ├── TypingIndicator.tsx  # [NEW] Animated bot active typing states
│   │   └── Navbar.tsx           # Premium top navigation header
│   ├── hooks/
│   │   └── useAutoScroll.ts     # [NEW] Scroll position and view anchor hook
│   ├── globals.css              # Custom HSL-based stylesheet
│   ├── layout.tsx               # Root Next.js metadata and body configuration
│   └── page.tsx                 # Root landing layout
├── .env.local                   # Environment keys (e.g., GROQ_API_KEY)
├── package.json                 # [NEW] Workspace dependencies and scripts
└── tsconfig.json                # [NEW] TypeScript compiler options and path aliases
```

---

## 🛠️ Components Explained

### 1. `useAutoScroll.ts` (Custom Hook)
Abstracts scroll logic out of rendering components. It exposes `scrollContainerRef` and `messagesEndRef`. It checks:
```typescript
const isNearBottom = container.scrollHeight - container.scrollTop - container.clientHeight <= threshold;
```
If `isNearBottom` evaluates to `true` (or the last message belongs to the user), the hook fires a smooth animation scrolling to the bottom. Otherwise, it locks the position so that the user's manual reading is not interrupted.

### 2. `CodeBlock.tsx` (Component)
Handles rendering for triple-backtick markdown blocks.
*   Features its own localized `copied` state.
*   Displays the detected language name in an uppercase header.
*   Wraps the `Prism` engine from `react-syntax-highlighter` to parse code dynamically.

### 3. `TypingIndicator.tsx` (Component)
Renders a visual indicator demonstrating the AI model's generation status. Shows a standard `<Bot />` avatar alongside a three-dot CSS scaling animation.

### 4. `Message.tsx` (Component)
Converts markdown text to React elements. If a code block is detected, it delegates rendering to `<CodeBlock />` while handling inline-code with local styles.

---

## 🚀 How to Run the App

1.  **Install dependencies**:
    Ensure you run it with legacy peer dependency resolution:
    ```bash
    npm install --legacy-peer-deps
    ```

2.  **Configure Environment**:
    Create a `.env.local` file at the root of the project:
    ```env
    GROQ_API_KEY=your_actual_groq_api_key_here
    ```

3.  **Start Dev Server**:
    Launch the dev compiler (Turbopack):
    ```bash
    npm run dev
    ```

4.  **Production Compilation**:
    Build and optimize for production:
    ```bash
    npm run build
    ```
