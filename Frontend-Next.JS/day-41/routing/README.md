# Day 41 - Dynamic Routing in Next.js

## Project

Developer Directory

---

# Topics Covered

- Dynamic Routing
- Dynamic Segments
- params
- generateStaticParams()
- notFound()
- Link
- App Router

---

# What is Dynamic Routing?

Dynamic Routing allows pages to be generated using URL parameters.

Example:

```
/developers/1

/developers/2

/developers/3
```

Instead of creating separate pages manually.

---

# Dynamic Segments

Folders inside square brackets become dynamic.

Example

```
developers/

↓

[id]

↓

page.tsx
```

The URL

```
/developers/1
```

passes

```tsx
params.id
```

---

# params

Next.js automatically provides route parameters.

Example

```tsx
export default function Page({
    params
}){

console.log(params.id)

}
```

---

# generateStaticParams()

Used to pre-generate dynamic pages during build time.

Example

```tsx
export async function generateStaticParams(){

return developers.map(dev=>({
id:dev.id.toString()
}))

}
```

---

# notFound()

Displays the built-in 404 page.

```tsx
if(!developer){

notFound()

}
```

---

# Project Flow

```
Home

↓

Developer List

↓

Developer Card

↓

Dynamic Route

↓

Developer Details
```

---

# Folder Structure

```
app/

│

├── developers/

│ ├── page.tsx

│ └── [id]/

│ └── page.tsx

│

├── components/

├── data/

├── layout.tsx

└── page.tsx
```

---

# Learning Outcome

Today I learned:

- Dynamic Routing
- Dynamic Segments
- params
- generateStaticParams
- notFound
- Link Navigation
- Dynamic Pages

---

# Next Day

Topics

- Data Fetching
- fetch()
- Async Server Components
- Loading UI

Project

GitHub Developer Dashboard