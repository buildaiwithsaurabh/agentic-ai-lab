# Day 37 - React Context API & Theme Switcher

## Project

Developer Profile Directory

A React application that demonstrates **Context API**, **Global State Management**, and **Theme Switching** using reusable components.

---

# Concepts Covered

- createContext()
- useContext()
- Context Provider
- Global State
- Theme Switching
- Reusable Components
- Props
- map()
- Conditional Rendering

---

# Folder Structure

```
src/
│
├── components/
│   ├── Navbar.jsx
│   └── ProfileCard.jsx
│
├── context/
│   └── ThemeContext.jsx
│
├── data/
│   └── developers.js
│
├── App.jsx
├── main.jsx
└── index.css
```

---

# What is Context API?

Context API is React's built-in solution for sharing data across multiple components without passing props through every level of the component tree.

Example:

```
Theme

↓

Navbar

↓

Profile Card

↓

Footer
```

Every component can access the same data.

---

# Why Context API?

Without Context API:

```
App

↓

Navbar

↓

Button

↓

Child

↓

Profile Card
```

Props must be passed manually through every component (**props drilling**).

With Context API:

```
Theme Context

↓

Any Component
```

Components can directly access shared data.

---

# createContext()

Creates a context object.

```jsx
const ThemeContext = createContext();
```

---

# Provider

The Provider makes context values available to all child components.

```jsx
<ThemeProvider>
    <App />
</ThemeProvider>
```

---

# useContext()

Reads values from the nearest Provider.

```jsx
const { theme } = useTheme();
```

---

# Theme Switching

The application supports:

- 🌞 Light Mode
- 🌙 Dark Mode

The current theme is shared globally using Context API.

---

# Project Features

- Developer Directory
- Multiple Profile Cards
- Reusable Components
- Skills Section
- GitHub Profile Button
- Global Theme Management
- Light & Dark Mode
- Responsive Layout

---

# Learning Outcome

Today I learned:

- Context API
- createContext
- useContext
- Provider
- Global State
- Theme Switcher
- Component Communication

---

# Next Day

## Topics

- Custom Hooks
- useMemo
- useCallback
- Performance Optimization

## Project

Developer Analytics Dashboard