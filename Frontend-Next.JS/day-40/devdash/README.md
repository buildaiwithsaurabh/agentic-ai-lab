# Day 40 - Server Components vs Client Components

## Project

Developer Dashboard

---

# Topics Covered

- Server Components
- Client Components
- "use client"
- useState
- Event Handling
- Component Composition

---

# What is a Server Component?

Server Components run on the server by default.

Advantages:

- Faster
- Better SEO
- Smaller JavaScript bundle
- Secure

Example:

```tsx
export default function Header(){
   return <h1>Hello</h1>
}
```

---

# What is a Client Component?

Client Components run in the browser.

Required for:

- useState
- useEffect
- Event Handling
- Browser APIs

Example:

```tsx
"use client";

import {useState} from "react";
```

---

# Why "use client"?

Next.js treats every component as a Server Component by default.

If you need:

- useState
- useEffect
- onClick

you must add:

```tsx
"use client";
```

---

# Server vs Client

| Server | Client |
|---------|---------|
| SEO | Interactive UI |
| Fast | Browser Logic |
| Secure | Event Handling |
| Database | Forms |

---

# Learning Outcome

Today I learned:

- Server Components
- Client Components
- use client
- Component Composition
- Interactive Components

---

# Next Day

Topics

- Dynamic Routing
- useParams
- Dynamic Pages

Project

Developer Portfolio Dynamic Routes