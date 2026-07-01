# Day 38 - TypeScript Fundamentals

## Project

Student Information System

---

# What is TypeScript?

TypeScript is a statically typed superset of JavaScript developed by Microsoft.

It adds type safety to JavaScript.

Example:

```ts
let age: number = 24;
```

---

# Why TypeScript?

- Better IntelliSense
- Detects errors before runtime
- Easier refactoring
- Improved maintainability
- Industry standard for React and Next.js

---

# Topics Covered

- Primitive Types
- Arrays
- Objects
- Functions
- Type Inference
- Union Types
- Literal Types
- any
- unknown

---

# Primitive Types

```ts
let name: string = "Saurabh";
let age: number = 24;
let active: boolean = true;
```

---

# Arrays

```ts
let skills: string[] = [
  "React",
  "Next.js"
];
```

---

# Objects

```ts
let student = {
   id:1,
   name:"Saurabh"
}
```

---

# Functions

```ts
function greet(name:string):string{
    return `Welcome ${name}`;
}
```

---

# Union Types

```ts
let id:number | string;
```

Allows multiple types.

---

# Literal Types

```ts
type Role = "Admin" | "Student";
```

Restricts values.

---

# any

```ts
let value:any;
```

Disables type checking.

Avoid when possible.

---

# unknown

Safer than `any`.

Requires type checking before use.

---

# Type Inference

TypeScript can infer types automatically.

```ts
let city = "Bhopal";
```

TypeScript understands this is a `string`.

---

# Learning Outcome

Today I learned:

- TypeScript Basics
- Static Typing
- Primitive Types
- Arrays
- Objects
- Functions
- Union Types
- Literal Types
- any vs unknown
- Type Inference

---

# Next Day

Day 39

Topics

- Interfaces
- Type Aliases
- Optional Properties
- Enums
- Generics

Project

Employee Management System