# Day 39 - Introduction to Next.js

## Project

Developer Portfolio Website

---

# What is Next.js?

Next.js is a React framework developed by Vercel that enables developers to build production-ready web applications with features like routing, server-side rendering, static generation, API routes, and optimized performance.

---

# Why Next.js?

Benefits include:

- File-based Routing
- App Router
- Server Components
- Client Components
- Metadata API
- Image Optimization
- SEO
- Fast Performance
- API Routes
- Full-Stack Development

---

# App Router

The App Router uses the `app` directory to define routes.

Example:

```
app/
│
├── page.tsx
├── about/
│   └── page.tsx
```

Automatically creates:

```
/
```

and

```
/about
```

---

# Routing

Every folder containing a `page.tsx` file becomes a route.

Example:

```
app/projects/page.tsx
```

becomes:

```
/projects
```

---

# Layout

`layout.tsx` defines shared UI across all pages.

Typical use cases:

- Navbar
- Footer
- Sidebar

---

# Link

Use Next.js `Link` instead of HTML `<a>` for client-side navigation.

Example:

```tsx
import Link from "next/link";

<Link href="/about">
  About
</Link>
```

---

# Metadata

Metadata controls SEO information.

Example:

```tsx
export const metadata = {
  title: "Developer Portfolio",
  description: "Learning Next.js"
}
```

---

# Project Structure

```
app/
│
├── components/
├── about/
├── projects/
├── contact/
├── globals.css
├── layout.tsx
└── page.tsx
```

---

# Learning Outcome

Today I learned:

- What is Next.js
- Why Next.js
- App Router
- Routing
- Layout
- Link
- Metadata
- Project Structure

---

# Next Day

Topics:

- Client Components
- Server Components
- "use client"
- Navigation
- Images
- Fonts

Project:

Developer Portfolio v2