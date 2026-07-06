# Day 43 - Next.js Route Handlers (API Routes)

## Project

**Developer API Dashboard**

A beginner-friendly project demonstrating how to build REST APIs using **Next.js App Router Route Handlers**.

---

# Learning Objectives

Today I learned how to build backend APIs directly inside a Next.js application using Route Handlers.

Topics Covered:

- Route Handlers
- API Routes
- GET Request
- POST Request
- Request Object
- Response Object
- NextResponse
- JSON Response
- API Testing

---

# Project Structure

```
frontend-nextjs/
└── day-43/
    ├── app/
    │
    ├── api/
    │   ├── quotes/
    │   │   └── route.ts
    │   │
    │   └── developers/
    │       └── route.ts
    │
    ├── components/
    │   ├── Navbar.tsx
    │   ├── QuoteCard.tsx
    │   └── DeveloperCard.tsx
    │
    ├── data/
    │   ├── quotes.ts
    │   └── developers.ts
    │
    ├── globals.css
    ├── layout.tsx
    └── page.tsx
    │
    └── README.md
```

---

# What are Route Handlers?

Route Handlers allow you to create backend API endpoints inside the **app/api** directory.

Instead of creating a separate Express or FastAPI server, Next.js lets you build APIs within the same project.

Example:

```
app/

↓

api/

↓

quotes/

↓

route.ts
```

Automatically creates

```
/api/quotes
```

---

# Why Route Handlers?

Benefits:

- No separate backend required
- Full-stack development
- Built into Next.js
- Easy API creation
- Server-side execution
- Perfect for AI applications

---

# Folder Convention

```
app/
│
├── api/
│   ├── quotes/
│   │   └── route.ts
│   │
│   └── developers/
│       └── route.ts
```

Each folder containing `route.ts` becomes an API endpoint.

---

# GET Request

Used to retrieve data.

Example

```ts
export async function GET() {
    return NextResponse.json(data);
}
```

Request

```
GET /api/quotes
```

Response

```json
{
  "success": true,
  "data": []
}
```

---

# POST Request

Used to create new data.

Example

```ts
export async function POST(request: Request) {

}
```

Read request body

```ts
const body = await request.json();
```

---

# Request Object

The Request object contains:

- Body
- Headers
- URL
- Method

Example

```ts
const body = await request.json();
```

---

# Response Object

Responses are returned using

```ts
NextResponse.json()
```

Example

```ts
return NextResponse.json({
    success: true
});
```

---

# HTTP Status Codes

Common status codes used:

| Code | Meaning |
|------|----------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Internal Server Error |

Example

```ts
return NextResponse.json(
    {
        success:false
    },
    {
        status:400
    }
);
```

---

# API Endpoints

## Quotes API

### GET

```
GET /api/quotes
```

Returns all quotes.

---

### POST

```
POST /api/quotes
```

Creates a new quote.

Example Body

```json
{
  "quote":"Never stop learning.",
  "author":"Saurabh Kumar"
}
```

---

## Developers API

### GET

```
GET /api/developers
```

Returns all developers.

---

# Testing APIs

Open browser:

```
http://localhost:3000/api/quotes
```

or

```
http://localhost:3000/api/developers
```

For POST requests use:

- Postman
- Thunder Client
- VS Code REST Client
- Insomnia

---

# Project Flow

```
Browser

↓

API Request

↓

Route Handler

↓

Data Layer

↓

NextResponse

↓

JSON Response

↓

Browser
```

---

# Route Handler Flow

```
GET /api/quotes

↓

route.ts

↓

quotes.ts

↓

NextResponse.json()

↓

JSON
```

---

# Why This Matters

Every AI application follows the same architecture.

Example:

```
React UI

↓

POST /api/chat

↓

Route Handler

↓

OpenAI / Gemini

↓

Streaming Response

↓

Browser
```

Today's learning builds the foundation for:

- AI SDK
- OpenAI API
- Gemini API
- Groq API
- RAG
- AI Agents

---

# Learning Outcome

Today I learned:

- Route Handlers
- API Routes
- GET APIs
- POST APIs
- Request Object
- Response Object
- NextResponse
- JSON Responses
- HTTP Status Codes

---

# Next Day

## Topics

- Server Actions
- Forms
- Form Actions
- Validation

## Project

Feedback Management System

---

# Repository

GitHub

```
https://github.com/buildaiwithsaurabh/agentic-ai-lab.git
```

---

## Repository Commit

```bash
git add .

git commit -m "feat(day-43): build Next.js route handlers with GET and POST APIs"

git push origin main
```

---

## Final Learning Roadmap

```
React ✅

↓

TypeScript ✅

↓

Next.js App Router ✅

↓

Server & Client Components ✅

↓

Dynamic Routing ✅

↓

Data Fetching ✅

↓

Route Handlers ✅

↓

Server Actions

↓

AI SDK

↓

Supabase

↓

OpenAI / Gemini

↓

RAG

↓

AI Agents

↓

Agentic AI
```