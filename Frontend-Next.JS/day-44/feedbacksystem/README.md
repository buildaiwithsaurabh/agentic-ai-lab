# Day 44 - Server Actions in Next.js

## 🚀 Project

**Feedback Management System**

A beginner-friendly Next.js project demonstrating how to use **Server Actions** to handle form submissions without creating traditional API Routes.

---

# 📚 Topics Covered

- Server Actions
- `"use server"`
- Form Submission
- FormData
- Server-side Validation
- Reusable Components
- App Router
- Data Layer
- Component-Based Architecture

---

# 📁 Project Structure

```text
frontend-nextjs/
└── day-44/
    ├── app/
    │
    ├── actions/
    │   └── feedback.ts
    │
    ├── components/
    │   ├── Navbar.tsx
    │   ├── FeedbackForm.tsx
    │   ├── FeedbackList.tsx
    │   └── SuccessMessage.tsx
    │
    ├── data/
    │   └── feedback.ts
    │
    ├── globals.css
    ├── layout.tsx
    └── page.tsx
    │
    └── README.md
```

---

# 🌐 What are Server Actions?

Server Actions are a feature introduced in the **Next.js App Router** that allows forms and other interactions to execute server-side functions directly.

Instead of creating a REST API endpoint, you can call a server function from a form.

Traditional Flow

```
Form

↓

fetch()

↓

API Route

↓

Database

↓

Response
```

Server Action Flow

```
Form

↓

Server Action

↓

Database

↓

Updated UI
```

---

# 🤔 Why Server Actions?

Benefits

- Less boilerplate
- No API Routes required
- Better developer experience
- Secure server-side execution
- Built into Next.js
- Ideal for forms and mutations

---

# 📌 The `"use server"` Directive

A Server Action must begin with:

```ts
"use server";
```

Example

```ts
"use server";

export async function submitFeedback() {

}
```

This tells Next.js to execute the function on the server.

---

# 📝 Form Submission

Instead of using JavaScript fetch requests,

Traditional React

```tsx
await fetch("/api/feedback");
```

Next.js Server Actions

```tsx
<form action={submitFeedback}>
```

That's all.

---

# 📥 Reading Form Data

The browser automatically sends the form values.

Example

```ts
export async function submitFeedback(
    formData: FormData
){

}
```

Read values

```ts
const name = formData.get("name");

const email = formData.get("email");

const message = formData.get("message");
```

---

# ✅ Server-side Validation

Validation happens before saving data.

Example

```ts
if(!name || !email || !message){

    return;

}
```

This prevents invalid submissions.

---

# 💾 Saving Data

For this demo, data is stored in an in-memory array.

```ts
feedbackList.push(newFeedback);
```

In production applications you would save to:

- PostgreSQL
- Supabase
- Prisma
- MongoDB

Example

```ts
await db.feedback.create({

data:{
name,
email,
message
}

})
```

---

# 🧩 Project Architecture

```
Browser

↓

Feedback Form

↓

Server Action

↓

Validation

↓

Store Data

↓

Return Response

↓

Updated UI
```

---

# 📂 Components

### Navbar

Displays navigation links.

---

### FeedbackForm

Collects user feedback.

---

### FeedbackList

Displays submitted feedback.

---

### SuccessMessage

Shows confirmation after submission.

---

# 📂 Data Layer

```
feedback.ts
```

Stores sample feedback data.

This mimics a database until a real database is connected.

---

# 📄 Server Action

```
submitFeedback()
```

Responsibilities

- Read FormData
- Validate Inputs
- Create Feedback Object
- Store Data
- Return Success

---

# ⚙️ FormData

FormData is automatically provided by the browser.

Example

```ts
formData.get("name")

formData.get("email")

formData.get("message")
```

No JSON parsing is required.

---

# 🚀 Why This Matters

Server Actions are widely used for:

- Login Forms
- Registration
- Contact Forms
- Feedback Systems
- Comments
- AI Prompt Submission
- Chat Applications
- Database Mutations

---

# 🤖 Preparing for AI Applications

Today's architecture is almost identical to an AI application.

Today

```
Feedback Form

↓

Server Action

↓

Save Data

↓

Success
```

Tomorrow

```
Chat Form

↓

Server Action

↓

Vercel AI SDK

↓

OpenAI

↓

Gemini

↓

Groq

↓

Streaming Response

↓

Chat UI
```

Understanding Server Actions makes AI integration much easier.

---

# 🎯 Learning Outcome

Today I learned:

- Server Actions
- `"use server"`
- Form Submission
- FormData
- Validation
- Server-side Functions
- Component Communication
- Data Flow in Next.js

---

# 📈 Next Learning

## Day 45

### Vercel AI SDK

Topics

- AI SDK
- Chat Interface
- Streaming Responses
- OpenAI Integration
- Gemini Integration
- AI Messages
- Markdown Rendering

Project

**AI Chat Assistant**

---

# 🛠️ Tech Stack

- Next.js 15
- React
- TypeScript
- App Router
- Server Actions
- CSS

---

# 📚 Key Concepts

| Concept | Description |
|----------|-------------|
| Server Actions | Execute server-side functions directly from forms |
| `"use server"` | Marks a function to run on the server |
| FormData | Reads submitted form values |
| Validation | Ensures valid user input |
| Components | Build reusable UI |
| Data Layer | Temporary in-memory storage |

---

# 📌 Repository

GitHub

```
https://github.com/buildaiwithsaurabh/agentic-ai-lab.git
```

---

## 📦 Repository Commit

```bash
git add .

git commit -m "feat(day-44): implement Next.js server actions with feedback management system"

git push origin main
```

---

# 🗺️ Learning Roadmap

```
✅ FastAPI

↓

✅ React

↓

✅ TypeScript

↓

✅ Next.js App Router

↓

✅ Server & Client Components

↓

✅ Dynamic Routing

↓

✅ Data Fetching

↓

✅ Route Handlers

↓

✅ Server Actions

↓

🚀 Vercel AI SDK

↓

OpenAI / Gemini / Groq

↓

Supabase

↓

RAG

↓

AI Agents

↓

Agentic AI

↓

Vertical AI SaaS Products
```