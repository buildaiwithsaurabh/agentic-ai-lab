# Day 42 - Data Fetching in Next.js

## Project

GitHub Developer Dashboard

---

# Topics Covered

- Data Fetching
- Async Server Components
- fetch()
- Server-side Rendering
- API Integration
- Rendering Dynamic Data
- Error Handling

---

# What is Data Fetching?

Data Fetching is the process of retrieving data from an external source such as:

- REST APIs
- Databases
- CMS
- Backend Services

---

# Why Next.js Data Fetching?

Unlike React, Next.js allows fetching data directly inside Server Components.

Example:

```tsx
export default async function Home() {
  const response = await fetch(url);

  const data = await response.json();

  return <div>...</div>;
}
```

No `useEffect` required.

---

# Async Server Components

Server Components can be asynchronous.

Example:

```tsx
export default async function Home() {

}
```

This allows:

- Database Queries
- API Calls
- Authentication
- AI Requests

before rendering HTML.

---

# fetch()

Example

```tsx
const response = await fetch(
  "https://api.github.com/users"
);

const users = await response.json();
```

---

# Rendering API Data

```tsx
users.map((user) => (
  <UserCard
    key={user.id}
    user={user}
  />
))
```

---

# Why use `cache: "no-store"`?

```tsx
await fetch(url, {
  cache: "no-store",
});
```

Always fetches fresh data.

Useful for:

- Dashboards
- Live Analytics
- Admin Panels

---

# Project Flow

```
GitHub API

↓

fetch()

↓

Server Component

↓

UserCard

↓

Browser
```

---

# Folder Structure

```
app/

│

├── components/

│ ├── Navbar.tsx

│ ├── UserCard.tsx

│ └── Footer.tsx

│

├── globals.css

├── layout.tsx

└── page.tsx
```

---

# Learning Outcome

Today I learned:

- Async Server Components
- Data Fetching
- fetch()
- API Integration
- Server-side Rendering
- Rendering Dynamic Data
- Component Composition

---

# Next Day

## Topics

- loading.tsx
- error.tsx
- not-found.tsx
- Suspense
- Streaming UI

## Project

GitHub Explorer with Loading & Error UI