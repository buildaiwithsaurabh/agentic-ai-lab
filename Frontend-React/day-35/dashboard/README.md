# Day 35 - React CRUD with Axios

## Project

Product Management Dashboard

---

# Topics Covered

- Axios
- GET Request
- POST Simulation
- DELETE Operation
- CRUD
- State Updates

---

# What is Axios?

Axios is a promise-based HTTP client used to communicate with REST APIs.

Install:

```bash
npm install axios
```

Example:

```jsx
const response = await axios.get(url);
```

---

# Why Axios?

Compared to Fetch API:

- Cleaner syntax
- Automatic JSON parsing
- Better error handling
- Request interceptors
- Response interceptors

---

# CRUD Operations

CRUD stands for:

- Create
- Read
- Update
- Delete

Today's project includes:

✔ Read products from API

✔ Create products locally

✔ Delete products locally

---

# GET Request

```jsx
axios.get(url)
```

Fetches data from an API.

---

# POST Simulation

Instead of sending data to a backend, today's project updates local React state.

```jsx
setProducts([newProduct,...products]);
```

---

# DELETE Operation

```jsx
products.filter(...)
```

Removes a product from the UI.

---

# Why Stable Keys?

Products use:

```jsx
key={product.id}
```

instead of

```jsx
key={index}
```

---

# Features

- Product Dashboard
- API Integration
- Add Product
- Delete Product
- Dynamic Rendering

---

# Learning Outcome

Today I learned:

- Axios
- CRUD Basics
- GET Requests
- React State Updates
- Delete Operations

---

# Next Day

Topics

- React Router
- Routes
- Link
- NavLink
- useNavigate

Project

Travel Explorer