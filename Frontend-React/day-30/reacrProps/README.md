# Day 30 - React Fundamentals

## Overview

After completing Python and FastAPI, I started my React journey.

Today I learned the foundational concepts of React including JSX, Components, and Props by building a reusable Profile Card application.

---

# What is React?

React is a JavaScript library developed by Meta (Facebook) for building user interfaces.

It helps developers create interactive and reusable UI components.

Key Features:

- Component-Based Architecture
- Reusable UI Elements
- Virtual DOM
- Fast Rendering
- Large Ecosystem

Example:

```jsx
function App() {
  return <h1>Hello React</h1>;
}
```

---

# What is Vite?

Vite is a modern frontend build tool used to create React applications quickly.

Benefits:

- Fast Development Server
- Instant Hot Reloading
- Lightweight Setup
- Better Performance than Create React App

Create Project:

```bash
npm create vite@latest
```

---

# What is JSX?

JSX stands for JavaScript XML.

It allows developers to write HTML-like syntax inside JavaScript.

Example:

```jsx
const element = <h1>Hello React</h1>;
```

JSX makes UI code easier to read and write.

---

# What are Components?

Components are reusable building blocks in React.

Instead of writing the same UI repeatedly, components allow code reuse.

Example:

```jsx
function ProfileCard() {
  return <h2>Saurabh Kumar</h2>;
}
```

Benefits:

- Reusability
- Maintainability
- Better Code Organization

---

# What are Props?

Props (Properties) are used to pass data from a parent component to a child component.

Example:

```jsx
<ProfileCard
  name="Saurabh"
  role="GenAI Engineer"
/>
```

Receiving Props:

```jsx
function ProfileCard(props) {
  return (
    <>
      <h2>{props.name}</h2>
      <p>{props.role}</p>
    </>
  );
}
```

---

# Passing Data Using Props

Props make components dynamic.

Example:

```jsx
<ProfileCard
  name="Saurabh"
  role="Full Stack Developer"
/>

<ProfileCard
  name="John"
  role="Frontend Developer"
/>
```

The same component can display different data.

---

# Reusable Components

One component can be used multiple times with different data.

Benefits:

- Less Code
- Easier Maintenance
- Better Scalability

Example:

```jsx
<ProfileCard />
<ProfileCard />
<ProfileCard />
```

This follows the DRY principle:

Don't Repeat Yourself.

---

# Project

Profile Card Application

Features:

- React Components
- JSX
- Props
- Dynamic Data Rendering
- Reusable Component Design

---

# Learning Outcome

Today I learned:

- What React is
- What Vite is
- What JSX is
- What Components are
- What Props are
- Passing Data using Props
- Creating Reusable Components

---

# Next Day

Day 31

Topics:

- useState
- Events
- Input Handling
- Counter Application