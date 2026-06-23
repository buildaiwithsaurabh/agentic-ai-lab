# Day 31 - React State & Events

## Project

Student Registration Dashboard

## Concepts Covered

### useState

The useState hook allows React components to store and update data.

Example:

```jsx
const [name, setName] = useState("");
```

---

### State Management

State represents dynamic data that changes over time.

Examples:

- Student Name
- Student Count
- Student List

---

### Events

Events allow users to interact with the application.

Examples:

- Button Click
- Input Change

---

### onClick

Used when a button is clicked.

```jsx
<button onClick={addStudent}>
```

---

### onChange

Used when input values change.

```jsx
onChange={(e) => setName(e.target.value)}
```

---

### Input Handling

React stores input values inside state and updates the UI dynamically.

---

## Features

- Add Student
- Display Student Count
- Display Student List
- Dynamic UI Updates

---

## Learning Outcome

Today I learned:

- useState Hook
- State Management
- Event Handling
- onClick Event
- onChange Event
- Input Handling