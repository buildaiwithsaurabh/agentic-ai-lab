# Day 34 - React API Integration with useEffect

## Project

User Directory Dashboard

---

# Topics Covered

- useEffect Hook
- Fetch API
- Loading State
- Error Handling
- API Integration
- Rendering Dynamic Data

---

# What is useEffect?

useEffect is a React Hook used to perform side effects inside components.

Examples:

- API Calls
- Timers
- Event Listeners
- Local Storage

Example:

```jsx
useEffect(() => {
    fetchUsers();
}, []);
```

The empty dependency array (`[]`) means the effect runs once when the component is first rendered.

---

# Why use useEffect?

Without useEffect, an API request would run on every render.

useEffect allows React to control when side effects should execute.

---

# What is Fetch API?

Fetch API is a built-in JavaScript API used to request data from a server.

Example:

```jsx
const response = await fetch(url);
const data = await response.json();
```

---

# Loading State

While waiting for the API response, display feedback to the user.

Example:

```jsx
if (loading) {
    return <h2>Loading...</h2>;
}
```

---

# Error Handling

Always handle request failures.

Example:

```jsx
try {
    ...
}
catch(error){
    setError(error.message);
}
```

---

# Why Stable Keys?

API data already contains unique IDs.

Example:

```jsx
key={user.id}
```

Avoid using:

```jsx
key={index}
```

---

# Features

- Fetch Users
- Loading Indicator
- Error Handling
- User Cards
- Responsive Layout

---

# Learning Outcome

Today I learned:

- useEffect
- Fetch API
- Async/Await
- Loading States
- Error Handling
- Rendering API Data

---

# Next Day

## Topics

- Axios
- CRUD Operations
- POST Request
- DELETE Request

## Project

Product Management Dashboard