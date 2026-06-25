# Day 33 - React Forms, Validation & Search

## Project

Student Management System

---

# Topics Covered

- Forms
- Controlled Components
- Form Validation
- Search Functionality
- Filtering
- UUID
- Stable Keys
- useState

---

# What are Forms?

Forms collect user input.

Example:

```jsx
<input />
```

React uses forms to collect data like:

- Login
- Registration
- Contact Forms

---

# Controlled Components

React controls the value of the input.

```jsx
const [studentName, setStudentName] = useState("");

<input
   value={studentName}
   onChange={(e)=>setStudentName(e.target.value)}
/>
```

Benefits:

- Predictable UI
- Easy Validation
- Easy API Submission

---

# Form Validation

Validation prevents invalid input.

Example:

```jsx
if(studentName.trim()===""){
   alert("Student name is required");
}
```

---

# Search Functionality

Search filters data based on user input.

Example:

```jsx
students.filter(...)
```

---

# Why use Objects instead of Strings?

Instead of:

```js
[
 "Saurabh",
 "Rahul"
]
```

Use:

```js
[
 {
   id:"123",
   name:"Saurabh"
 },
 {
   id:"456",
   name:"Rahul"
 }
]
```

Benefits:

- Better scalability
- Easier CRUD operations
- Stable unique keys

---

# What is a React Key?

A key uniquely identifies each item in a list.

Bad:

```jsx
key={index}
```

Good:

```jsx
key={student.id}
```

Stable keys prevent rendering bugs when:

- Sorting
- Filtering
- Updating
- Deleting

---

# Why crypto.randomUUID()?

```jsx
id: crypto.randomUUID()
```

Generates a unique ID for every student.

This mimics how IDs come from a database like PostgreSQL or Supabase.

---

# Features

- Register Student
- Search Student
- Validation
- Stable React Keys
- Dynamic UI
- Real-time Filtering

---

# Learning Outcome

Today I learned:

- Forms
- Controlled Components
- Validation
- Search
- Filtering
- UUID
- React Keys
- Best Practices for List Rendering

---

# Next Day

Day 34

Topics:

- useEffect
- Fetch API
- Loading State
- Error Handling

Project:

Employee Directory (API Integration)